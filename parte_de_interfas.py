from tkinter import *
import tkinter as tk
from tkinter import ttk
import parte_busqueda
import data

Margot = Tk()
Margot.geometry("500x500")
Margot.title("Albun de Super Heroes")
Margot.config(cursor="pirate")

###############  Menu de Marvel  ##################
def abrir():
    veabrir= Tk()
    veabrir.geometry("310x105+50+50")
    veabrir.resizable(0,0)
    veabrir.title("Información")
    veabrir.config(bg = "Black")
    Label(veabrir, text="Realizado por: Anthony Córdova",font = "Times", 
                        bg = "Black", fg = "Red").pack()
    Label(veabrir, text="Contactos : anthonycordova330@gmail.com ",  font = "Times",
                        bg = "Black", fg = "Red").pack()
    Label(veabrir, text="Version : 1.2.5.3",  font = "Times", 
                        bg = "Black", fg = "Red").pack()
    Label(veabrir, text="La vercion mas receinte esta instalada.", font = "Times",
                        bg = "Black", fg = "Red").pack()
    
    veabrir.mainloop()
##########  Menú en Marvel  ################
barra=Menu(Margot)
MenuArchivo=Menu(barra)
MenuArchivo.add_command(label="Informacion",command= abrir)#Opciones
MenuArchivo.add_separator()#Separador
MenuArchivo.add_command(label="Nuevo")#Opciones
MenuArchivo.add_separator()#Separador
MenuArchivo.add_command(label="Salir",command=Margot.destroy)#Opciones
barra.add_cascade(label="Menu",menu=MenuArchivo)
Margot.config(menu=barra)
################## Icono de Margot ######################
Margot.iconbitmap(r"imagen_fondo\warner.ico")
tab_control = ttk.Notebook(Margot)
#################  pestaña inicial ######################

################### def de ventanas de impreción ###########
index = -1
def get_heroe():
    global index
    superHero = index
    return data.heroes[index]
def getLabel():
        vird = Tk()
        vird.geometry("900x150")
        vird.title("Información del Super Heroe")
        vird.iconbitmap(r"imagen_fondo\warner.ico")
        vird.config(bg = "Black")
        muerteamix = get_heroe()['id'],",",get_heroe()['superhero'],",",get_heroe()['publisher'],",",get_heroe()['alter_ego'], ",", get_heroe()['first_appearance'], ",", get_heroe()['characters'],",",get_heroe()['information']
       
        scrollbar = Scrollbar(vird)
        scrollbar.pack( side = RIGHT, fill = Y )
        text1 = tk.Text(vird,  font=('times',12), height = 25, width = 50)
        text1.configure( yscrollcommand = scrollbar.set)    
        text1.pack(side = RIGHT )
        scrollbar.config(command = text1.yview )
        #############  pantalla de escritura ##############
        text1.config(state = "normal")
        text1.insert(tk.INSERT, muerteamix)
        text1.pack()


        boton = Button(vird, text="Exit Superhero Information", font = "times", fg = "Red",
                command=vird.destroy).place(x = 0, y = 0)
        vird.mainloop()

def siguiente_Heroe():
    global index
    index = index + 1 
    getLabel()
####################################### Universo  DC    #########################################
tab1 = ttk.Frame(tab_control)
################## Imagen de fondo en Dc ########################
dcvent=tk.PhotoImage(file= r"imagen_fondo\DC image.gif")
label2=tk.Label(tab1,image=dcvent).place(x = 0, y = 26)
################### Nombres de cada Super heroe del Universo Dc #############

arrow = PhotoImage(file = r"imagen\imagen.gif\dc-arrow.gif")
lard = Button(tab1, image = arrow, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 80, y = 20)

batman = PhotoImage(file = r"imagen\imagen.gif\dc-batman.gif")
berd = Button(tab1, image = batman, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 330, y = 20)
            
Black = PhotoImage(file = r"imagen\imagen.gif\dc-black.gif")
jodi = Button(tab1, image = Black, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 580, y = 20)

blue = PhotoImage(file = r"imagen\imagen.gif\dc-blue.gif")
berdi = Button(tab1, image = blue, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 830, y = 20)

green = PhotoImage(file = r"imagen\imagen.gif\dc-green.gif")
salud = Button(tab1, image = green , command = siguiente_Heroe,
            height = 300, width = 200).place(x = 1080, y = 20)

martian = PhotoImage(file = r"imagen\imagen.gif\dc-martian.gif")
bad = Button(tab1, image = martian,  command = siguiente_Heroe,
            height = 300, width = 200).place(x = 80, y = 350)

robin = PhotoImage(file = r"imagen\imagen.gif\dc-robin.gif")
cor = Button(tab1, image = robin, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 330, y = 350)

flash = PhotoImage(file = r"imagen\imagen.gif\dc-flash.gif")
do = Button(tab1, image = flash, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 580, y = 350)

superman = PhotoImage(file = r"imagen\imagen.gif\dc-superman.gif")
bore = Button(tab1, image = superman, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 830, y = 350)

wonder = PhotoImage(file = r"imagen\imagen.gif\dc-wonder.gif")
fun = Button(tab1, image = wonder, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 1080, y = 350)

#######################################    Marvel    #########################################           
tab2 = ttk.Frame(tab_control)
Label(tab2, text="Bienvenidos al Universo de Marvel ",
                bg = "black", fg = "Red",
                        font = "Times",padx = 30, pady = 0 ).place(x = 250, y = 3)
################## Imagen de fondo en Marvel ########################
fondov=tk.PhotoImage(file= r"imagen_fondo\fondo marvel.gif")
label1=tk.Label(tab2,image=fondov).place(x = 0, y = 29)
################### Nombres de cada Super heroe del Universo de Marvel #############

captain = PhotoImage(file = r"imagen\imagen.gif\marvel-captain.gif")
btns = Button(tab2, image = captain, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 80, y = 35)

cyclops = PhotoImage(file = r"imagen\imagen.gif\marvel-cyclops.gif")
btnsa = Button(tab2, image = cyclops,  command = siguiente_Heroe,
            height = 300, width = 200).place(x = 330, y = 35)

daredevil = PhotoImage(file = r"imagen\imagen.gif\marvel-daredevil.gif")
btn = Button(tab2, image =daredevil, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 580, y = 35)

hawkeye = PhotoImage(file = r"imagen\imagen.gif\marvel-hawkeye.gif")
btnsal = Button(tab2, image = hawkeye, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 830, y = 35)

hulk = PhotoImage(file = r"imagen\imagen.gif\marvel-hulk.gif")
btp = Button(tab2, image = hulk, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 1080, y = 35)

ironman = PhotoImage(file = r"imagen\imagen.gif\marvel-iron.gif")
blth = Button(tab2, image = ironman, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 80, y = 370)

silver = PhotoImage(file = r"imagen\imagen.gif\marvel-silver.gif")
filip = Button(tab2, image = silver, command = siguiente_Heroe,
            height = 300, width = 200).place(x = 330, y = 370)

spider = PhotoImage(file = r"imagen\imagen.gif\marvel-spider.gif")
morgan = Button(tab2, image = spider , command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 580, y = 370)

thor = PhotoImage(file = r"imagen\imagen.gif\marvel-thor.gif")
bernardo = Button(tab2, image = thor, command = siguiente_Heroe,  
            height = 300, width = 200).place(x = 830, y = 370)

wolverine = PhotoImage(file = r"imagen\imagen.gif\marvel-wolverine.gif")
san = Button(tab2, image = wolverine, command = siguiente_Heroe, 
            height = 300, width = 200).place(x = 1080, y = 370)

tab_control.add(tab1, text='Universo DC')
tab_control.add(tab2, text='Universo de Marvel')

tab_control.pack(expand=1, fill='both')

Margot.mainloop()