import requests
import os

# Path to the Downloads folder of the current user
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
os.makedirs(downloads_path, exist_ok=True)

# Insert file URL
file_url = input("Enter file URL: ").strip()

# Get file name from URL
file_name = file_url.split("/")[-1] or "downloaded_file"
save_path = os.path.join(downloads_path, file_name)

try:
    r = requests.get(file_url, stream=True)
    r.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"File saved to: {save_path}")

except requests.exceptions.RequestException as e:
    print(f"Download error: {e}")

input("Done! Press Enter to exit...")
