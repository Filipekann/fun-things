import tkinter as tk

def create_overlay(insights):
    # Create a Tkinter window
    window = tk.Tk()

    # Create a label to display the insights
    insights_label = tk.Label(window, text=insights, font=('Arial', 16))

    # Pack the label to add it to the window
    insights_label.pack()

    # Customize the window appearance
    window.title('League of Legends Overlay')
    window.attributes('-topmost', True)
    window.attributes('-transparentcolor', 'white')
    window.configure(bg='white')

    # Set the window size and position
    window.geometry('400x200+100+100')

    # Run the Tkinter event loop
    window.mainloop()

# Example insights
insights = "Here are some insights:\n\n- Champion win rates\n- Itemization trends\n- Map control analysis\n- Team performance metrics"

# Example usage
create_overlay(insights)
