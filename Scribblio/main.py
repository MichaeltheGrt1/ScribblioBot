from pynput import keyboard
from image_analyzer import ImageAnalyzer  # Assuming image_analyzer is a module containing the ImageAnalyzer class
import click_handler  # Assuming click_handler is a module

def on_press(key):
    """Detect backtick key press to start the program."""
    try:
        if key == keyboard.KeyCode.from_char('`'):  # Check if the backtick is pressed
            return False  # Stops the listener (to start the program)
    except AttributeError:
        pass


def main():
    # Create a listener to detect key press
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    listener.join()  # Wait for the key press to stop the listener

    # Create an instance of the ImageAnalyzer class
    analyzer = ImageAnalyzer(path="./images")

    # Check if the image folder contains images
    if not analyzer.image_validity():
        print("No images found in the folder.")
        return  # Stop the execution if no image is found

    # Analyze the image and get the color coordinates
    pixel_color = analyzer.image_analyzer()  # Image analysis

    # If the image analysis succeeded, perform the click based on the color data
    if pixel_color:
        click_handler.click(pixel_color)  # Perform the click based on the analyzed data
    else:
        print("Color extraction failed.")


if __name__ == "__main__":
    main()
