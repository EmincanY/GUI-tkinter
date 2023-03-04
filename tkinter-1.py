import tkinter as tk

form = tk.Tk() # Create form-window
form.title("Tkinter dersleri 1") # Ana başlık
etiket = tk.Label(text = 'Tkinter Python') # Etiketimiz
etiket.pack() # Etiketi de ekranda görebilmemiz için packlememiz gerekiyor. Bütün araçları pack etmeliyiz.
etiket2 = tk.Label(form, text="Python Tkinter Dersleri")
etiket2.pack()


form.mainloop() # Bizim ekranımızda da görünmesi için