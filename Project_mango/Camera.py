import math
from Tools import Vector2, Segment
from BetterRay import BetterRay
from Angle import Angle
from Ray import Ray


class Camera():
	def __init__(self, pos=Vector2(), rotation=Angle(),
		screen_size=Vector2(200, 55), fov=Vector2(120, 80)):
			self.pos = pos.cast()
			self.rotation = rotation
			self.fov = fov
			self.screen_size = screen_size.cast()
			self.screen = []
			self.objects = []
			self.initialize_screen()
			self.update()
						
	def initialize_screen(self):
		for y in range(self.screen_size.y):
			self.screen.append([])
			for x in range(self.screen_size.x):
				self.screen[y].append(" ")
				
	def send_screen(self):
		return self.screen
				
	def update_objects(self, objects):
		self.objects = objects
			
	def update(self):
		iter_ang = self.fov.x / self.screen_size.x
		for x in range(self.screen_size.x):
			current_angle = Angle(self.rotation.add(
				- iter_ang * x + self.fov.x / 2))
			direction = Vector2(math.cos(current_angle.rads) * 0.1,
			math.sin(current_angle.rads) * 0.1)
			# ray = Ray(self.pos, direction, 100, self.objects)
			ray = BetterRay(self.pos, direction, 100, self.objects)
			if ray.cast():
				brightness = 4 - (ray.distance + 1) / 2
			else:
				brightness = None

			if ray.distance:
				y_iter_ang = self.fov.y / self.screen_size.y
				for y in range(self.screen_size.y):
					vertical_angle = Angle(y_iter_ang * y - self.fov.y / 2)
					h = - (ray.distance) * math.tan(vertical_angle.rads) + 1.5
					if h >= 0 and h <= 2.5:
						if brightness:
							if brightness >= 4:
								self.screen[y][x] = "█"
							elif brightness >= 3:
								self.screen[y][x] = "▓"
							elif brightness >= 2.3:
								self.screen[y][x] = "▒"
							elif brightness >= 1:
								self.screen[y][x] = "░"
							else:
								self.screen[y][x] = "\'"
					else:
						self.screen[y][x] = " "
			else:
				for y in range(self.screen_size.y):
					self.screen[y][x] = " "

	def displace(self, direction):
		move = Segment(self.pos, self.pos.cast().add(direction))
		intersection = False
		for object_ in self.objects:
			if object_.intersects(move):
			# if move.intersects(object_):
				intersection = True
		if not intersection:
			self.pos.add(direction)
		return not intersection

	def move(self, magnitude, precision=10):
		direction = Vector2(math.cos(self.rotation.rads) * magnitude / precision,
			math.sin(self.rotation.rads) * magnitude / precision)
		for i in range(precision):
			if not self.displace(direction):
				break
		# self.pos.add(direction)
		
	def test_print(self):
		for y in range(len(self.screen)):
			print(".", end='')
			for x in range(len(self.screen[0])):
				print(self.screen[y][x], end='')
			print(".")
			
			

# █, ▓, ▒, ░,  
# 
