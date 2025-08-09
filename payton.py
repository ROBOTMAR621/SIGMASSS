import tkinter as tk
import random


def mover_boton():

    nueva_x = random.randint(0, 500) 
    nueva_y = random.randint(0, 300)  

  
    boton.place(x=nueva_x, y=nueva_y)


ventana = tk.Tk()
ventana.title("el boton mas pro ")


ventana.geometry("600x400") 


boton = tk.Button(ventana, text="click", command=mover_boton, bg="blue", fg="white", font=("Arial", 14), width=20, height=3)
boton.place(x=100, y=150)  


ventana.mainloop()
