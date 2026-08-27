import os
import shutil

# Put the exact path of the folder you want to organize here
target_dir = os.path.expanduser("~/Downloads")

# Define the folder categories and their matching file extensions
file_types = {
    "Code": [".py", ".html", ".css", ".js", ".json"],
    "Assets": [".png", ".jpg", ".jpeg", ".gif", ".models", ".blend"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg"],
    "Docs": [".pdf", ".txt", ".md", ".docx"]
}

print("⚡ Vorphix File Optimizer Booting Up...")

# Scan the files in the directory
for filename in os.listdir(target_dir):
    filepath = os.path.join(target_dir, filename)
    
    # Skip directories, only look at actual files
    if os.path.isfile(filepath):
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Check which folder the file belongs to
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = os.path.join(target_dir, folder_name)
                
                # Create the folder if it doesn't exist yet
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Move the file inside
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"📦 Moved: {filename} ➡️ /{folder_name}")

print("✨ System clean complete. All assets organized seamlessly!")
