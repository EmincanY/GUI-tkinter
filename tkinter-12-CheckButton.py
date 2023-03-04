import tkinter as tk


form = tk.Tk()

form.title('CheckButton')
form.geometry("500x500+300+250")


x = tk.IntVar()
x.set(0)

def kontrol():
    if x.get() == 0:
        print('Onaylanmadı')
    else:
        print('Onaylandı')

check = tk.Checkbutton(form, text="Onay butonu", fg ='pink', bg='green', variable= x, command= kontrol)
check.pack()










form.mainloop()