import tkinter as tk
from tkinter import messagebox

form = tk.Tk()
form.title('MessageBoxes')
form.geometry("500x500+350+300")


def message():
    messagebox.showinfo(title = 'Mesaj1' , message= 'Lütfen mesaja riayet edelim!')
    messagebox.askretrycancel(title= 'Mesaj2' , message= "Lütfen et artık!") # Yeniden dene ve iptal geliyor
    messagebox.askyesno(title= 'Mesaj3' , message= "artık!") # Evet Hayır geliyor mesajdan sonra
    messagebox.askquestion(title='Mesaj4' , message='tkinter Messagebox son') # Soru işareti imleciyle birlikte geliyor.

message_buton = tk.Button(form, text="Tıkla Mesaj Gelsin", command= message).pack()
# warning_button = tk.Button(form, text='Tıkla Uyarı Gelsin')



form.mainloop()