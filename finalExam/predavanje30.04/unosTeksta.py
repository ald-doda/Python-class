import tkinter as tk



prozor = tk.Tk()

prozor.title("Unos teksta")

prozor.geometry("400x250")



tk.Label(prozor, text="Kako se zoves", font=("Arial", 12)).pack(pady=10)



polje = tk.Entry(prozor, font=("Arial", 14), width=25)

polje.pack(pady=5)



poruka = tk.Label(prozor, text="", font=("Arial", 12))

poruka.pack(pady=10)



def pozdravi():

    ime = polje.get().strip()

    if len(ime) > 0:

        poruka.config(text="Zdravo"+ ime + "!")

    else:

        poruka.config(text="Upisi ime pa klikni dugme.")



tk.Button(prozor, text="Posalji", font=("Arial", 12), command=pozdravi).pack()



prozor.mainloop()
