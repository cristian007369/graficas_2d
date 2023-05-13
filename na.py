import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Dibujar el frente del cubo
canvas.create_polygon(50, 50, 150, 50, 150, 150, 50, 150, fill='red', outline='black')
# Dibujar la parte superior del cubo
canvas.create_polygon(50, 50, 100, 25, 200, 25, 150, 50, fill='blue', outline='black')
# Dibujar el lado derecho del cubo
canvas.create_polygon(150, 50, 200, 25, 200, 125, 150, 150, fill='green', outline='black')

root.mainloop()
import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Dibujar el frente del cubo
front = canvas.create_polygon(50, 50, 150, 50, 150, 150, 50, 150, fill='red', outline='black')
# Dibujar la parte superior del cubo
top = canvas.create_polygon(50, 50, 100, 25, 200, 25, 150, 50, fill='blue', outline='black')
# Dibujar el lado derecho del cubo
right = canvas.create_polygon(150, 50, 200, 25, 200, 125, 150, 150, fill='green', outline='black')

# Animar el cubo
for i in range(100):
    canvas.move(front, 1, 0)
    canvas.move(top, 1, 0)
    canvas.move(right, 1, 0)
    root.update()
    time.sleep(0.05)

root.mainloop()


