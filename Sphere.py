class Sphere():
    
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius=radius
        self.x=x
        self.y=y
        self.z=z

    def get_volume(self):
        return (4/3*3.141592653589*(self.radius**3))

    def get_square(self):
        return (4*3.141592653589*(self.radius**2))

    def get_radius(self):
        return (self.radius)

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, r):
        self.radius=r

    def set_center(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def is_point_inside(self,a,b,c):
        if abs(self.x)+abs(a)<=self.radius \
            and abs(self.y)+abs(b)<=self.radius \
                and abs(self.z)+abs(c)<=self.radius:
            return True
        else:
            return False
