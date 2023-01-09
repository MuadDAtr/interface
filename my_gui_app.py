import tkinter as tk


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Hello, Hi!", font = ("Vedrana", 20))
        self.label.pack(padx = 30, pady = 50)
        self.textbox = tk.Text(self.root, height = 6, font = ('Times New Roman', 13))
        self.textbox.pack(padx = 20, pady = 10)

        self.ch_status = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text = "Testing", font = ('Arial', 17), variable = self.ch_status)
        self.check.pack(padx = 20, pady = 20)

        self.button = tk.Button(self.root, text = "I love you", font = ('Baskerville', 24), command = self.test_it)
        self.button.pack(padx = 20, pady = 10)

        self.root.mainloop()
    
    def test_it(self):
        if self.ch_status.get() == 0:
            print(self.textbox.get('1.0', tk.END))

MyGUI()