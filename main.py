from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
#Setting new default styling
root.configure(bg=settings.BG1)
root.geometry(f"{settings.WIDTH}x{settings.HEIGTH}")
root.title("MineSweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg=settings.BG2,
    width= utils.width_prct(100),
    height= utils.height_prct(25)
)

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    text="Minesweeper Game",
    font=('', 48)
)

game_title.place(
    x=utils.width_prct(40),
    y=55

)
left_frame = Frame(
    root,
    bg=settings.BG3,
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)

left_frame.place(x=0,y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg=settings.BG1,
    width=utils.width_prct(75),
    height=utils.height_prct(75),
)
center_frame.place(
    x=utils.width_prct(40),
    y=utils.height_prct(31),
)

c1 = Cell(X,Y)
c1.create_btn_object(center_frame)
c1.cell_btn_object.grid(
    column=0, row=0
)

c2 = Cell(X,Y)
c2.create_btn_object(center_frame)
c2.cell_btn_object.grid(
    column = 1, row = 0
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y) 
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row= y
        )
Cell.randomize_mines()
#Call the label from Cell class

Cell.create_cell_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,
    y=0
)

#run the window
root.mainloop()


