import pyautogui as pg
import time

def click(color_coords):
    beg_x, beg_y = 427, 292
    pg.PAUSE = 0  # Zero delay

    try:
        # Click the colors with small intervals to avoid issues
        def click_color(color, x_offset, y_offset):
            pg.click(x_offset, y_offset)
            time.sleep(0.1)  # Small delay to ensure actions register
            for (x, y) in color_coords[color]:
                pg.click(beg_x + x, beg_y + y)
                pg.mouseDown()
                time.sleep(.0001)
                pg.mouseUp()
                time.sleep(0.0001)  # Slight delay between clicks

        # Process the different colors
        click_color("Black", 470, 1055)
        click_color("Dark Blue", 714, 1055)
        click_color("Dark Red", 531, 1055)
        click_color("Dark Orange", 561, 1055)
        click_color("Dark Gray", 500, 1055)
        click_color("Brown", 833, 1031)
        click_color("Mahogany", 833, 1055)
        click_color("Forest Green", 624, 1055)
        click_color("Navy Blue", 686, 1055)
        click_color("Teal", 654, 1055)
        click_color("Gold", 591, 1055)
        click_color("Copper", 800, 1055)
        click_color("Purple", 738, 1031)
        click_color("Magenta", 743, 1055)
        click_color("Violet", 772, 1055)
        click_color("Blue", 711, 1031)
        click_color("Green", 622, 1031)
        click_color("Light Blue", 680, 1031)
        click_color("Light Green", 652, 1031)
        click_color("Yellow", 591, 1031)
        click_color("Orange", 564, 1031)
        click_color("Pink", 768, 1031)
        click_color("Peach", 803, 1031)
        click_color("Light Gray", 504, 1031)

    finally:
        print("Finished")

