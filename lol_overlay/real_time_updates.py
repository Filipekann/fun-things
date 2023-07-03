import tkinter as tk
import threading

def update_overlay():
    # Update the insights with new data
    insights = get_realtime_insights()  # Replace this with your function to retrieve real-time data

    # Update the label text with the new insights
    insights_label.config(text=insights)

    # Schedule the next update after a delay (e.g., 5 seconds)
    window.after(5000, update_overlay)

def create_overlay():
    # Create a Tkinter window
    window = tk.Tk()

    # Create a label to display the insights
    insights_label = tk.Label(window, text="", font=('Arial', 16))

    # Pack the label to add it to the window
    insights_label.pack()

    # Customize the window appearance
    window.title('League of Legends Overlay')
    window.attributes('-topmost', True)
    window.configure(bg='white')

    # Set the window size and position
    window.geometry('400x200+100+100')

    # Schedule the initial update after a short delay (e.g., 1 second)
    window.after(1000, update_overlay)

    # Run the Tkinter event loop
    window.mainloop()

# Example function to retrieve real-time insights
def get_realtime_insights():
    # Simulate getting real-time data
    insights = "Real-time insights:\n\n- Player stats\n- Team performance\n- Game events"

    return insights

# Start the overlay creation
create_overlay()
