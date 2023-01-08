import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Hello, Hi!", font = ("Vedrana", 20))
        self.label.pack(padx = 30, pady = 50)
        self.textbox = tk.Textbox()
        self.root.mainloop()