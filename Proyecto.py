#PROYECTO FINAL : APLICACIÓN PARA PEDIR COMIDA A UN RESTAURANTE
#AUTORA: Evelyn Tabares Valencia
import tkinter as tk
from tkinter import Tk,Text,Button,END,re,Entry,PhotoImage
from tkinter import *
from tkinter import messagebox as MessageBox

class Interfaz:
    def __init__(self, ventana1):
        ventana1.withdraw()
        #Inicializar la ventana con un título
        self.win=Toplevel()
        self.win.title("Proyecto")
        self.win.geometry("400x700")#Tamaño de la ventana
        self.win.resizable(0, 0) #No permite redimensionar la ventana
        boton1= Button(self.win, text="Entrar", width=19, height=1, font=("Corbel",15), command=lambda:self.menuprincipal(self.win))# Menú
        boton1.place(x=100,y=300)
    def menuprincipal(self, ventana1):
        ventana1.withdraw()
        #Inicializar la ventana con un título
        self.win=Toplevel()
        self.win.title("Proyecto")
        self.win.geometry("400x700")#Tamaño de la ventana
        self.win.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="menu1.png" )#Fondo
        imagenf=Label(self.win,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)

 #Crear los botones de la ventana principal 
        boton1= Button(self.win, text="Menú", width=19, height=1, font=("Corbel",15), command=lambda:self.abrirMenu(self.win))# Menú
        boton2=Button(self.win, text="Carrito de compra", width=19, height=1, font=("Corbel",15),command=lambda:self.abrirCarrito(self.win))#Carrito
        boton3=Button(self.win, text="Cupón de descuento", width=19, height=1, font=("Corbel",15), command=lambda:self.abrirCodigo(self.win))#Codigo de descuento
        #Ubicar los botones con el gestor grid
        botones=[boton1, boton2, boton3]
        contador=0        
        for fila in range(1,4):
            botones[contador].place(x=100,y=160+fila*80)#Ubicar botones en la ventana
            contador+=1
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio
#---------------------------
    def abrirMenu(self,ventana): #Menú de comidas del restaurante 
        ventana.withdraw()
        win=Toplevel()
        win.title("Menú")
        win.geometry("400x700")#Tamaño de la ventana
        win.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="platos.png" )#Fondo
        imagenf=Label(win,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        boton4=Button(win,text="Entradas", width=19, height=1, font=("Corbel",15), command=lambda:MenuComidas.abrirEntradas(self,win))
        boton5=Button(win, text="Platos fuertes", width=19, height=1, font=("Corbel",15), command=lambda:MenuComidas.abrirPfuerte(self,win))
        boton6=Button(win, text="Bebidas", width=19, height=1, font=("Corbel",15), command=lambda:MenuComidas.abrirBebidas(self,win))
        boton7=Button(win, text="Postres", width=19, height=1, font=("Corbel",15), command=lambda:MenuComidas.abrirPostres(self,win))
        botonsalir=Button(win, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: self.atrasvprincipal(win)) #botón canje
        botonsalir.place(x=315,y=620)
        #Ubicar los botones con el gestor grid
        botones=[boton4, boton5, boton6,boton7]
        contador=0
            
        for fila in range(1,5):
            botones[contador].place(x=100,y=130+fila*70)
            contador+=1
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio

    def abrirCarrito(self,ventana):
        ventana.withdraw()
        win=tk.Toplevel()
        win.title("Carrito de compra")
        win.geometry("410x700")
        win.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="carrito.png" )#Fondo
        imagenf=Label(win,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        #botón salir
        Button(win, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: self.atrasvprincipal(win)).place(x=315,y=650)
        Button(win, text="Realizar pedido", width=13, height=1, font=("Bahnschrift Light",13),command=lambda: self.validarpago(win,total)).place(x=30,y=650)
        costo=[14000,22600,14500,14000,9800,38300,35900,35000,35500,44900,7500,8800,5300,10500,5300,15000,15500,15000,18000,20000]#Faltan los combos y bebidas
        NombPlato=['Empanadas','Chicharrón','Crema de maíz','Champiñones al ajillo','Patacones con hogao','Bandeja paisa','Filete de pescado','Mondongo','Filete de pechuga','Salmón en salsa','Limonada','Jugo de mora','Coca-cola','Soda de mango','Sprite','Torta de maracuyá','Tarta Napoleón','Arroz con leche','Merengón','Flan tres leches']
        subtotal = 0
        total= 0
        conty=30 #Contador para posición Y 
        descuento =0
        for i in range(len(platos)):#Recorre la lista platos
            if cantidades[i] > 0:#si la cantidad del pedido es > 0
                u=platos[i] #Me indica que plato es
                precio = costo[u]*cantidades[i]
                conty= conty + 30 #contador posición Y
                Label(win,text= f" {NombPlato[u]} {cantidades[i]} unidades", font=("Sans-Serif",10)).place(x=10, y=conty)#Nombre y unidades del pedido
                Label(win,text=f"Costo : {precio} ",font=("Sans-Serif",10)).place(x=250, y=conty)#Precio del pedido
                Button(win, text="X",width= 2,height=1,background="LightSalmon2", font=("Sans-Serif",8),command=lambda: self.eliminar(win,i)).place(x=370, y=conty)#Eliminar pedido
                subtotal= subtotal + precio
            else: #Eliminamos el plato del carrito si cantidad == 0
                del cantidades[i] 
                del platos[i]
        for descuento in codigodes:
            optotal= (subtotal*descuento)/100
            
        if descuento == 0: #Si no hay descuento
            total=subtotal
        else:
            total= subtotal - optotal
        Label(win,text= f"Subtotal :{subtotal}", font=("Sans-Serif",10)).place (x=205, y=conty + 50)#Subtotal de la compra
        Label(win,text= f"Descuento :{descuento}%", font=("Sans-Serif",10)).place (x=205, y=conty + 80)#Subtotal de la compra
        Label(win,text= f"Total :{total}", font=("Sans-Serif",10)).place (x=205, y=conty + 110)#Subtotal de la compra
         #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio
    #---
    def eliminar(self,win,i):#Eliminar un pedido desde la interfaz de usuario
        del cantidades[i] 
        del platos[i]
        self.abrirCarrito(win)
    #---------
    def validarpago(self,win,total):#Valida que haya algo para pagar 
        if total ==0:#Si no ha pedido 
            MessageBox.showinfo("Pago", "¡No hay pedidos, realice un pedido para pagar!") # título, mensaje
        else:#Si ya pidió 
            self.pagarpedido(win)#Abre la ventana de pago 

    def pagarpedido(self,win):
        win.withdraw()
        winpagar=tk.Toplevel()
        winpagar.title("Pagar Pedido")
        winpagar.geometry("400x700")
        winpagar.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="pagar.png" )#Fondo
        imagenf=Label(winpagar,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        Label(winpagar,text="Nombre", font=("Sans-Serif",14)).place(x=70, y=80)#Nombre
        nombre= StringVar()# La entrada a la caja de texto es un string
        Entry(winpagar,textvariable=nombre,justify="center",width=20,background="LightSalmon2").place(x=210,y=80)#Caja de texto
        #---------------------
        Label(winpagar,text="Apellido", font=("Sans-Serif",15)).place(x=70, y=130)#apellido
        apellido= StringVar()# La entrada a la caja de texto es un string
        Entry(winpagar,textvariable=apellido,justify="center",width=20,background="LightSalmon2").place(x=210,y=130)#Caja de texto
        #---------------------
        Label(winpagar,text="Dirección", font=("Sans-Serif",14)).place(x=70, y=180)#Dirección 
        direccion= StringVar()# La entrada a la caja de texto es un string
        Entry(winpagar,textvariable=direccion,justify="center",width=20,background="LightSalmon2").place(x=210,y=180)#Caja de texto
        #---------------------
        Label(winpagar,text= "Ciudad", font=("Sans-Serif",14)).place(x=70, y=230)#Ciudad
        ciudad= StringVar()# La entrada a la caja de texto es un string
        Entry(winpagar,textvariable=ciudad,justify="center",width=20, background="LightSalmon2").place(x=210,y=230)#Caja de texto
        #---------------------
        Label(winpagar,text= "Teléfono", font=("Sans-Serif",14)).place(x=70, y=280)#Telefono
        telefono= StringVar()# La entrada a la caja de texto es un string
        Entry(winpagar,textvariable=telefono,justify="center",width=20,background="LightSalmon2").place(x=210,y=280)#Caja de texto
        #---------------------
        
        Button(winpagar, text="Pagar", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: self.finalizacompra(nombre,apellido,direccion,ciudad,telefono)).place(x=30,y=650)
        Button(winpagar, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: self.abrirCarrito(winpagar)).place(x=315,y=650)
         #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio
    #--------------   
    def finalizacompra(self,nombre,apellido,direccion,ciudad,telefono):
        #Si el usuario ingresa sus datos se realiza el pago
        if nombre.get() != "" and apellido.get() != "" and direccion.get() != "" and ciudad.get() != "" and telefono.get() != "":
            MessageBox.showinfo("Pago", "¡Pago Exitoso!") # título, mensaje
            platos.clear() #Limpia la lista de platos
            cantidades.clear()#Limpia la lista de cantidades de cada plato
            codigodes.clear()#Limpia el descuento 
        else: # Si el usuario no ingresa sus datos
            MessageBox.showinfo("Pago", "¡Ingrese todos sus datos!") # título, mensaje
 #--------------
    def abrirCodigo(self,ventana):#Canjear codigo de descuento 
        ventana.withdraw()
        winc=Toplevel()
        winc.title("Cupón de descuento")
        winc.geometry("400x700")#Tamaño de la ventana
        winc.resizable(0, 0) #No permite redimensionar la ventana
        
        fondo=PhotoImage(file="codigo.png" )#Fondo
        imagenf=Label(winc,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        letrerocodigo=Label(winc,text= "Código de descuento: ", font=("Corbel",15))
        letrerocodigo.place(x=120, y=105)
        self.entradaN= tk.StringVar()# La entrada a la caja de texto es nn estring
        #Caja de texto para escribir el codigo de descuento
        self.EscriCodigo = tk.Entry(winc,textvariable=self.entradaN,justify="center",width=30,background="LightSalmon2").place(x=120,y=200)
        #Botón para validar el canje
        canje=Button(winc, text="Canje", width=10, height=1, font=("Corbel",15),command=lambda: self.validarCodigo(self.entradaN)) #botón canje
        canje.place(x=150,y=250)
        #Botón para regresar al menú de inicio
        #winc2=winc.withdraw()
        botonAtras = Button(winc, text="Menú", width=10, height=1, font=("Corbel",15), command=lambda:self.atrasvprincipal(winc))#botón inicio
        botonAtras.place(x=150,y=450)
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio
#----------
    def validarCodigo(self,entradaN): #Validar codigo de descuento 
        #USO DE ENCAPSULAMIENTO PARA PROTEGER LOS CODIGOS
        self.__codigo1= "E1R2T3Y4U4"#codigo del 13% de descuento
        self.__codigo2= "U45STY852P"#codigo del 15% de descuento
        self.__codigo3= "Q902FKJ09W"#codigo del 20% de descuento
        self.__codigo4= "KSE45XD5V2"#codigo del 5% de descuento
        mensaje= self.entradaN.get()
        #Si se ingresa un codigo de descuento   
        if mensaje == self.__codigo1:
           codigodes.append(13)
           MessageBox.showinfo("Canje", "¡Canje Exitoso!") # título, mensaje
        elif mensaje == self.__codigo2:
           codigodes.append(15)
           MessageBox.showinfo("Canje", "¡Canje Exitoso!") # título, mensaje
        elif mensaje == self.__codigo3:
           codigodes.append(20)
           MessageBox.showinfo("Canje", "¡Canje Exitoso!") # título, mensaje
        elif mensaje == self.__codigo4:
           codigodes.append(5)
           MessageBox.showinfo("Canje", "¡Canje Exitoso!") # título, mensaje
        else:
          MessageBox.showinfo("Canje", " Código inválido") # título, mensaje
#---      
    def atrasvprincipal(self,win):#Regreso al menú de principal
        win.withdraw()
        win3=Toplevel()
        self.menuprincipal(win3)
#--------------------------__________________ --------------------------------------------------------------       
#------------------------- |MENÚ DE PLATILLOS|-------------------------------------------------------------------------
class MenuComidas(Interfaz):
    
    def atrasmenu(self,winE):#Regreso al menú general de comidas 
        winE.withdraw()
        win2=Toplevel()
        self.abrirMenu(win2)
    #Opciones del Menú de comidas---------------
    def abrirEntradas(self,win):
        win.withdraw()#creación de nueva ventana
        self.winE=Toplevel(ventana_p)
        self.winE.title("Entradas")
        self.winE.geometry("400x700") #"400x700"
        self.winE.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="entradas.png" )#Fondo
        imagenf=Label(self.winE,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        
        self.Ent1= IntVar()# La entrada a la caja de texto es un int
        #Caja de texto para escribir la cantidad de comida
        self.EscriCant = Entry(self.winE,textvariable=self.Ent1,justify="center",width=3,background="LightSalmon2").place(x=275,y=80)
        #Botón para añadir al carrito
        añadir=Button(self.winE, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Ent1,0)) #botón canje
        añadir.place(x=315,y=70)
        info= Button(self.winE,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato0()))
        info.place(x=10,y=95)
        #   2------
        self.Ent2= IntVar()# Entrada 2
        self.EscriCant2 = Entry(self.winE,textvariable=self.Ent2,justify="center",width=3,background="LightSalmon2").place(x=275,y=195)
        #Botón para añadir al carrito 2
        añadir2=Button(self.winE, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Ent2,1)) #botón canje
        añadir2.place(x=315,y=185)
        info= Button(self.winE,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato1()))
        info.place(x=10,y=205)
        #   3------
        self.Ent3= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant3 = Entry(self.winE,textvariable=self.Ent3,justify="center",width=3,background="LightSalmon2").place(x=275,y=320)
        #Botón para añadir al carrito 3
        añadir3=Button(self.winE, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Ent3,2)) #botón canje
        añadir3.place(x=315,y=310)
        info= Button(self.winE,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato2()))
        info.place(x=10,y=315)
        #   4-----------
        self.Ent4= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant4 = Entry(self.winE,textvariable=self.Ent4,justify="center",width=3,background="LightSalmon2").place(x=275,y=440)
        #Botón para añadir al carrito 3
        añadir4=Button(self.winE, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Ent4,3)) #botón canje
        añadir4.place(x=315,y=430)
        info= Button(self.winE,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato3()))
        info.place(x=10,y=425)
       
        #   5--------------
        self.Ent5= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant5 = Entry(self.winE,textvariable=self.Ent5,justify="center",width=3,background="LightSalmon2").place(x=275,y=560)
        añadir5=Button(self.winE, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Ent5,4)) #botón canje
        añadir5.place(x=315,y=550)
        info= Button(self.winE,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato4()))
        info.place(x=10,y=545)
        
        añadir6=Button(self.winE, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: MenuComidas.atrasmenu(self,self.winE)) #botón canje
        añadir6.place(x=315,y=650)
        #Abrir carrito -----
        carrito=Button(self.winE, text="Carrito", width=7, height=1, font=("Bahnschrift Light",13),command=lambda: Interfaz.abrirCarrito(self,self.winE)) #botón carrito
        carrito.place(x=30,y=650)
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inicio
#---------      
    def Carrito(cantP,indice): #Añade los elementos ingresados por el usuario en la lista 
        if indice in platos: #Si ya se ha guardado un pedido de ese plato
            id= platos.index(indice)#Indice del número ya guardado en la lista
            cantn= cantP.get() # cantidad del nuevo plato
            cantidades[id] = cantidades[id]+ cantn #Suma la cantidad antigua del plato con la nueva
        else:
            platos.append(indice)#El indice indica que plato es 
            cantidades.append(cantP.get())#Cantidad de comida pedida   
#--------
    def abrirPfuerte(self,win):#Platos fuertes 
        win.withdraw()
        self.winPf=Toplevel()
        self.winPf.title("Platos fuertes")
        self.winPf.geometry("400x700")
        self.winPf.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="platosfuertes.png" )#Fondo
        imagenf=Label(self.winPf,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        self.Pf1= IntVar()# La entrada a la caja de texto es un int
        #Caja de texto para escribir la cantidad de comida
        self.EscriCant = Entry(self.winPf,textvariable=self.Pf1,justify="center",width=3,background="LightSalmon2").place(x=275,y=80)
        #Botón para añadir al carrito
        añadir=Button(self.winPf, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pf1,5)) #botón canje
        añadir.place(x=315,y=70)
        info= Button(self.winPf,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato5()))
        info.place(x=10,y=95)
        #   2------
        self.Pf2= IntVar()# Entrada 2
        self.EscriCant2 = Entry(self.winPf,textvariable=self.Pf2,justify="center",width=3,background="LightSalmon2").place(x=275,y=195)
        #Botón para añadir al carrito 2
        añadir2=Button(self.winPf, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pf2,6)) #botón canje
        añadir2.place(x=315,y=185)
        info= Button(self.winPf,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato6()))
        info.place(x=10,y=205)
        #   3------
        self.Pf3= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant3 = Entry(self.winPf,textvariable=self.Pf3,justify="center",width=3,background="LightSalmon2").place(x=275,y=320)
        #Botón para añadir al carrito 3
        añadir3=Button(self.winPf, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pf3,7)) #botón canje
        añadir3.place(x=315,y=310)
        info= Button(self.winPf,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato7()))
        info.place(x=10,y=315)
        #   4-----------
        self.Pf4= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant4 = Entry(self.winPf,textvariable=self.Pf4,justify="center",width=3,background="LightSalmon2").place(x=275,y=440)
        #Botón para añadir al carrito 3
        añadir4=Button(self.winPf, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pf4,8)) #botón canje
        añadir4.place(x=315,y=430)
        info= Button(self.winPf,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato8()))
        info.place(x=10,y=425)
        #   5--------------
        self.Pf5= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant5 = Entry(self.winPf,textvariable=self.Pf5,justify="center",width=3,background="LightSalmon2").place(x=275,y=560)
        añadir5=Button(self.winPf, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pf5,9)) #botón canje
        añadir5.place(x=315,y=550)
        info= Button(self.winPf,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato9()))
        info.place(x=10,y=545)

        añadir6=Button(self.winPf, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: MenuComidas.atrasmenu(self,self.winPf)) #botón canje
        añadir6.place(x=315,y=650)
        #Abrir Carrito----
        carrito=Button(self.winPf, text="Carrito", width=7, height=1, font=("Bahnschrift Light",13),command=lambda: Interfaz.abrirCarrito(self,self.winPf)) #botón carrito
        carrito.place(x=30,y=650)
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inici
#---------
    def abrirBebidas(self,win):
        win.withdraw()
        self.winbe=Toplevel()
        self.winbe.title("Bebidas")
        self.winbe.geometry("400x700")
        self.winbe.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="BEBIDAS.png" )#Fondo
        imagenf=Label(self.winbe,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)

        self.be1= IntVar()# La entrada a la caja de texto es un int
        #Caja de texto para escribir la cantidad de comida
        self.EscriCant = Entry(self.winbe,textvariable=self.be1,justify="center",width=3,background="LightSalmon2").place(x=275,y=80)
        #Botón para añadir al carrito
        añadir=Button(self.winbe, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.be1,10)) #botón canje
        añadir.place(x=315,y=70)
        info= Button(self.winbe,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato10()))
        info.place(x=10,y=95)
        #   2------
        self.be2= IntVar()# Entrada 2
        self.EscriCant2 = Entry(self.winbe,textvariable=self.be2,justify="center",width=3,background="LightSalmon2").place(x=275,y=195)
        #Botón para añadir al carrito 2
        añadir2=Button(self.winbe, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.be2,11)) #botón canje
        añadir2.place(x=315,y=185)
        info= Button(self.winbe,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato11()))
        info.place(x=10,y=205)
        #   3------
        self.be3= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant3 = Entry(self.winbe,textvariable=self.be3,justify="center",width=3,background="LightSalmon2").place(x=275,y=320)
        #Botón para añadir al carrito 3
        añadir3=Button(self.winbe, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.be3,12)) #botón canje
        añadir3.place(x=315,y=310)
        info= Button(self.winbe,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato12()))
        info.place(x=10,y=315)
        #   4-----------
        self.be4= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant4 = Entry(self.winbe,textvariable=self.be4,justify="center",width=3,background="LightSalmon2").place(x=275,y=440)
        #Botón para añadir al carrito 3
        añadir4=Button(self.winbe, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.be4,13)) #botón canje
        añadir4.place(x=315,y=430)
        info= Button(self.winbe,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato13()))
        info.place(x=10,y=425)
        #   5--------------
        self.be5= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant5 = Entry(self.winbe,textvariable=self.be5,justify="center",width=3,background="LightSalmon2").place(x=275,y=560)
        añadir5=Button(self.winbe, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.be5,14)) #botón canje
        añadir5.place(x=315,y=550)
        info= Button(self.winbe,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato14()))
        info.place(x=10,y=545)
        
        añadir6=Button(self.winbe, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: MenuComidas.atrasmenu(self,self.winbe)) #botón canje
        añadir6.place(x=315,y=650)
        #Abrir Carrito----
        carrito=Button(self.winbe, text="Carrito", width=7, height=1, font=("Bahnschrift Light",13),command=lambda: Interfaz.abrirCarrito(self,self.winbe)) #botón carrito
        carrito.place(x=30,y=650)
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inici
#--------
    def abrirPostres(self,win):
        win.withdraw()
        winpos=Toplevel()
        winpos.title("Combos")
        winpos.geometry("400x700")
        winpos.resizable(0, 0) #No permite redimensionar la ventana
        fondo=PhotoImage(file="postres.png" )#Fondo
        imagenf=Label(winpos,image=fondo)
        imagenf.place(x=0,y=0,relheight=1,relwidth=1)
        
        self.Pos1= IntVar()# La entrada a la caja de texto es un int
        #Caja de texto para escribir la cantidad de comida
        self.EscriCant = Entry(winpos,textvariable=self.Pos1,justify="center",width=3,background="LightSalmon2").place(x=275,y=80)
        #Botón para añadir al carrito
        añadir=Button(winpos, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pos1,15)) #botón canje
        añadir.place(x=315,y=70)
        info= Button(winpos,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato15()))
        info.place(x=10,y=95)
        #   2------
        self.Pos2= IntVar()# Entrada 2
        self.EscriCant2 = Entry(winpos,textvariable=self.Pos2,justify="center",width=3,background="LightSalmon2").place(x=275,y=195)
        #Botón para añadir al carrito 2
        añadir2=Button(winpos, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pos2,16)) #botón canje
        añadir2.place(x=315,y=185)
        info= Button(winpos,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato16()))
        info.place(x=10,y=205)
        #   3------
        self.Pos3= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant3 = Entry(winpos,textvariable=self.Pos3,justify="center",width=3,background="LightSalmon2").place(x=275,y=320)
        #Botón para añadir al carrito 3
        añadir3=Button(winpos, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pos3,17)) #botón canje
        añadir3.place(x=315,y=310)
        info= Button(winpos,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato17()))
        info.place(x=10,y=315)
        #   4-----------
        self.Pos4= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant4 = Entry(winpos,textvariable=self.Pos4,justify="center",width=3,background="LightSalmon2").place(x=275,y=440)
        #Botón para añadir al carrito 3
        añadir4=Button(winpos, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pos4,18)) #botón canje
        añadir4.place(x=315,y=430)
        info= Button(winpos,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato18()))
        info.place(x=10,y=425)
        #   5--------------
        self.Pos5= IntVar()# La entrada a la caja de texto es un int
        self.EscriCant5 = Entry(winpos,textvariable=self.Pos5,justify="center",width=3,background="LightSalmon2").place(x=275,y=560)
        añadir5=Button(winpos, text="Añadir", width=5, height=1, font=("Bahnschrift Light",13),command=lambda:MenuComidas.Carrito(self.Pos5,19)) #botón canje
        añadir5.place(x=315,y=550)
        info= Button(winpos,text="i", font=("Bahnschrift Light",10),command=lambda:funcion(Plato19()))
        info.place(x=10,y=545)

        añadir6=Button(winpos, text="atrás", width=5, height=1, font=("Bahnschrift Light",13),command=lambda: MenuComidas.atrasmenu(self,winpos)) #botón canje
        añadir6.place(x=315,y=650)
        #Abrir Carrito----
        carrito=Button(winpos, text="Carrito", width=7, height=1, font=("Bahnschrift Light",13),command=lambda: Interfaz.abrirCarrito(self,winpos)) #botón carrito
        carrito.place(x=30,y=650)
        #Botón error
        Button(self.win1, text="atrás", width=5, height=1, font=("Corbel",15), command=lambda: MenuComidas.atrasmenu(self,self.win1))#botón inici

#----------____________________________-------
#----------|INGREDIENTES DE CADA PLATO |----------------------------------------------------------------------------------------------------
class Plato0:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes", "Tomate, cebolla, pimentón, carne molida de cerdo y de res, harina de maíz precocida, limón y ají para servir ") # título, mensaje
class Plato1:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Tocino de cerdo, sal, polvo para hornear, limón para servir.")
class Plato2:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Mazorca, ajo, cilantro, papa, cebolla, crema de leche.")  
class Plato3:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Champiñones, aceite de oliva, dientes de ajo, perejil, sal y pimineta, zumo de limón, cayena") 
class Plato4:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Platanos verdes, aceite vegetal,cebolla larga, tomate, sal y pimineta, mantequilla, queso blanco.")
class Plato5:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Cebolla, tomate, frijoles, carne molida, arroz blanco, tocino, chorizo, huevo, aguacate, arepa, plátano maduro ")
class Plato6:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Filete de pescado, ajo, sal, limón, aceite de oliva, pimienta, perejil ")  
class Plato7:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Mondongo, agua, aceite, limón, cebolla, carne de cerdo, tomate, zanahoria, papa, arveja.")  
class Plato8:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Pechuga de pollo, cebolla, ajo, harina, vino blanco, laurel, aceite de oliva, sal y pimienta.")
class Plato9:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Salmón, limón, sal y pimienta, aceite, mayonesa, alcaparras, ajo, cebolla, hinojo,perejil.")  
class Plato10:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Limón, lima, azúcar, hielo, ralladura de limón, lechera, agua") 
class Plato11:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Mora, leche, hielo, hierba buena, azúcar ") 
class Plato12:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Gaseosa Coca-cola")
class Plato13:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes", "concentrado de tamarindo, chile con limón en polvo, limón, fresas, mango, azucar, jugo de limón." )   
class Plato14:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Gaseosa Sprite")
class Plato15:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Mantequilla, crema de leche, huevo, azúcar, pulpa de maracuyá, galletas de coco, yema de huevo.")
class Plato16:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Requesón, fresas, azúcar, mantequilla, miel, huevos.")      
class Plato17:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Agua,arroz, canela, leche, leche condensada, crema de leche, uvas pasas, queso opcional.") 
class Plato18:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","Claras de huevo, azúcar, duraznos, crema de leche, fresas, frambuesas.")    
class Plato19:
    def ingredientes(self):
        MessageBox.showinfo("Ingredientes","azúcar, agua, huevos, leche condensada, crema de leche, leche, esencia de vainilla, fresas, moras.")        
def funcion(objeto):
    objeto.ingredientes()
        



   
ventana_p=Tk()
proyecto=Interfaz(ventana_p)
platos=[]
cantidades=[]
costo=[]
codigodes=[]        
ventana_p.mainloop()