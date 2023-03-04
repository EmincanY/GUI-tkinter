# Email ve şifre giriş yeri altında Kaydol ve Giriş Buttonları
# Kaydol butonuna tıklarsa altta ad-email-sifre isteyen yeni bir kaydolma yeri açılacak

import tkinter as tk

form = tk.Tk()
form.title('Giriş Uygulaması')
form.geometry("500x400+300+250")

mail = tk.Label(form, text="E-mail", fg= 'black' , bg= 'red', font='Times 10 bold')
mail.place(x=10 , y = 30)
passw = tk.Label(form, text="Sifre", fg= 'black' , bg= 'red', font='Times 10 bold')
passw.place(x=10 , y = 60)


email_entry = tk.Entry()
email_entry.place(x = 60 , y = 30)
passw_entry = tk.Entry(show='*')
passw_entry.place(x = 60 , y = 60)





def kayıtOl():
    add_kayıt = tk.Label(form, text='Ad:', fg= 'green' , bg= 'red', font='Times 10 bold' )
    add_kayıt.place(x=10 , y = 120)
    mail_kayıt = tk.Label(form, text="E-mail", fg= 'green' , bg= 'red', font='Times 10 bold')
    mail_kayıt.place(x=10 , y = 150)
    passw_kayıt = tk.Label(form, text="Sifre", fg= 'green' , bg= 'red', font='Times 10 bold')
    passw_kayıt.place(x=10 , y = 180)


    ad_kayıt_entry = tk.Entry()
    ad_kayıt_entry.place(x = 60 , y = 120)
    email_kayıt_entry = tk.Entry()
    email_kayıt_entry.place(x = 60 , y = 150)
    passw_kayıt_entry = tk.Entry()
    passw_kayıt_entry.place(x = 60 , y = 180)
    
    kayıt_button = tk.Button(form, text='Kayıt olmak için tıkla !' , command=kayıtOlunduMessage)
    kayıt_button.place(x = 60 , y = 210)
    
    
def kayıtOlunduMessage(): 
    kayıtOlunduLabel = tk.Label(form, text = 'Başarıyla kayıt olundu')
    kayıtOlunduLabel.place(x = 60, y = 250)
    
    
    
    
def girisYap():
    email_entry.delete(0,'end')
    passw_entry.delete(0,'end')


kaydol_button = tk.Button(form, text="Kayıt Ol",command= kayıtOl , fg = 'green' , bg ='yellow')
giris_button = tk.Button(form, text="Giris Yap",command= girisYap , fg = 'red' , bg ='yellow')
kaydol_button.place(x = 60 , y = 90 )
giris_button.place(x = 120 , y = 90 )



form.mainloop()