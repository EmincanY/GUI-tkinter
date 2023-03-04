import tkinter as tk


form = tk.Tk()
form.title('RadioButton')
form.geometry("500x500+350+300")


def kontrol():
    if x.get() == '1' :
        print('Buton 1')
    elif x.get() == '2':
        print('Buton 2')
    else:
        print('Buton 1 ve 2')


button = tk.Button(form, text='Tıkla' , fg= 'black' , bg= 'red' , activebackground= 'green', command= kontrol)
button.pack()


x= tk.StringVar()
x.set(0)

radio_button = tk.Radiobutton(form, text = 'radio1' , activebackground='red' , value = 1, variable=x)
radio_button.pack()

radio_button2 = tk.Radiobutton(form, text = 'radio2' , activebackground='green' , value = 2, variable=x)
radio_button2.pack()








form.mainloop()







