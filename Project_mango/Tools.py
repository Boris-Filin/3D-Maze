import math
from Angle import Angle


class Vector2:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def castadd(self, new_vector):
		return Vector2(self.x + new_vector.x, self.y + new_vector.y)
		
	def add(self, new_vector):
		self.x += new_vector.x
		self.y += new_vector.y
		return self
		
	def cast(self):
		return Vector2(self.x, self.y)

	def multiply(self, value):
		return Vector2(self.x * value, self.y * value)

	def matches(self, new_vector):
		if self.x == new_vector.x and self.y == new_vector.y:
			return True
		return False

	def bearing(self, new_vector):
		resulting_angle = Angle()
		a = math.sqrt(self.x ** 2 + self.y ** 2)
		b = math.sqrt(new_vector.x ** 2 + new_vector.y ** 2)
		c = math.sqrt((new_vector.x - self.x) ** 2 + (new_vector.y - self.y) ** 2)
		resulting_angle.convert_from_rads(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
		return resulting_angle


class Equation:
	def __init__(self, a=0, b=0, c=0):
		self.a = a
		self.b = b
		self.c = c

	def make_equation(self, pos_a, pos_b):
		dx = pos_b.x - pos_a.x
		dy = pos_b.y - pos_a.y
		self.a = dy
		self.b = - dx
		if dx == 0:
			self.a = 1
			self.c = - pos_a.x
		elif dy == 0:
			self.b = 1
			self.c = - pos_a.y
		else:
			self.c = (pos_a.y - (dy / dx) * pos_a.x) * dx
		
	def intersects(self, other_equation):
		a1 = self.a
		b1 = self.b
		c1 = self.c
		a2 = other_equation.a
		b2 = other_equation.b
		c2 = other_equation.c
		if b1 == 0 and b2 == 0:
			if a1 != a2:
				return None
			else:
				return - c1
		elif b1 == 0:
			return - c1
		elif b2 == 0:
			return - c2
		else:
			if a1 * b2 - a2 * b1 == 0:
				return None
			x_intersect = - (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
			return x_intersect

	def count_intersection(self, other_equation, origin):
		a1 = self.a
		b1 = self.b
		c1 = self.c
		a2 = other_equation.a
		b2 = other_equation.b
		c2 = other_equation.c
		intersection = None
		if b1 == 0 and b2 == 0:
			if a1 != a2:
				intersection = None
			else:
				intersection = Vector2(- c1, origin.y)
		elif b1 == 0:
			intersection = Vector2(- c1, (- c2 + a2 * c1) / b2)
		elif b2 == 0:
			intersection = Vector2(- c2, (- c1 + a1 * c2) / b1)
		elif a1 == 0 and a2 == 0:
			intersection = None
		else:
			if a1 * b2 - a2 * b1 == 0:
				intersection = None
			else:
				x_intersect = - (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
				intersection = Vector2(x_intersect, (c1 + a1 * x_intersect) / (- b1))
		return intersection
		
	def print_self(self):
		print(">>>: " + str(self.a) + "x + " + str(self.b) + "y + " + str(self.c))

class Segment():
	def __init__(self, pos_a, pos_b):
		self.pos_a = pos_a
		self.pos_b = pos_b
		if self.pos_a.x > self.pos_b.x:
			self.pos_a, self.pos_b = self.pos_b, self.pos_a
		self.equation = Equation()
		self.equation.make_equation(pos_a, pos_b)
		self.direction = Vector2(pos_a.x - pos_b.x, pos_a.y - pos_b.y)

	def set_vertices(self, new_pos_a, new_pos_b):
		self.pos_a = new_pos_a
		self.pos_b = new_pos_b
		self.equation.make_equation(pos_a, pos_b)
		self.direction = Vector2(pos_a.x - pos_b.x, pos_a.y - pos_b.y)
	
	def includes(self, pos):
		a = self.equation.a
		b = self.equation.b
		c = self.equation.c
		x = pos.x
		y = pos.y
		d = (a * x + b * y + c) / math.sqrt(a ** 2 + b ** 2)
		if abs(d) < 0.5 and (self.pos_a.x <= x and self.pos_b.x >= x):
			return True
		else:
			return False

	def intersects_old(self, other_segment):
		x = self.equation.intersects(other_segment.equation)
		if x == None:
			return False
		if (self.pos_a.x <= x and x <= self.pos_b.x) and (
			other_segment.pos_a.x <= x and x <= other_segment.pos_b.x):
				return True
		return False

	def intersects(self, other_segment):
		intersection = self.equation.count_intersection(other_segment.equation, self.pos_a)
		if intersection != None:
			if self.has_point(intersection) and other_segment.has_point(intersection):
				return True
		return False

	def has_point(self, pos):
		if self.pos_a.x <= pos.x and pos.x <= self.pos_b.x:
			if self.pos_a.x == self.pos_b.x:
				 if (self.pos_a.y <= pos.y and pos.y <= self.pos_b.y) or (self.pos_b.y <= pos.y and pos.y <= self.pos_a.y):
				 	return True
				 else:
				 	return False
			else:
				return True
		else:
			return False

class MathRay():
	def __init__(self, pos, direction):
		self.pos = pos
		self.equation = Equation()
		self.make_equation(direction)
		self.pointing = Vector2(self.sign(direction.x), self.sign(direction.y))

	def make_equation(self, direction):
		endpoint = self.pos.cast().add(direction)
		if endpoint.x < self.pos.x:
			self.equation.make_equation(endpoint, self.pos)
		else:
			self.equation.make_equation(self.pos, endpoint)

	def count_intersection(self, segment):
		intersection = self.equation.count_intersection(segment.equation, self.pos)
		if intersection != None:
			if self.if_matches(intersection) and segment.has_point(intersection):
				dist = math.sqrt((intersection.x - self.pos.x) ** 2 + (intersection.y - self.pos.y) ** 2)
				return dist
			else:
				return None
		else:
			return None

	def if_matches(self, new_pos):
		if self.pointing.x == 1:
			if self.pointing.y == 1:
				if new_pos.x >= self.pos.x and new_pos.y >= self.pos.y:
					return True
				else:
					return False
			elif self.pointing.y == 0:
				if new_pos.x >= self.pos.x:
					return True
				else:
					return False
			else:
				if new_pos.x >= self.pos.x and new_pos.y <= self.pos.y:
					return True
				else:
					return False
		elif self.pointing.x == 0:
			if self.pointing.y == 1:
				if new_pos.y >= self.pos.y:
					return True
				else:
					return False
			elif pointing.y == 0:
				return False
			else:
				if new_pos.y <= self.pos.y:
					return True
				else:
					return False
		else:
			if self.pointing.y == 1:
				if new_pos.x <= self.pos.x and new_pos.y >= self.pos.y:
					return True
				else:
					return False
			elif self.pointing.y == 0:
				if new_pos.x <= self.pos.x:
					return True
				else:
					return False
			else:
				if new_pos.x <= self.pos.x and new_pos.y <= self.pos.y:
					return True
				else:
					return False

	def sign(self, x):
		if x < 0:
			return - 1
		elif x == 0:
			return 0
		else:
			return 1

# v1 = Vector2(1, 0)
# v2 = Vector2(1, 1)
# print(v1.bearing(v2).angle)





			

