import tkinter as tk

form = tk.Tk()

form.title("Tkinter Ders3")
# form.geometry("500x250") # Yatayda 500 Dikeyde 250 boyutlarında gelsin.
form.geometry("500x250+500+350") # Yatayda 500 Dikeyde 250 boyutlarında gelsin. + işaretiyle ilk açıldığı konumları belirtiyoruz.
# form.minsize(450,400) # X'i en az 450 , Y'si en az 400
# form.maxsize(550,550) # X'i en çok 550 , Y'si en çok 550
form.resizable(False , False) # Boyutlarımın x ekseniyle de y ekseniyle de oynanamasın.
 
label = tk.Label(form, text='Ders3')
label.pack()













form.mainloop()