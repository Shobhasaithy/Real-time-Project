import tkinter as tk

def change_colors():
    label.config(bg="blue", fg="white")
    button.config(bg="green", fg="white")

# Create the main window
window = tk.Tk()
window.geometry("300x200")
window.title("Color Test")

# Create a label and a button
label = tk.Label(window, text="Hello, World!", font=("Arial", 24), bg="white", fg="black")
label.pack(pady=20)

button = tk.Button(window, text="Change Colors", command=change_colors, bg="gray", fg="black")
button.pack()

# Run the tkinter main loop
window.mainloop()
