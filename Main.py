from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Currrency Converter")

icon = PhotoImage(file='IconImage\currencyIcon.png')
window.iconphoto(True,icon)
window.config(background="#c1c4c7")

header = Label(window, 
               text="Currency Converter", 
               background="#c1c4c7").grid(row=0, column=0)
# header.place(x=0, y=0)

# Input Fields
fromCurrency_label = Label(window, text="From:")
fromCurrency_label.grid(row=2, column=0)
# fromCurrency_entry = Entry(window)
currencies = ["USD", "EUR", "GBP", "INR", "AUD"]
defaultOption = StringVar(value="USD")
fromCurrency_entry = OptionMenu(window, defaultOption, *currencies)
fromCurrency_entry.grid(row=3, column=0)

toCurrency_label = Label(window, text="To:")
toCurrency_label.grid(row=2, column=1)
toCurrency_entry = OptionMenu(window, defaultOption, *currencies)
toCurrency_entry.grid(row=3, column=1)

# Amount
amount_label = Label(window, text="Amount:").grid(row=4)
amount_entry = Entry(window).grid(row=5)

# Convert button
convertButton = Button(window, text="Convert").grid(row=6)



window.mainloop()