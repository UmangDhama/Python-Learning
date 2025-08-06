from tkinter import *

def button_clicked():
    new_text=float(entry.get())
    new_text= new_text * 1.60934
    km_dis.config(text=new_text)

in_kn=0
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

entry=Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles=Label(window, text="Miles")
miles.grid(column=2, row=0)


my_label = Label(window, text="is equal to",)
my_label.grid(column=0, row=1)

km_dis=Label(window, text=in_kn)
km_dis.grid(column=1, row=1)

km=Label(window, text="Km")
km.grid(column=2, row=1)

button=Button(window,text="Calculate ",command=button_clicked)
button.grid(column=1, row=2)










window.mainloop()