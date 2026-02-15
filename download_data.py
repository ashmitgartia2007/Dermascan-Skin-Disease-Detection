
from bing_image_downloader import downloader
import os
import shutil

# Classes map matching app.py
classes = {
    0: "Actinic keratosis",
    1: "Atopic Dermatitis",
    2: "Benign keratosis",
    3: "Dermatofibroma",
    4: "Melanocytic nevus",
    5: "Melanoma",
    6: "Squamous cell carcinoma",
    7: "Tinea Ringworm Candidiasis",
    8: "Vascular lesion"
}

dataset_dir = "dataset"
if os.path.exists(dataset_dir):
    shutil.rmtree(dataset_dir)
os.makedirs(dataset_dir, exist_ok=True)

for idx, class_name in classes.items():
    print(f"Downloading images for: {class_name}")
    query_string = f"skin disease {class_name}"
    downloader.download(
        query_string, 
        limit=10, 
        output_dir=dataset_dir, 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60, 
        verbose=True
    )
    
    # Rename folder to match class index or simply keep name and use flow_from_directory
    # flow_from_directory uses folder names. We'll verify structure later.
    
print("Download complete.")
