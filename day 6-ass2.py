##############SHAPES############

import math

class Cone:
    def __init__(self,Radius,Height):
        self.Radius = Radius
        self.Height = Height
        #self.Volume = Volume
        #self.Surface = Surface

    def Volume(self):
        Vol = (1/3) * math.pi * self.Radius*self.Radius*self.Height
        print("Volume of Cone is:", Vol)

    def Surface_area(self):
        SA = math.pi*self.Radius*(self.Radius + math.sqrt(self.Height + self.Radius))
        print("Surface area of cone is:", SA)

obj = Cone(4, 8)
obj.Volume()
obj.Surface_area()