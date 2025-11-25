from graphics.rectfunction import RectArea
from graphics.cirFunction import CirArea
from graphics.Dgraphics.spherefuc import SpArea
from graphics.Dgraphics.cubfunction import CubPerimeter

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Rectangle Area =",RectArea(l, b))


r = int(input("Enter radius of Circle: "))
print("Circle Area =", CirArea(r))


r = int(input("Enter radius of Sphere: "))
print("Sphere Area =", SpArea(r))


l = int(input("Enter cuboid length: "))
b = int(input("Enter cuboid breadth: "))
h = int(input("Enter cuboid height: "))
print("Cuboid Perimeter =", CubPerimeter(l, b, h))
