from tkinter import *
BASE=460
ALTURA=220

ventana_principal = Tk()
ventana_principal.title("Graficas 2d - lineas rectas")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="black")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="white", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas
c= Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="yellow")
c.place(x=10,y=10)

#lineas
linea1=c.create_line(10,10,BASE-10,10, fill="red")
linea2=c.create_line(BASE-10,10,BASE-10,ALTURA-10, fill="red")
linea3=c.create_line(BASE-10,ALTURA-10,10,ALTURA-10, fill="red")
linea4=c.create_line(10,ALTURA-10,10,10, fill="red")
linea5=c.create_line(10,10,BASE-10,ALTURA-10, fill="BLUE")
linea6=c.create_line(10,ALTURA-10,BASE-10,10, fill="BLUE")
linea7=c.create_line(190,10,290,10, fill="black", width=4)
linea8=c.create_line(190,ALTURA-10,290,ALTURA-10, fill="black", width=4)
linea9=c.create_line(BASE-10,60,BASE-10,ALTURA-60, fill="black", width=4)
linea10=c.create_line(10,60,10,ALTURA-60, fill="black", width=4)
linea11=c.create_line(10,60,190,60, fill="black", width=4)
linea12=c.create_line(290,60,BASE-10,60, fill="black", width=4)
linea13=c.create_line(10,ALTURA-60,190,ALTURA-60, fill="black", width=4)
linea14=c.create_line(290,ALTURA-60,BASE-10,ALTURA-60, fill="black", width=4)
linea15=c.create_line(190,10,190,60, fill="black", width=4)
linea16=c.create_line(290,10,290,60, fill="black", width=4)
linea17=c.create_line(190,ALTURA-60,190,ALTURA-10, fill="black", width=4)
linea18=c.create_line(290,ALTURA-60,290,ALTURA-10, fill="black", width=4)

ventana_principal.mainloop()