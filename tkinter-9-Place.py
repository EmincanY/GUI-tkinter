# Place methodu da aynı pack gibi fakat tam olarak istediğimiz koordinatta yerleştirebiliyoruz pack ile.

import tkinter as tk

form = tk.Tk()

form.title('Ders9-Place')
form.geometry('500x400+350+300')

button = tk.Button(form, text='Deneme' , fg='red', bg='green', font='Times 17 bold')
# button.place(x = 150 , y= 140) # Spesifik olarak (150,140) koordinatlarında oluştur benim buttonumu.
# button.place(relx= 0.5 , rely=0.5) # Hareketli olmasını sağlamak için relx ve rely parametreleri kullanılır. Yüzdesel olarak değerler alır bu parametreler.
button.place(width=150 , height=160)







form.mainloop()