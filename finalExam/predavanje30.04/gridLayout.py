import tkinter as tk

from tkinter import messagebox

prozor = tk.Tk()



prozor.title("Primjer za grid")

prozor.geometry("400x200")



tk.Label(prozor, text="Ime", font=("Arial", 12)).grid(row=0, column=0, padx=(12, 8), pady=8)

polje_ime = tk.Entry(prozor, font=("Arial", 12))

polje_ime.grid(row=0, column=1, padx=(0, 12), pady=8)



tk.Label(prozor, text="Grad", font=("Arial", 12)).grid(row=1, column=0, padx=(12,8), pady=8)

polje_grad = tk.Entry(prozor, font=("Arial",12))

polje_grad.grid(row=1, column=1, padx=(0, 12), pady=8)



def prikazi():

    ime=polje_ime.get().strip()

    grad =polje_grad.get().strip()



    if len(ime) > 0 and len(grad)>0:

        messagebox.showinfo("Poruka","Zdravo "+ime+" iz "+grad)

    else:

         messagebox.showerror("Poruka","Morate unijeti sve podatke")

    

    #rezultat.config(text="Zdravo "+ime+" iz "+grad)



tk.Button(prozor, text="Prikazi", font=("Arial", 12), command=prikazi).grid(row=2, column=0, columnspan=2, pady=15)



rezultat=tk.Label(prozor, text="",font=("Arial", 12))

rezultat.grid(row=3,column=0,columnspan=2)

prozor.mainloop()
