import urllib.request
import os
import json


save_dir = './datasets/coco/val2014'
annotations_path = "./data/coco_pope_adversarial.jsonl"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to download image from URL and save it to the specified directory
def download_image(img_url, save_path):
    try:
        urllib.request.urlretrieve(img_url, save_path)
        print(f"Downloaded {img_url} to {save_path}")
    except Exception as e:
        print(f"Failed to download {img_url}. Error: {e}")


pope_coco_img_names = []

with open(annotations_path, 'r') as f:
    for line in f:
        pope_coco_img_names.append(json.loads(line)["image"])

pope_coco_image_names_set = set(pope_coco_img_names)

# Iterate over the images in the COCO annotations
for image_name in pope_coco_image_names_set:


    img_url = f"http://images.cocodataset.org/val2014/{image_name}"
    save_path = os.path.join(save_dir, image_name)

    # Download and save the image
    download_image(img_url, save_path)

print("Download completed.")
