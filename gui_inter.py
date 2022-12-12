import tkinter as tk


window = tk.Tk()
window.geometry("1000x600")
window.title("My GUI interface")
label = tk.Label(window,text = "My GUI", font = ("Times New Roman", 24))
label.pack()
window.mainloop()