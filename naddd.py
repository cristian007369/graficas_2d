import tkinter as tk
import math
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Coordenadas iniciales del cubo
coords = [[-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],
          [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]]

# Función para rotar puntos en el espacio 3D
def rotate(points, angle_x, angle_y):
    new_points = []
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        # Rotar en el eje X
        new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
        new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
        y = new_y
        z = new_z
        # Rotar en el eje Y
        new_x = x * math.cos(angle_y) + z * math.sin(angle_y)
        new_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
        x = new_x
        z = new_z
        new_points.append([x, y, z])
    return new_points

# Función para dibujar el cubo
def draw_cube(points):
    # Dibujar el frente del cubo
    canvas.create_polygon(points[0][0] + 200, points[0][1] + 200,
                          points[1][0] + 200, points[1][1] + 200,
                          points[2][0] + 200, points[2][1] + 200,
                          points[3][0] + 200, points[3][1] + 200,
                          fill='red', outline='black')
    # Dibujar la parte superior del cubo
    canvas.create_polygon(points[0][0] + 200, points[0][1] + 200,
                          points[4][0] + 200, points[4][1] + 200,
                          points[5][0] + 200, points[5][1] + 200,
                          points[1][0] + 200, points[1][1] + 200,
                          fill='blue', outline='black')
    # Dibujar el lado derecho del cubo
    canvas.create_polygon(points[1][0] + 200, points[1][1] + 200,
                          points[5][0] + 200, points[5][1] + 200,
                          points[6][0] + 200, points[6][1] + 200,
                          points[2][0] + 200, points[2][1] + 200,
                          fill='green', outline='black')
    # Dibujar la parte trasera del cubo
    canvas.create_polygon(points[4][0] + 200, points[4][1] + 200,
                          points[5][0] + 200, points[5][1] + 200,
                          points[6][0] + 200, points[6][1] + 200,
                          points[7][0] + 200, points[7][1] + 200,
                          fill='yellow', outline='black')
    # Dibujar la parte inferior del cubo
    canvas.create_polygon(points[3][0] + 200