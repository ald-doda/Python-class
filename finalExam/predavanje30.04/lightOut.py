import tkinter as tk



prozor = tk.Tk()

prozor.title("Prekidac")

prozor.geometry("300x300")



image1=tk.PhotoImage(file="light_off.png")

image2=tk.PhotoImage(file="light_on.png")



is_on=False



def promijeni():

    global is_on

    if is_on:

        dugme.config(image=image1, text="Turn on")

    else:

        dugme.config(image=image2, text="Turn off")

        is_on=True



dugme = tk.Button(prozor, text="turn on", image=image1, command=promijeni)

dugme.pack(pady=50)

prozor.mainloop()
