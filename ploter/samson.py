
from bresenham_pixel_shapes import bresenhams_circle, bitmap

def main():
    canvas = bitmap.Bitmap(100,100)
    circle_drawer = bresenhams_circle.Bresenhams_circle(canvas)
    circle_drawer.draw_ring((50,50),40,4)
    circle_drawer.plot()
    canvas.chardisplay()



if __name__ == '__main__':
    main()


