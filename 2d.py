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
"""
#lineas
linea1=c.create_line(10,10,BASE-10,10, fill="red",width=3)
linea2=c.create_line(BASE-10,10,BASE-10,ALTURA-10, fill="red",width=3)
linea3=c.create_line(BASE-10,ALTURA-10,10,ALTURA-10, fill="red",width=3)
linea4=c.create_line(10,ALTURA-10,10,10, fill="red",width=3)
linea5=c.create_line(10,10,BASE-10,ALTURA-10, fill="BLUE",width=3)
linea6=c.create_line(10,ALTURA-10,BASE-10,10, fill="BLUE",width=3)
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

# Textos 
texto1=c.create_text(BASE/2,ALTURA/2,text="Sistemas UIS Socorro",anchor="center",font=("Times new roman","20","bold"),fill="green",activefill="White")

# Cuadrados y rectangulos
rect1=c.create_rectangle(20,20,120,120, fill="blue",outline="red",width=3)

# poligonos 
poligono1=c.create_polygon(0,0,BASE/2,ALTURA/2,BASE,0,fill="purple", outline="red")
poligono2=c.create_polygon(0,ALTURA,BASE/2,ALTURA/2,BASE,ALTURA,fill="RED", outline="red")
poligono3=c.create_polygon(0,0,BASE/2,ALTURA/2,0,ALTURA,fill="GREEN", outline="red")
"""
poligono3=c.create_polygon(BASE/4,0,0,ALTURA/4,BASE/2,ALTURA/4,fill="GREEN", outline="red")
poligono4=c.create_polygon(0,ALTURA/4,BASE/4,ALTURA/2,BASE/2,ALTURA/4,fill="GREEN", outline="red")

poligono6=c.create_polygon(BASE/4,ALTURA/2,0,ALTURA-ALTURA/4,BASE/2,ALTURA-ALTURA/4,fill="GREEN", outline="red")
poligono5=c.create_polygon(BASE/4,ALTURA,0,ALTURA-ALTURA/4,BASE/2,ALTURA-ALTURA/4,fill="GREEN", outline="red")

poligono3=c.create_polygon(BASE-BASE/4,0,BASE/2,ALTURA/4,BASE,ALTURA/4,fill="GREEN", outline="red")
poligono4=c.create_polygon(BASE/2,ALTURA/4,BASE,ALTURA/4,BASE-BASE/4,ALTURA/2,fill="GREEN", outline="red")

mi_color="#ffffff"
poligono6=c.create_polygon(BASE-BASE/4,ALTURA,BASE/2,ALTURA-ALTURA/4,BASE,ALTURA-ALTURA/4,fill=mi_color, outline="red")
poligono5=c.create_polygon(BASE-BASE/4,ALTURA/2,BASE/2,ALTURA-ALTURA/4,BASE,ALTURA-ALTURA/4,fill="GREEN", outline="red")

#ovalos- circulo
elipse1=c.create_oval(BASE/2,ALTURA/2,BASE,ALTURA, fill="orange")

elipse1=c.create_oval(BASE/2-50,ALTURA/2-50,BASE/2+50,ALTURA/2+50, fill="orange")

# arcos 
arc1=c.create_arc(BASE/2-30,ALTURA/2-30,BASE/2+30,ALTURA/2+30,start=45,extent=270, fill="black")

elipse1=c.create_oval(BASE/4-50,ALTURA/4-50,BASE/4+50,ALTURA/4+50, fill="orange")
arc1=c.create_arc(BASE/4-50,ALTURA/4-50,BASE/4+50,ALTURA/4+50,start=45,extent=270, fill="black")
elipse2=c.create_oval(BASE*3/4-50,ALTURA/4-50,BASE*3/4+50,ALTURA/4+50, fill="orange")
arc1=c.create_arc(BASE*3/4-50,ALTURA/4-50,BASE*3/4+50,ALTURA/4+50,start=45,extent=270, fill="black")
elipse1=c.create_oval(BASE/4-50,ALTURA*3/4-50,BASE/4+50,ALTURA*3/4+50, fill="orange")
arc1=c.create_arc(BASE/4-50,ALTURA*3/4-50,BASE/4+50,ALTURA*3/4+50,start=45,extent=270, fill="black")
elipse2=c.create_oval(BASE*3/4-50,ALTURA*3/4-50,BASE*3/4+50,ALTURA*3/4+50, fill="black")
arc1=c.create_arc(BASE*3/4-50,ALTURA*3/4-50,BASE*3/4+50,ALTURA*3/4+50,start=45,extent=270, fill="white")


ventana_principal.mainloop()