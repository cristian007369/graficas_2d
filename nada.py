from tkinter import *

# crear el canvas
root = Tk()
c = Canvas(root, width=400, height=400)
c.pack()

# definir la función para la parábola
def parabola(x):
    return x ** 2

# definir los parámetros para la curva
x_min = -10
x_max = 10
n_points = 100
x_step = (x_max - x_min) / n_points

# graficar la curva de la parábola
x = x_min
y = parabola(x)
x_canvas = 200 + x * 20
y_canvas = 200 - y * 20
for i in range(n_points):
    x += x_step
    y = parabola(x)
    x_canvas_new = 200 + x * 20
    y_canvas_new = 200 - y * 20
    c.create_line(x_canvas, y_canvas, x_canvas_new, y_canvas_new, fill="blue")
    x_canvas, y_canvas = x_canvas_new, y_canvas_new

# iniciar el loop de tkinter
root.mainloop()
