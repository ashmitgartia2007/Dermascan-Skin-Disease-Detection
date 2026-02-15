
import os
import shutil

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
source_dir = os.path.join(dataset_dir, "skin disease Actinic keratosis")

# Ensure source exists
if not os.path.exists(source_dir) or not os.listdir(source_dir):
    print("Source dir empty or missing!")
    exit(1)

files = os.listdir(source_dir)[:5] # Take 5 images

for idx, name in classes.items():
    target_dir = os.path.join(dataset_dir, f"skin disease {name}")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created {target_dir}")
        for f in files:
            src = os.path.join(source_dir, f)
            dst = os.path.join(target_dir, f)
            if os.path.isfile(src):
                shutil.copy(src, dst)
        print(f"Populated {target_dir} with dummy data")
    elif len(os.listdir(target_dir)) == 0:
         print(f"Populating empty {target_dir}")
         for f in files:
            src = os.path.join(source_dir, f)
            dst = os.path.join(target_dir, f)
            if os.path.isfile(src):
                shutil.copy(src, dst)

print("Dataset patching complete.")
