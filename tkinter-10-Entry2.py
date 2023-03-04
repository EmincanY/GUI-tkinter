import tkinter as tk

form = tk.Tk()

form.title("'Ders10-Entry2")
form.geometry("500x400+300+200")

entry = tk.Entry(form)
entry.pack()


def veriAl():
    etiket['text'] = entry.get()

def veriSil():
    entry.delete(0,'end') # first-last parametreleri. En baştan en sona demiş olduk.
    entry2.delete(0,'end')
    
entry2 = tk.Entry(form,show='*' ) # show parametresi ile verileri gizli bir şekilde alabiliyoruz. Şifre vb. bilgiler alınırken iyi
entry2.pack()

verial_button = tk.Button(form , text='Verileri al' , fg='red' , bg= 'green' , command=veriAl)  
verial_button.pack()  

verisil_button = tk.Button(form , text='Verileri sil' , fg='red' , bg= 'green' , command=veriSil)  
verisil_button.pack()  


etiket = tk.Label(text= 'Veriler Burada görünecek !')
etiket.pack()









form.mainloop()