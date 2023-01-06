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

window.mainloop()