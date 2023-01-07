import tkinter as tk


window = tk.Tk()
window.geometry("1000x600")
window.title("My GUI interface")
label = tk.Label(window,text = "My GUI", font = ("Vedrana", 24))
label.pack(padx=35, pady=35)

textbox = tk.Text(window, font=('Times New Roman', 30), height = 5)
textbox.pack(padx=40, pady=40)

button = tk.Button(window, text = "Log in", font = ('Vedrana', 14))
button.pack()

bframe = tk.Frame(window)
bframe.columnconfigure(0, weight=1)
bframe.columnconfigure(1, weight=1)

button1 = tk.Button(bframe, text = "Przycisk 1", font =("Vedrana", 14))
button1.grid(row = 0, column = 0)
button2 = tk.Button(bframe, text = "Przycisk 2", font =("Vedrana", 14))
button2.grid(row = 0, column = 1)
button3 = tk.Button(bframe, text = "Przycisk 3", font =("Vedrana", 14))
button3.grid(row = 1, column = 0)
button3 = tk.Button(bframe, text = "Przycisk 4", font =("Vedrana", 14))
button3.grid(row = 1, column = 1)

bframe.pack()

window.mainloop()
