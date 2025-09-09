import tkinter as tk

def say_hello():
    label.config(text="Hello, " + entry.get() + "!")

# Create main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150")

# Add label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Add entry field
entry = tk.Entry(root)
entry.pack(pady=5)

# Add button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=5)

# Run the application
root.mainloop()
