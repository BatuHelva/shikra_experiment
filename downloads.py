import requests
import os
import torch
from transformers import LlamaForCausalLM, LlamaConfig

# Create a directory to save the downloaded files
os.makedirs("llama-7b", exist_ok=True)

# List of files to download
files = [
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

# Create a directory to save the downloaded files
os.makedirs("shikras-7b/shikra-7b-delta-v1/", exist_ok=True)

# List of files to download
files = [
    "pytorch_model-00001-of-00002.bin",
    "pytorch_model-00002-of-00002.bin",
    "pytorch_model.bin.index.json"  # This is the index file needed to load sharded models
]

# Base URL for the repository
base_url = "https://huggingface.co/shikras/shikra-7b-delta-v1/resolve/main/"

for file_name in files:
    url = base_url + file_name
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join("shikras-7b/shikra-7b-delta-v1/", file_name), "wb") as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")
