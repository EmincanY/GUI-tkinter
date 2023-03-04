"""
    1-50 arası 5 adet rastgele sayı üretip göster adındaki butona tıklandığında label'a yazdırsın değeleri.
    Saydamlaştır adındaki butona tıklandığında  penceremiz saydamlaşsın. / eski haline döndürmek için Döndür butonu bulunsun.
    Max yap, Min yap butonları ile de pencereyi tam ekran yapıp küçültebilelim.
"""

import tkinter as tk

form = tk.Tk()

form.title('UYGULAMA')
form.geometry("500x450+350+300")


label = tk.Label(form, fg = 'yellow' , bg='blue' ,height=10,width=30)
label.pack()


def show():
    import random
    label.config(text= random.choices(range(1,50), k = 5) , fg='red' , font='Times 10')  # random.sample'da aynı mantık. # label.config yaparak, labeldaki düzenlemeleri yapıyoruz.

def saydamlastır():
    form.wm_attributes('-alpha', 0.5)

def geriDöndür():
    form.wm_attributes('-alpha', 1)

def maxYap():
    form.state('zoomed')

def minYap():
    form.state('iconic')
    
    
show_button = tk.Button(form, text="Random 5 sayı",fg = 'black', bg = 'yellow', command=show)
show_button.pack(side=tk.LEFT, padx=5)
trans_button = tk.Button(form, text="Saydamlastır",command=saydamlastır)
trans_button.pack(side=tk.LEFT, padx=5)
back_button = tk.Button(form, text="Geri döndür",command=geriDöndür)
back_button.pack(side=tk.LEFT, padx=5)
max_button = tk.Button(form, text="Max Yap",command=maxYap)
max_button.pack(side=tk.LEFT, padx=5)
min_button = tk.Button(form, text="Min Yap",command=minYap)
min_button.pack(side=tk.LEFT, padx=5)



form.mainloop()