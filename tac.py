import tkinter as tk
import numpy as np

def on_click(row, col):
    #toggle cell value when clicked
    if grid[row][col] == 0:
        grid[row][col] = 1
    else:
        grid[row][col] = 0
    update_grid()

def update_grid():
#update grid values based on values in grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                tk.canvas.itemconfig(cells[i][j], fill = 'black')
            else:
                tk.Canvas.itemconfig(cells[i][j], fill = 'white')

#define grid dimensions
rows = 3
cols = 3

#initialise grid with zeros
grid = [[0] * cols for _ in range(rows)]

#Create main window
root = tk.Tk()
root.title("Clickable grid")

#Create Canvas
canvas = tk.Canvas(root, width = cols*30, height = rows * 30, bg = 'white')
canvas.pack()


#Create grid cells
cells = [[None] * cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        x0 = i *30
        y0 = j *30
        x1 = x0 + 30
        y1 = y0 + 30
        cells[i][j] = canvas.create_rectangle(x0, y0, x1, y1, outline = 'black', fill = 'white')
        canvas.tag_bind(cells[i][j], '<Button-1>', lambda event, row = i, col = j: on_click(row,col))
root.mainloop()
