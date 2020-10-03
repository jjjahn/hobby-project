from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import PIL


brush_color = ((0.0, 0.0, 0.0), '#000000')

def colorpicker():
    global brush_color
    brush_color = colorchooser.askcolor()
 
def eraser():
    global brush_color
    brush_color = ((255, 255, 255), '#ffffff')


def clearcanvas():
    canva.delete("all")
    draw.rectangle([(0,0),(910, 560)], fill = 'white', width = 0)

def savefile():
    filename = filedialog.asksaveasfile(mode = 'w', defaultextension = '.jpg', filetypes=[("JPG", ".jpg")])
    image1.save(filename)

def paint(event):
    global brush_color
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    canva.create_oval(x1, y1, x2, y2, fill = brush_color[1], width = 0)
    draw.ellipse((x1, y1, x2, y2), fill = brush_color[1], width = 0)


root = Tk()
root.geometry('960x600')
root.title("Start Drawing!")
canva = Canvas(root, height = 560, width = 910, bg = "white")
canva.pack(side = BOTTOM)


colorpick = Button(root, text = "Color", command = colorpicker)
colorpick.pack(side = LEFT)
erase = Button(root, text = "Eraser", command = eraser)
erase.pack(side = LEFT)
clear = Button(root, text = "Clear", command = clearcanvas)
clear.pack(side = LEFT)
save = Button(root, text = "Save", command = savefile)
save.pack(side = LEFT)


canva.pack(expand = YES, fill = BOTH)
canva.bind("<B1-Motion>", paint)

image1 = PIL.Image.new("RGB", (910, 560), "white")
draw = ImageDraw.Draw(image1)


root.mainloop()



