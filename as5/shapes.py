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

	def __init__(self, center, x=0.0, y=0.0):
		self.center = center
		self.x_extent = float(x)
		self.y_extent = float(y)

	def __str__(self):
		return 'Ellipse with Center: {0}; Width: {1:.1f}; Height: {2:.1f}'.format(self.center, self.y_extent*2, self.x_extent*2)

	def translate(self, dx=0.0, dy=0.0):
		self.center.translate(dx, dy)

	def get_area(self):
		return pi*(self.x_extent**2 + self.y_extent**2)

def getEllipse():
	x = float(input('Enter Ellipse Center X Point: '))
	y = float(input('Enter Ellipse Center Y Point: '))
	xe = float(input('Enter Ellipse X Extent: '))
	ye = float(input('Enter Ellipse Y Extent: '))
	return Ellipse(Point(x,y), xe, ye)

class Circle(Ellipse):

	def __str__(self):
		return 'Circle with Center: {0}; Radius: {1:.1f};'.format(self.center, self.x_extent)

	def contains(self, other):
		d = ((self.center.x - other.center.x)**2 + (self.center.y - other.center.y)**2)**(1/2)
		if other.x_extent + d < self.x_extent:
			return True
		else:
			return False

def getCircle():
	x = float(input('Enter Circle Center X Point: '))
	y = float(input('Enter Circle Center Y Point: '))
	r = float(input('Enter Circle Radius: '))
	return Circle(Point(x,y), r)

if __name__ == "__main__":
	circle1 = getCircle()
	circle2 = getCircle()
	print(circle1)
	print(circle2)
	print('cirlce 1 area = %.1f' % circle1.get_area())
	print('cirlce 2 area = %.1f' % circle2.get_area())
	print(circle1.contains(circle2))
	print(circle2.contains(circle1))