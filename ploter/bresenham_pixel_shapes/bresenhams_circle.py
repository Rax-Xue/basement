from bresenham_pixel_shapes.bitmap import *

import math

class Bresenhams_circle():

    def __init__(self, bitmap:Bitmap) -> None:
        self.bitmap = bitmap
        self.width = bitmap.width
        self.height = bitmap.height
        self.background = bitmap.background
        self.layers = list()
        pass

    def draw_circle(self, center:(int,int), radius:int,color:Colour=black):
        # create canvas
        layer = Bitmap(self.width, self.height,self.background)

        # start at the first octant from (0,R) to -(R√2, R√2), marching along x axis
        x = 0
        y = radius

        cx = center[0]
        cy = center[1]

        # accumulative error of drawing
        # next half point is (1,R-0.5)
        # delta = F(x + 1, y - 0.5)
        # the initial value is 1*1+(R-0.5)*(R-0.5)-R*R=1.25-R, where 1.25 rounded into integer 1
        delta = 1 - radius

        while(y>=x): # which will ends at -(R√2, R√2) to only cover the first octant
            # copying the same process into all eight octants to save computation
            layer.set(x+cx, y+cy,color)
            layer.set(y+cx,x+cy,color)
            layer.set(-x+cx, y+cy,color)
            layer.set(-y+cx,x+cy,color)
            layer.set(-x+cx,-y+cy,color)
            layer.set(-y+cx,-x+cy,color)
            layer.set(x+cx,-y+cy,color)
            layer.set(y+cx,-x+cy,color)

            if delta < 0: # the middle point error delta = F(x+1,y-0.5) < 0, no need to decrease y
                # next delta = F(x + 2, y - 0.5) = d + 2x + 3
                delta = delta + 2*x + 3
            else: # error > 0, y needs to decrease
                # next delta = F(x + 2, y - 1.5)  = (x + 2)^2 + (y - 1.5)^2 - R^2 
                # = (x + 1)^2 + (x - 0.5)^2 - R^2 + 2x + 3 - 2y + 2 = d + 2x - 2y + 5
                delta = delta + 2*(x-y)+5
                y -= 1
            x += 1

        self.layers.append(layer)
        return layer

    def draw_ring(self, center:(int,int), radius:int, thickness:int=1, color:Colour=black):
        '''
        no return, call plot/plot_to to draw it
        '''
        oc = self.draw_circle(center,radius,color) # outer circle
        r2 = radius - thickness + 1
        ic = self.draw_circle(center,r2,color) # inner circle

        layer = Bitmap(self.width, self.height,self.background)

        # fill the gaps
        for line in range(center[1]-radius,center[1]+radius):
            ocps = oc.findline(line,color)
            icps = ic.findline(line,color)

            if len(icps) == 0:
                for index in range(ocps[0],ocps[-1]):
                    layer.set(index,line,color)
            else:
                for index in range(ocps[0],icps[0]):
                    layer.set(index,line,color)
                for index in range(icps[-1],ocps[-1]):
                    layer.set(index,line,color)
            
        self.layers.append(layer)

    def draw_arc(self, center:(int,int), radius:int, start_angle:float, end_angle:float, thickness:int=1):
        if abs(start_angle) > 360:
            start_angle = start_angle % 360
        if abs(end_angle) > 360:
            end_angle = end_angle % 360
        sa_rad = math.radians(start_angle)
        ea_rad = math.radians(end_angle)

        
        pass

    def plot_to(self,bitmap:Bitmap):
        for layer in self.layers:
            bitmap.superposition(layer)

    def plot(self):
        self.plot_to(self.bitmap)
        


