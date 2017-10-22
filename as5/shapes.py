from math import pi

class Point(object):

	def __init__(self, x=0.0, y=0.0):
		self.x = float(x)
		self.y = float(y)
	def __str__(self):
		return '({0:.1f}, {1:.1f})'.format(self.x, self.y)

	def translate(self, dx=0.0, dy=0.0):
		self.x += dx
		self.y += dy

	def dist(self, pb):
		return ((self.x -pb.x)**2 + (self.y - pb.y)**2)**(1/2)

class Ellipse(object):

	def __init__(self, center, x, y):
		self.center = center
		self.x_extent = float(x)
		self.y_extent = float(y)

	def __str__(self):
		return 'Ellipse with Center: {0}; Width: {1:.1f}; Height: {2:.1f}'.format(self.center, self.y_extent*2, self.x_extent*2)

	def translate(self, dx=0.0, dy=0.0):
		self.center.translate(dx, dy)

	def get_area(self):
		return pi*(self.x_extent**2 + self.y_extent**2)

pa = Point(5, 5)
pb = Point(8, 2)
pa.translate(-4.0,-4.0)
print('Distance = {0:.1f}'.format(pa.dist(pb)))
print(pa)
print('{0:.1f}'.format(pa.x))

P = Point(1.0, 3.0)
E = Ellipse(P, 2.3, 1.2)
print(E)
print(E.get_area())