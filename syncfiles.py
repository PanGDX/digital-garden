import os
import re
import shutil
import subprocess
import urllib.parse

def main():
    # 1. Prompt for directories with defaults
    obsidian_dir_default = "/home/pran/Documents/Pran's Vault/Media"
    content_dir_default = "/home/pran/Desktop/digital-garden/content"
    media_dir_default = "/home/pran/Documents/Pran's Vault/Media"

    obsidian_dir = input(f'input: "public obsidian directory" default: {obsidian_dir_default}\n> ').strip() or obsidian_dir_default
    content_dir = input(f'input: "final content directory" default: {content_dir_default}\n> ').strip() or content_dir_default
    media_dir = input(f'input: "obsidian media folder" default: {media_dir_default}\n> ').strip() or media_dir_default

    # 2. Setup destination media folder
    dest_media_dir = os.path.join(content_dir, "Media")
    os.makedirs(content_dir, exist_ok=True)
    os.makedirs(dest_media_dir, exist_ok=True)

    # Regex pattern to match Obsidian image wikilinks.
    # Group 1 captures the filename. The (?:\|.*?)? part ignores optional sizing like "|697"
    pattern = re.compile(r'!\[\[(.*?)(?:\|.*?)?\]\]')

    print("\n--- Processing Markdown Files ---")
    
    # 3. Iterate through the Obsidian directory
    for root, dirs, files in os.walk(obsidian_dir):
        for file in files:
            if file.endswith(".md"):
                source_md_path = os.path.join(root, file)
                
                # Calculate relative path to maintain sub-folder structures if they exist
                rel_path = os.path.relpath(root, obsidian_dir)
                dest_md_dir = os.path.join(content_dir, rel_path) if rel_path != '.' else content_dir
                os.makedirs(dest_md_dir, exist_ok=True)
                dest_md_path = os.path.join(dest_md_dir, file)

                # Read markdown content
                with open(source_md_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find all images in the current file
                matches = pattern.finditer(content)
                modified_content = content
                
                for match in matches:
                    original_wikilink = match.group(0)     # e.g., ![[Job Search Pyramid.jpg|697]]
                    image_filename = match.group(1).strip() # e.g., Job Search Pyramid.jpg

                    # Source and Destination paths for the image
                    source_image_path = os.path.join(media_dir, image_filename)
                    dest_image_path = os.path.join(dest_media_dir, image_filename)

                    # 4. Copy the image if it exists
                    if os.path.exists(source_image_path):
                        shutil.copy2(source_image_path, dest_image_path)
                    else:
                        print(f"Warning: Image '{image_filename}' not found in media folder.")

                    # 5. Replace wikilink with standard markdown link
                    # Calculate dynamic relative path from the .md file to the Media folder
                    rel_media_path = os.path.relpath(dest_media_dir, dest_md_dir)
                    
                    # URL encode the filename so spaces become %20 (Standard markdown requirement)
                    safe_image_filename = urllib.parse.quote(image_filename)
                    
                    # Format: ![Local picture](./Media/my-photo.jpg)
                    standard_md_link = f"![Local picture]({rel_media_path}/{safe_image_filename})"
                    
                    # Replace in text
                    modified_content = modified_content.replace(original_wikilink, standard_md_link)

                # Write the modified content to the destination folder
                with open(dest_md_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                print(f"Processed: {file}")

    print("\n--- Syncing Quartz ---")
    
    # 6. Run npx quartz sync
    # We run this command from the root of the digital-garden (parent of content directory)
    quartz_root_dir = os.path.dirname(content_dir) 
    
    try:
        # Running the command in the shell
        subprocess.run(["npx", "quartz", "sync"], cwd=quartz_root_dir, check=True)
        print("\nSync completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\nError running Quartz sync: {e}")
    except FileNotFoundError:
        print("\nError: 'npx' command not found. Please ensure Node.js and npm are installed.")

if __name__ == "__main__":
    main()
