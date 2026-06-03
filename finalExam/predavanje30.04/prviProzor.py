#pip install tkinter

import tkinter as tk



prozor = tk.Tk()



prozor.title("Moj prvi prozor")



prozor.geometry("400x200")



labela = tk.Label(prozor, text="Klikni dugme ispod.", font=("Arial", 14))

labela.pack(pady=20)





def klik_na_dugme():

    labela.config(text = "Bravo dugme radi.")



dugme = tk.Button(prozor, text="Klikni ovdje", font = ("Arial", 12), command=klik_na_dugme)

dugme.pack()



prozor.mainloop()
