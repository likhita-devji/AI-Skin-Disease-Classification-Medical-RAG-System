"""
HAM10000 Dataset Downloader & Structurer Utility
Downloads HAM10000 dataset files and structures them into class directories:
- dataset/HAM10000/akiec
- dataset/HAM10000/bcc
- dataset/HAM10000/bkl
- dataset/HAM10000/df
- dataset/HAM10000/mel
- dataset/HAM10000/nv
- dataset/HAM10000/vasc
"""

import os
import zipfile
import urllib.request
import pandas as pd
import shutil

DATASET_DIR = "dataset/HAM10000"
KAGGLE_DATASET_NAME = "kmader/skin-cancer-mnist-ham10000"

def setup_sample_dataset():
    """Creates directory structure and sample metadata for testing and development."""
    classes = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]
    print("[Dataset Setup] Initializing HAM10000 folder structure...")
    for cls in classes:
        cls_dir = os.path.join(DATASET_DIR, cls)
        os.makedirs(cls_dir, exist_ok=True)
    
    print(f"[Dataset Setup] Successfully created class folders in '{DATASET_DIR}'.")
    print("\n--- DATASET DOWNLOAD INSTRUCTIONS ---")
    print("Option 1 (Kaggle CLI):")
    print(f"  kaggle datasets download -d {KAGGLE_DATASET_NAME} -p {DATASET_DIR} --unzip")
    print("\nOption 2 (Direct Download links):")
    print("  Harvard Dataverse: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T")
    print("  Kaggle HAM10000: https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000")

def organize_dataset_by_metadata(metadata_csv_path: str, images_dir: str):
    """Organizes unzipped images into class directories using HAM10000_metadata.csv."""
    if not os.path.exists(metadata_csv_path):
        print(f"Metadata file '{metadata_csv_path}' not found.")
        return

    df = pd.read_csv(metadata_csv_path)
    print(f"Found {len(df)} entries in metadata CSV.")
    
    copied_count = 0
    for idx, row in df.iterrows():
        image_id = row['image_id']
        dx = row['dx']  # class label (e.g. mel, nv, bcc)
        
        img_name = f"{image_id}.jpg"
        src_path = os.path.join(images_dir, img_name)
        target_dir = os.path.join(DATASET_DIR, dx)
        dest_path = os.path.join(target_dir, img_name)

        if os.path.exists(src_path):
            os.makedirs(target_dir, exist_ok=True)
            shutil.copy(src_path, dest_path)
            copied_count += 1

    print(f"Successfully organized {copied_count} images into class folders under '{DATASET_DIR}'.")

if __name__ == "__main__":
    setup_sample_dataset()
