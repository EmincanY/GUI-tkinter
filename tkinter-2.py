import tkinter as tk

form = tk.Tk()
form.title('Tkinter Dersleri Formu')

label = tk.Label(form, text='Python Tkinter')
label.pack()
label2 = tk.Label(form, text='Ders2', fg='red')
label2.pack()
label3 = tk.Label(form, text="Ders2 arkaplan" , fg='black' , bg="green")
label3.pack()
label4 = tk.Label(form, text="Yeni Label" , fg="blue" , bg='green' , font="Times 15 italic")
label4.pack()
label5 = tk.Label(form, text="En son label" , fg="green" , bg = 'red',
                   font='Times 17 bold')
label5.pack()

form.mainloop()