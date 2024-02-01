
from bresenham_pixel_shapes.bitmap import Bitmap
from bresenham_pixel_shapes.bresenhams_circle import Bresenhams_circle

def main():
    canvas = Bitmap(100,100)
    circle_drawer = Bresenhams_circle(canvas)
    circle_drawer.draw_ring((50,50),40,4)
    circle_drawer.plot()
    canvas.chardisplay()



if __name__ == '__main__':
    main()


