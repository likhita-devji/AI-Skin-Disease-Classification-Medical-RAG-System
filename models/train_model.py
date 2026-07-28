"""
Skin Disease Classifier - HAM10000 Transfer Learning Trainer
Trains an EfficientNetB0 convolutional neural network on the HAM10000 skin lesion dataset.
"""

import os
import argparse

def train_tensorflow_model(data_dir: str, epochs: int = 15, batch_size: int = 32, output_model_path: str = "models/skin_disease_classifier.keras"):
    import tensorflow as tf
    from tensorflow.keras import layers, models
    from tensorflow.keras.preprocessing.image import ImageDataGenerator

    print("==================================================")
    print(" Starting EfficientNetB0 Training on HAM10000 Dataset")
    print(f" Data Directory: {data_dir}")
    print(f" Target Epochs: {epochs} | Batch Size: {batch_size}")
    print(f" Output Path: {output_model_path}")
    print("==================================================")

    # 1. Data Augmentation and Normalization
    train_datagen = ImageDataGenerator(
        preprocessing_function=tf.keras.applications.efficientnet.preprocess_input,
        rotation_range=25,
        width_shift_range=0.15,
        height_shift_range=0.15,
        shear_range=0.15,
        zoom_range=0.15,
        horizontal_flip=True,
        vertical_flip=True,
        validation_split=0.2
    )

    if not os.path.exists(data_dir):
        print(f"[Error] Data directory {data_dir} does not exist!")
        print("Please run `python download_dataset.py` first to download HAM10000.")
        return

    train_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    val_generator = train_datagen.flow_from_directory(
        data_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    num_classes = train_generator.num_classes
    print(f"Detected {num_classes} classes: {list(train_generator.class_indices.keys())}")

    # 2. Build EfficientNet Architecture
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights='imagenet',
        input_shape=(224, 224, 3)
    )
    base_model.trainable = False  # Initial feature extraction phase

    inputs = tf.keras.Input(shape=(224, 224, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs, outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
    )

    # 3. Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1),
        tf.keras.callbacks.ModelCheckpoint(output_model_path, monitor='val_accuracy', save_best_only=True, verbose=1)
    ]

    # 4. Phase 1: Feature Extraction Training
    print("\n--- Phase 1: Training Classification Head ---")
    model.fit(
        train_generator,
        epochs=max(1, epochs // 2),
        validation_data=val_generator,
        callbacks=callbacks
    )

    # 5. Phase 2: Fine-Tuning Top Layers
    print("\n--- Phase 2: Fine-tuning EfficientNet Base Layers ---")
    base_model.trainable = True
    for layer in base_model.layers[:100]:
        layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
        loss='categorical_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc')]
    )

    model.fit(
        train_generator,
        epochs=epochs,
        validation_data=val_generator,
        callbacks=callbacks
    )

    print(f"\n[Success] Training complete! Model saved to {output_model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Skin Disease Classifier")
    parser.add_argument("--data_dir", type=str, default="dataset/HAM10000", help="Path to HAM10000 directory")
    parser.add_argument("--epochs", type=int, default=10, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--output", type=str, default="models/skin_disease_classifier.keras", help="Output model file")
    
    args = parser.parse_args()
    train_tensorflow_model(args.data_dir, args.epochs, args.batch_size, args.output)
