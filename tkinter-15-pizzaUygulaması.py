import tkinter as tk

form = tk.Tk()

form.title('Pizza Sipariş Programı')
form.geometry('500x500+400+100')

baslik_label = tk.Label(form, text="Pizza Sipariş Programına Hoşgeldiniz", bg="yellow" , fg='red', font='Times 20 italic').pack()


ad_label = tk.Label(form, text='Ad Soyad :' , bg='pink', font='Times 12 italic').place(x=10 , y=45)
boyut_label = tk.Label(form, text='Boyut :' , bg='pink', font='Times 12 italic').place(x=10 , y=75)
icindekiler_label = tk.Label(form, text='İçindekiler :' , bg='pink', font='Times 12 italic').place(x=10 , y=105)
adres_label = tk.Label(form, text='Adres :' , bg='pink' , font = 'Times 12 italic').place(x= 10 , y= 135 )


ad_entry_value = tk.StringVar()
adres_entry_value = tk.StringVar()
ad_entry = tk.Entry(form, textvariable= ad_entry_value).place(x=100 , y=45)
adres_entry = tk.Entry(form, textvariable= adres_entry_value).place(x=100 , y = 135)

boyut_x = tk.StringVar()
boyut_rd_button_kücük = tk.Radiobutton(form, text= 'Kücük' , activebackground= 'green', variable= boyut_x, value='Küçük Boy').place(x=100 , y=75)
boyut_rd_button_orta = tk.Radiobutton(form, text= 'Orta' , activebackground= 'green', variable= boyut_x , value='Orta Boy').place(x=160 , y=75)
boyut_rd_button_büyük = tk.Radiobutton(form, text= 'Büyük' , activebackground= 'green', variable= boyut_x, value='Büyük Boy').place(x=220 , y=75)



x1 = tk.StringVar() # Checkbuttonların bize str değer döndürmesini istiyoruz.
x2 = tk.StringVar()
x3 = tk.StringVar()

check1 = tk.Checkbutton(form, text= 'Sucuklu' , activebackground= 'green', variable=x1 , onvalue= 'Sucuklu' ).place(x=100 , y=105)
check2 = tk.Checkbutton(form, text= 'Etli' , activebackground= 'green', variable=x2 , onvalue= 'Etli' ).place(x=175 , y=105)
check3 = tk.Checkbutton(form, text= 'Mantarlı' , activebackground= 'green', variable=x3 , onvalue= 'Mantarlı' ).place(x=250 , y=105)


def siparisVer():
    bilgi_label = tk.Label(form, text= "Sipariş Bilgileri",bg= 'green' , font= 'Times 15 italic').place(x = 120 , y= 200) 
    ad_label = tk.Label(form, text='Ad Soyad :' , bg='pink', font='Times 12 italic').place(x=10 , y=230)
    boyut_label = tk.Label(form, text='Boyut :' , bg='pink', font='Times 12 italic').place(x=10 , y=260)
    icindekiler_label = tk.Label(form, text='İçindekiler :' , bg='pink', font='Times 12 italic').place(x=10 , y=290)
    adres_label = tk.Label(form, text='Adres :' , bg='pink' , font = 'Times 12 italic').place(x= 10 , y= 320 )
    
    ad_label_text = tk.Label(form, text=adres_entry_value.get() , bg='red', font='Times 12 italic').place(x=100 , y=230)
    boyut_label_text = tk.Label(form, text=boyut_x.get() , bg='red', font='Times 12 italic').place(x=100 , y=260)
    icindekiler_label_text = tk.Label(form, text= x1.get()+' '+x2.get()+' '+x3.get() , bg='red', font='Times 12 italic').place(x=100 , y=290)
    adres_label_text = tk.Label(form, text=adres_entry_value.get() , bg='red' , font = 'Times 12 italic').place(x= 100 , y= 320 )

def iptalVer():
    form.quit()
    

siparis_button = tk.Button(form, text= 'Sipariş ver' , activebackground='green' , command= siparisVer).place(x = 100 , y= 160)
iptal_button = tk.Button(form, text='İptal et', activebackground='green' , command= iptalVer).place(x = 200 , y= 160)












form.mainloop()

