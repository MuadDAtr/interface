import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Hello, Hi!", font = ("Vedrana", 20))
        self.label.pack(padx = 30, pady = 50)
        self.textbox = tk.Textbox(self.root, font = ('Times New Roman', 13))
        self.textbox.pack(padx = 20, pady = 10)

        self.ch_status = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text = "Testing", font = ('Arial', 17), variable = self.ch_status)
        self.check.pack(padx = 20, pady = 20)


        self.root.mainloop()