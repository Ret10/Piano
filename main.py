from pygame import *
from effects import draw_key_effect
from keys import create_key_rects, draw_keys
window = display.set_mode((900,600))
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
display.update()
KEYS = {
    "a": "a6.mp3",
    "b": "b6.mp3",
    "c": "c6.mp3",
    "d": "d6.mp3",
    "f": "f6.mp3",
    "g": "g6.mp3",
    "e": "e6.mp3",
}
def draw keys(window, key rects, pressed_keys):
for i, rect in enumerate(key rects):
is pressed = i in pressed keys
draw_key_effect(window, rect, is_pressed)

def create key_rects(num_keys, start_x = 50, start_y = 100 , key_width = 100, key_hight = 250):
rects = []
for i in range(num keys):
x =  start x + i * key width
rects.append(Rect(x, start))
