import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40,"bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24,"bold")
DEFAULT_FONT_STYLE = ( "Arial",20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF#"
LIGHT_BLUE ="#CCEDFF"
LIGHT_GRAY  =  "#F5F5F5"
LABEL_COLOR =  "#25265E"

class Calculator:
    def __init__(self):
        self.windows = tk.Tk() #создание окна
        self.windows.geometry ("350x650") #размер появляемого окна
        self.windows.resizable(False, False) #отключение параметра изменения размера окна
        self.windows.title("Calculator_test") #отображается в шапке имя программы

    def start(self):
        self.windows.mainloop() #обработчик событий для ожидания действий пользователя
        
if __name__ == "__main__":
    vizov = Calculator()
    vizov.start()