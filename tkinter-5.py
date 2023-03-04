import tkinter as tk

form = tk.Tk()

form.title('Ders5')
form.geometry('500x400+300+250')

def topla(a,b):
    return a+b

button = tk.Button(form, text="Tıkla", fg='Black',bg='red', command=topla) # Buton oluşturduk. Butona tıklanınca command'ın içinde yazdığımız fonksiyon çalışacak.
button.pack(side= tk.LEFT) # side parametresi ile buttonumuzun form içindeki konumunu belirleyebiliyoruz.
button2 = tk.Button(form, text="Tıkla2", command=topla)
button2.pack(side=tk.RIGHT)










form.mainloop()