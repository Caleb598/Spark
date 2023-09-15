import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("Spark Demo")
window.geometry("1200x800")

# Create a label widget
label = tk.Label(window, text="Spark!")
label.pack(pady=20)

# Create a button widget
button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack()

# Run the main loop of the window
window.mainloop()
