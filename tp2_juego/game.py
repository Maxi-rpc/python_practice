### imports
import turtle
import sys
import os

# funcion para carpeta
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

### definir ratones

### definir gatos
gatos = {
    'tom': {
        'image': resource_path('resource/tom_caminando_mini.gif')
    } 
}

### config ventana
wn = turtle.Screen()
# titulo
wn.title('Juego de Tom y Jerry')
# size
wn.setup(width=600, height=600)
# background color
wn.bgcolor('light grey')

# load image
wn.addshape(gatos['tom']['image'])

cat = turtle.Turtle()
cat.speed(0)
cat.shape(gatos['tom']['image'])
cat.penup()
cat.goto(125,-220)

turtle.done()