from tkinter import *
from PIL import ImageTk,Image
#Datos tablero
M=10
N=10
T=120
#Datos Jugador 1
Nj1 = 'Jugador 1'
Cj1='Blue'
Pj1=0
#Datos Jugador 2
Nj2 = 'Jugador 2'
Cj2='Red'
Pj2=0



def archivo():
    archivo=Tk()
    cargaPartida=Button(archivo,text='Cargar Parrtida').pack()
    guardaPartida=Button(archivo,text='Guardar Partida').pack()
    MatrizGraphviz=Button(archivo,text='Matriz Graphviz').pack()
    HTML=Button(archivo,text='Reporte HTML').pack()
    salir=Button(archivo,text='Salir',command=archivo.destroy).pack()
    archivo.mainloop()

def config():
    global M,N,T,Nj1,Nj2,Cj1,Cj2,Pj1,Pj2
    config=Tk()
    config.title('Configuracion')
 #Jugador 1
    j1=LabelFrame(config, text="Jugador 1")
    j1.pack()
  #Alias 
    aliasLabelJ1=Label(j1,text='Alias: ').grid(row=0,column=0)
    aliasBoxJ1=Entry(j1,text=Nj1).grid(row=0,column=1)
  #opciones color
    colorLabelJ1=Label(j1,text='Color: ').grid(row=1,column=0)
    clicked1=StringVar()
    clicked1.set(Cj1)
    opj1=OptionMenu(j1,clicked1,"Blue","Red","Yellow","Green").grid(row=1,column=1)

 #Jugador 2
    j2=LabelFrame(config,text='Jugador 2')
    j2.pack()
  #Alias 
    aliasLabelJ2=Label(j2,text='Alias: ').grid(row=0,column=0)
    aliasBoxJ2=Entry(j2).grid(row=0,column=1)
  #opciones color
    colorLabel=Label(j2,text='Color: ').grid(row=1,column=0)
    clicked2=StringVar()
    clicked2.set(Cj2)
    opj1=OptionMenu(j2,clicked2,"Blue","Red","Yellow","Green").grid(row=1,column=1)

 #General
    gn=LabelFrame(config,text='General')
    gn.pack()
    tiempoLabel=Label(gn,text='Tiempo: ').grid(row=0,column=0)
    tiempoBox=Entry(gn).grid(row=0,column=1)
    piezasLabel=Label(gn,text='Cantidad de piezas: ').grid(row=1,column=0)
    piezasBox=Entry(gn).grid(row=1,column=1)

    mLabel=Label(gn,text='M: ').grid(row=2,column=0)
    mBox=Entry(gn).grid(row=2,column=1)

    nLabel=Label(gn,text='N: ').grid(row=3,column=0)
    nBox=Entry(gn).grid(row=3,column=1)

    ok=Button(config,text='Aceptar').pack()
    salir=Button(config,text='Cancelar',command=config.destroy).pack()
    config.mainloop()

def principal():
    global M,N,T,Nj1,Nj2,Cj1,Cj2,Pj1,Pj2

    root = Tk()
    root.title("Proyecto 1")
    op=LabelFrame(root)
    op.grid(row=0,column=0)
    arc=Button(op,text='Archivo',command=archivo).grid(row=0,column=0)
    conf=Button(op,text='Configuracion',command=config).grid(row=0,column=1)

    data=LabelFrame(root)
    data.grid(row=1,column=0)
 #Jugador 1
    j1=LabelFrame(data, text="Jugador 1",padx=10,pady=10)
    j1.grid(row=1,column=0)
  #Alias 
   #Punteo
    PLabelJ1=Label(j1,text='Punteo: ').grid(row=0,column=0)
    PunteoJ1=Label(j1,text=Pj1).grid(row=0,column=1)
   #X
    XLabelJ1=Label(j1,text='X: ').grid(row=1,column=0)
    XJ1=Entry(j1).grid(row=1,column=1)
   #Y
    YLabelJ1=Label(j1,text='Y: ').grid(row=2,column=0)
    YJ1=Entry(j1).grid(row=2,column=1)
   #Boton Aceptar
    Bj1=Button(j1,text='Aceptar').grid(row=3,column=1)
   #imagen
    ImgLabelJ1=Label(j1,text='Pieza a poner: ').grid(row=4,column=0)
    img= ImageTk.PhotoImage(Image.open("./piezas/0.png"))
    ImgJ1=Label(j1,image=img).grid(row=4,column=1)

 #Juego
    ju1=LabelFrame(data, text="Juego",padx=10,pady=10)
    ju1.grid(row=1,column=1)
  #Alias 
   #Punteo
    TimeLabel=Label(ju1,text='Tiempo').grid(row=0,column=0)
    Time=Label(ju1,text=Pj1).grid(row=0,column=1)
   #X
    Terminar=Button(ju1,text='Terminar Partida').grid(row=1,column=1)
    Empezar=Button(ju1,text='Iniciar Partida').grid(row=1,column=2)

 #Jugador 2
    j2=LabelFrame(data, text="Jugador 2",padx=10,pady=10)
    j2.grid(row=1,column=2)
  #Alias 
   #Punteo
    PLabelJ2=Label(j2,text='Punteo: ').grid(row=0,column=0)
    PunteoJ2=Label(j2,text=Pj2).grid(row=0,column=1)
   #X
    XLabelJ2=Label(j2,text='X: ').grid(row=1,column=0)
    XJ2=Entry(j2).grid(row=1,column=1)
   #Y
    YLabelJ2=Label(j2,text='Y: ').grid(row=2,column=0)
    YJ2=Entry(j2).grid(row=2,column=1)
   #Boton Aceptar
    Bj1=Button(j2,text='Aceptar').grid(row=3,column=1)
   #imagen
    ImgLabelJ2=Label(j2,text='Pieza a poner: ').grid(row=4,column=0)
    img2= ImageTk.PhotoImage(Image.open("./piezas/0.png"))
    ImgJ2=Label(j2,image=img2).grid(row=4,column=1)

    

 #Tablero
    tabla=LabelFrame(root)
    tabla.grid(row=2,column=0)

    root.mainloop()

   
#config()
principal()