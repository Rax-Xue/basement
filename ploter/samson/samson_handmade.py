#! /usr/bin/python3

# a handmade samson drawer with only ring implemented

import tkinter as tk
import numpy as np
import math

def plot_ring_mask(mask:np.ndarray, center:[int,int], radius:int, thickness:int = 1):
    r = radius
    xn = center[0] - r
    yn = center[1] - r

    for layer in range(thickness):
        for x in range(r*2):
            # (x-r)^2 + (y-r)^2 = r^2
            y2 = r*r - (x-r)*(x-r)
            y = round(abs(math.sqrt(y2)))
            ya = y + r
            yb = -y + r

            mask[x+xn][ya+yn if ya+yn < 50 else 49] = 1 # upper circle
            mask[x+xn][yb+yn if yb+yn < 50 else 49] = 1 # lower circle

        xn = xn +1
        yn = yn +1
        r = r - 1


    return mask


def puncutation_canvas(mask:np.ndarray):
    canvas = list()

    for row in range(mask.shape[1]):
        line = str()
        for item in mask[:][row]:
            if item == 1:
                line += 'o'
            else:
                line += '.'

        canvas.append(line)

    return canvas


class Samson():
    def __init__(self, scale:int=100) -> None:
        self.scale = scale if scale > 0 else 0

        self.plot()
    def plot(self):
        self.mask = np.zeros((self.scale,self.scale))
        center = [self.scale//2,self.scale//2]
        plot_ring_mask(self.mask, center, self.scale//2)
        
        pass

    def show(self):
        self.draw = puncutation_canvas(self.mask)
        for line in self.draw:
            print(line)
        wd = tk.TK()
        tk.Canvas.create_oval()


def main():
    sam = Samson(50)
    sam.show()

if __name__ == '__main__':
    main()