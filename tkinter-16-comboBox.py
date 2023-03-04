import tkinter as tk
from tkinter.ttk import Combobox

form = tk.Tk()
form.title('ComboBox')
form.geometry("500x500")



x = tk.StringVar()
kutu = Combobox(form, values= ('1','2',"3","4","5","6"), height=3, textvariable=x).pack()

def yazdır():
    print(x.get())

button = tk.Button(form, text='Yazdır', command=yazdır).pack()








form.mainloop()