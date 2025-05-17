from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

#Label 1
label_1 = Label(text="is equal to")
label_1.grid(column=1, row=2)

#Label 2
label_miles = Label(text="Miles")
label_miles.grid(column=3, row=1)

label_km = Label(text="Km")
label_km.grid(column=3, row=2)

#Entry mile
entry_mile = Entry(width=10)
entry_mile.insert(END, string="0")
entry_mile.grid(column=2, row=1)


#Label
result = Label(text=0)
result.grid(column=2, row=2)

#Button
def action():
    res = float(entry_mile.get()) * 1.609
    result.config(text=res)

calculate_button = Button(text="Calculate", command=action)
calculate_button.grid(column=2, row=3)
window.mainloop()