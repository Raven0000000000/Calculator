from tkinter import *
windows = Tk()     # создаем корневой объект - окно
windows.title("Calculator")     # устанавливаем заголовок окна
windows.geometry("500x650")    # устанавливаем размеры окна

label_out = Label(
    text = "0",
    font=("Arial", 44),
    fg="black",
    bg="snow3"
)
label_out.pack(anchor=N, padx=5,pady=5, side=RIGHT)

windows.mainloop()