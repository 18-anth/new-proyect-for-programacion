from tkinter import *
from tkinter import ttk
import tkinter as tk
import funciones 

def ventanaCapturaDatos():
    def devolverDatos():
        textoCaja= entryTexto.get()
        texto.set(textoCaja)    
    root=Tk()
    root.title("Entrada de datos")
    root.geometry("505x350")
    root.config(cursor="pirate")
    root.iconbitmap(r"imagen_fondo\warner.ico")
    ro = tk.PhotoImage(file = r"imagen_fondo\marvel y dc.gif")
    Label = tk.Label(root,image= ro).place(x = 0, y = 0)
    #FRAME DE ENTRADA DE DATOS*-
    miFrame= Frame(root)
    miFrame.pack()
    texto = StringVar()
    #ENTRY 

    entryTexto=Entry(miFrame, justify=CENTER ,textvariable=texto)
    entryTexto.grid(row=0, column=0, padx=5, pady=5)
      
    #BOTÓN Buscar
    
    boton = Button(root, text = "SEARCH", font=('verdana',12, 'bold'), command = root.destroy)
    boton.pack()

    root.mainloop()
    return texto.get()
texto = ventanaCapturaDatos()
##########################  Ventana de salida ###################################

ventana = Tk()
ventana.title("Superhero Information")
ventana.geometry("925x300")
ventana.config(cursor="pirate")
ventana.iconbitmap(r"imagen_fondo\warner.ico")
co = tk.PhotoImage(file = r"imagen_fondo\marvel y dc.gif")
Label = tk.Label(ventana,image= co).place(x = 0, y = 0)
superHero = texto
heroe = funciones.getHeroePorSuperHero(superHero)
#############################  Scrollar y Bandeja de texto ###################
scrollbar = Scrollbar(ventana)
scrollbar.pack( side = RIGHT, fill = Y )
text1 = tk.Text(ventana,  font=('times',12), height = 25, width = 50)
text1.configure( yscrollcommand = scrollbar.set)    
text1.pack(side = RIGHT)
scrollbar.config(command = text1.yview )

end = Button(ventana, font = "times", text = "Exit Superhero Information", fg = "Red",
                command = ventana.destroy).place(x = 0)
#############  pantalla de escritura ##############
text1.config(state = "normal")
text1.insert(tk.INSERT, heroe)
text1.pack()


ventana.mainloop()  
