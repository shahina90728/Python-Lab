from graphics.rectfunction import*
from graphics.cirFunction import*
from graphics.Dgraphics.spherefuc import*
from graphics.Dgraphics.cubfunction import*


l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("Enter radius of circle:"))
print("Circle Area=",CirArea(r))
print("circle Perimeter=",CirPerimeter(r))


r = int(input("Enter radius of Sphere: "))
print("Sphere Area =", SpArea(r))
print("Sphere Volume =", SpPerimeter(r))

l = int(input("Enter cuboid length: "))
b = int(input("Enter cuboid breadth: "))
h = int(input("Enter cuboid height: "))
print("Cuboid Area =", CubArea(l, b, h))
print("Cuboid Perimeter =", CubPerimeter(l, b, h))
