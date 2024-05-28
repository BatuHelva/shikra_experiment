import requests
import os

# Create a directory to save the downloaded files
os.makedirs("llama-7b", exist_ok=True)

# List of files to download
files = [
    "config.json",
    "pytorch_model-00001-of-00002.bin",
    "pytorch_model-00002-of-00002.bin",
    "pytorch_model.bin.index.json"  # This is the index file needed to load sharded models
]

# Base URL for the repository
base_url = "https://huggingface.co/huggyllama/llama-7b/resolve/main/"

for file_name in files:
    url = base_url + file_name
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join("llama-7b", file_name), "wb") as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")
