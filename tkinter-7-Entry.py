import tkinter as tk

form = tk.Tk()

form.title('Ders7-Entry')
form.geometry('500x400+350+300')


giris = tk.Entry(form, fg='black',bg='green')
giris.pack()
giris2 = tk.Entry(form, fg="red", bg='blue')
giris2.pack(side = tk.LEFT)











form.mainloop()