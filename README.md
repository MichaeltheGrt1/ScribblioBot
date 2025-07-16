# ScribblioBot
Recreates an image in-game from an image file put in the img folder
Link to project: https://github.com/MichaeltheGrt1/ScribblioBot
<img width="1916" height="1076" alt="image" src="https://github.com/user-attachments/assets/6342f29d-fade-4a26-a1ef-5bb5313b4db5" />

## How it was Made
I made this program in my free time. The dimensions that it was made for is solely based on my laptop screen size (1920x1080px) and is not a reflection of my best effort in coding or readability.
Nontheless, I thought my program was pretty cool and decided to upload it. The program starts by verifying an image is present, formatting an image, collecting every fourth pixel rgb value and storing it in a color map, euclidean colors are then used to find the color cooresponding to the pallet given in game, finally key presses are simulatted using pyautogui to recreate the image.

## How to Use
To run the program place a downloaded image in the images folder, press the play button then navigate back to your scribblio screen (full-screen), then finally press "`". Make sure to run from main!!!
To change the click speed change the time.sleep value in the click_handler.py file.
