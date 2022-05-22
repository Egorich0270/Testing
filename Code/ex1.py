class Point:
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('удаление экземпляра', str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

a = Point(1 ,2)
print(a.get_coords())
a = 19
