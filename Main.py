from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Currrency Converter")

icon = PhotoImage(file='IconImage\currencyIcon.png')
window.iconphoto(True,icon)
window.config(background="#c1c4c7")

header = Label(window, 
               text="Currency Converter", 
               background="#c1c4c7")
header.place(x=0, y=0)


window.mainloop()