import tkinter as tk

form = tk.Tk()

form.geometry('500x500+350+250')
form.title('Ders4')

# form.state('normal') # İLk çalıştırılmada hangi boyutlarda geleceğini belirliyoruz. normal= normal boyutlar , zoomed= Tam ekran , iconic= En altta pencere olarak getirtmek
form.wm_attributes('-alpha', 0.3) # Saydamlık ayarlama. 1 = Normal durum. 0.5 = Yarı saydam.









form.mainloop()