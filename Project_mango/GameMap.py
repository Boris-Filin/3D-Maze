import random
from Tools import Vector2, Segment
#from Wall import Segment

class GameMap:
	def __init__(self):
		self.num_of_walls = 2
		self.walls = []
		self.map_ = self.generate_map(Vector2(20, 20))
		self.generate_walls()
		self.paint_map()

	
	def generate_map(self, size):
		map_=[]
		for y in range(size.y):
			map_.append([])
			for x in range(size.x):
				map_[y].append(" ")
		return map_

	def generate_walls(self):
		for i in range(self.num_of_walls):
			size = Vector2(len(self.map_[0]), len(self.map_))
			a = Vector2(random.randint(0, size.x), random.randint(0, size.y))
			b = Vector2(random.randint(0, size.x), random.randint(0, size.y))
			self.walls.append(Segment(a, b))
		
	def paint_map(self):
		for y in range(len(self.map_)):
			for x in range(len(self.map_[y])):
				for wall in self.walls:
					if wall.includes(Vector2(x, y)):
						self.map_[y][x] = "#"
						
	def get_map(self):
		return self.map_
