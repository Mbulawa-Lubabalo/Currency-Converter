from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Currrency Converter")

icon = PhotoImage(file='IconImage\currencyIcon.png')
window.iconphoto(True,icon)
window.config(background="#c1c4c7")

header = Label(window, 
               text="Currency Converter", 
               background="#c1c4c7", 
               font=("Arial", 16)
               ).grid(row=0, column=0, columnspan=2, pady=10)
# header.place(x=0, y=0)

# Input Fields
fromCurrency_label = Label(window, text="From:")
fromCurrency_label.grid(row=1, column=0, padx=10, pady=5)
# fromCurrency_entry = Entry(window)
currencies = ["USD", "EUR", "GBP", "INR", "AUD"]
defaultOption = StringVar(value="USD")
fromCurrency_menu = OptionMenu(window, defaultOption, *currencies)
fromCurrency_menu.grid(row=2, column=0, padx=10, pady=5)

toCurrency_label = Label(window, text="To:")
toCurrency_label.grid(row=1, column=1, columnspan=2, pady=5)
toCurrency_entry = OptionMenu(window, defaultOption, *currencies)
toCurrency_entry.grid(row=2, column=1, columnspan=2, pady=5)

# Amount
amount_label = Label(window, text="Amount:").grid(row=3, column=0, columnspan=2, pady=5)
amount_entry = Entry(window).grid(row=4, column=0, columnspan=2, pady=5)

# convertedValue_label = Label(window, text="converted", background="#ffffff").grid(row=6)

# Convert button
convertButton = Button(window, 
                       text="Convert", 
                       ).grid(row=5, column=0, columnspan=2, pady=10)

# Result Label
result_label = Label(window, 
                     text="Converted Amount: ", 
                     background="#ffffff"
                     ).grid(row=6, column=0, columnspan=2, pady=10)



window.mainloop()