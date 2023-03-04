"""
    side - left-right-top-bottom
    fill - x-y
    expand - 0-1
    anchor - "n" yukarı "s" aşağı "e" sağ "w" sol "ne" yukarıSağ "nw" yukarıSol "sw" asagıSol "center" orta
"""
    
import tkinter as tk

form = tk.Tk()

form.title('Ders-8')
form.geometry('500x400+350+300')

label = tk.Label(form, text='Geometrik Yöneticiler')
label.pack(side=tk.TOP)
button = tk.Button(form, text="Pack()" , bg='red')
button.pack(side=tk.BOTTOM , fill=tk.X , expand= tk.YES ) # X ekseninde doldurdu button'un pack'ini. # Y ekseninde doldurmak için sideımız tk.LEFT ya da tk.RIGHT olmalı.
deneme_button = tk.Button(form, text='Deneme Butonu')
deneme_button.pack(expand=1 , anchor='ne' , padx=20 , pady=100)

deneme_button2 = tk.Button(form, text='Deneme Butonu2' , bg='green')
deneme_button2.pack(ipadx=50 , ipady=80)










form.mainloop()