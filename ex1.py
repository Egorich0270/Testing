class Point:
    color = 'red'
    circle = 2
    def set_coords(self,x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x,self.y)


a = Point()
a.set_coords(10,12)
print(a.get_coords())
