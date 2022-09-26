from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius=radius

    def calcArea(self):
        return 3.14*(self.radius**2)

    def toJSON(self):
        return f"{{\"circle\":{str(self.calcArea())} }}"

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side**2


#g1 = GraphicShape()
c1 = Circle(10)
s1 = Square(4)
print(c1.calcArea())
print(s1.calcArea())
print(c1.toJSON())