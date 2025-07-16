from PIL import Image
import os
import math

class ImageAnalyzer:
    def __init__(self, path="./images"):
        """Initialize the instance with a path to the images folder."""
        self.path = path
        self.image_files = os.listdir(self.path)

    def image_validity(self):
        """Check if the folder contains images."""
        if not self.image_files:
            return False
        return True

    def image_analyzer(self):
        """Analyze the first image in the folder."""
        if not self.image_validity():
            return {}  # Return an empty dictionary if no image is found

        image_name = self.image_files[0]  # Use self to access instance variable
        full_path = os.path.join(self.path, image_name)

        try:
            # Open the image
            img = Image.open(full_path)
            dithered_image = img.convert("P", dither=Image.FLOYDSTEINBERG)
            print(f"Image '{dithered_image}' opened successfully.")

            # Resize the image to fit within a max size
            img = self.image_adjustment(dithered_image)

            # Convert image to RGB
            img = img.convert("RGB")

        except FileNotFoundError:
            print("File was not found.")
            return {}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}

        # Extract colors from the image
        color_coords = self.extract_colors(img)
        return color_coords

    def image_adjustment(self, img):
        """Resize the image to fit within the max dimensions."""
        max_width = 600
        max_height = 600

        original_width, original_height = img.width, img.height
        scale_factor = min(max_width / original_width, max_height / original_height, 1.0)

        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)

        # Resize the image with high-quality resampling
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return resized_img

    def extract_colors(self, img):
        """Extract and classify the colors from the image."""
        color_map = {
            "White": (255, 255, 255),
            "Light Gray": (193, 193, 193),
            "Red": (239, 19, 11),
            "Orange": (255, 113, 0),
            "Yellow": (255, 228, 0),
            "Green": (0, 204, 0),
            "Light Green": (0, 255, 145),
            "Light Blue": (0, 178, 255),
            "Blue": (35, 31, 211),
            "Purple": (163, 0, 186),
            "Pink": (223, 105, 167),
            "Peach": (255, 172, 142),
            "Brown": (160, 82, 45),
            "Black": (0, 0, 0),
            "Dark Gray": (80, 80, 80),
            "Dark Red": (116, 11, 7),
            "Dark Orange": (194, 56, 0),
            "Gold": (232, 162, 0),
            "Forest Green": (0, 70, 25),
            "Teal": (0, 120, 93),
            "Navy Blue": (0, 86, 158),
            "Dark Blue": (14, 8, 101),
            "Magenta": (85, 0, 105),
            "Violet": (135, 53, 84),
            "Copper": (204, 119, 77),
            "Mahogany": (99, 48, 13)
        }

        def euclidean_distance(c1, c2):
            """Calculate the Euclidean distance between two RGB colors."""
            return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

        def classify_color(r, g, b):
            """Classify the input RGB color by finding the closest match."""
            input_color = (r, g, b)
            closest_color = min(color_map.items(), key=lambda item: euclidean_distance(item[1], input_color))
            return closest_color[0]

        color_coords = {color: [] for color in color_map}

        # Iterate through the pixels of the image
        for x in range(0, img.width, 3):  # You can adjust the step (3) for pixel skipping
            for y in range(0, img.height, 3):
                r, g, b = img.getpixel((x, y))
                color_name = classify_color(r, g, b)
                color_coords[color_name].append((x, y))

        return color_coords



