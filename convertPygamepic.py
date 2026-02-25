from pathlib import Path
import pygame

def convert(Folder):
    """
    Loop through a folder, convert all images to alpha, and return as a list.
    """
    folder_path = Path(Folder)
    converted_images = []
    
    # Loop through all image files in the folder
    for image_file in sorted(folder_path.glob('*')):
        if image_file.is_file() and image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            try:
                image = pygame.image.load(str(image_file)).convert_alpha()
                converted_images.append(image)
            except Exception as e:
                print(f"Error loading {image_file}: {e}")
    
    return converted_images
