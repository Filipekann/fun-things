import pygetwindow as gw
import tkinter as tk
import cv2
import numpy as np
import threading
import pyautogui

def capture_game_window():
    # Find the League of Legends game window by its title
    game_window = gw.getWindowsWithTitle('League of Legends')[0]

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

def create_overlay():
    # Create a Tkinter window
    window = tk.Tk()

    # Add your overlay content and widgets here
    # Example: Insights labels, statistics, timers, etc.

    # Customize the window appearance
    window.title('League of Legends Overlay')
    window.attributes('-topmost', True)
    window.attributes('-transparentcolor', 'white')
    window.configure(bg='white')

    # Set the window size and position
    window.geometry('400x200+100+100')

    # Run the Tkinter event loop
    window.mainloop()

# Create threads for capturing the game window and creating the overlay
capture_thread = threading.Thread(target=capture_game_window)
overlay_thread = threading.Thread(target=create_overlay)

# Start the threads
capture_thread.start()
overlay_thread.start()
