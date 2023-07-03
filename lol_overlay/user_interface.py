import pygetwindow as gw
import pyautogui
import cv2
import numpy as np

def capture_game_window():
    # Find the League of Legends game window by its title
    game_window = gw.getWindowsWithTitle('League of Legends')[0]

    # Activate the game window and bring it to the front
    game_window.activate()

    # Get the position and size of the game window
    window_x, window_y, window_width, window_height = game_window.left, game_window.top, game_window.width, game_window.height

    # Capture the game window using pyautogui
    screenshot = pyautogui.screenshot(region=(window_x, window_y, window_width, window_height))

    # Convert the screenshot to an OpenCV image format
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Display the captured game window image
    cv2.imshow('League of Legends Game Window', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
capture_game_window()
