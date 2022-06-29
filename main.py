from tkinter import *
import settings
from cell import Cell

root = Tk()
# Configuring the window
root.configure(bg='grey')
root.geometry(f'{359}x{396}')
root.title('Tic tac toe game')

center_frame = Frame(root,
                     bg='black',
                     width=359,
                     height=396
                     )
center_frame.place(x=0, y=0)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )

root.mainloop()