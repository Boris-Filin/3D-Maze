import random
from Tools import Vector2


class Maze():
	def __init__(self, size=Vector2(7, 7)):
		self.size = size
		self.random_map()
		self.print_maze()
		self.generate_route()

	def generate_route(self):
		pos = Vector2(0, self.size.y-1)
		exit_pos = Vector2(self.size.x-1, 0)
		routes = []
		hasbeen = []
		for y in range(self.size.y):
			hasbeen.append([])
			for x in range(self.size.x):
				hasbeen[y].append(False)
		self.step(pos, exit_pos, hasbeen, routes, None, 0)

		route = random.choice(routes)
		print(len(routes))
		for offset in route:
			print(offset.x, offset.y)

	def step(self, pos, exit_pos, hasbeen, routes, route, i):
		if route == None:
			route = []
		if pos.matches(exit_pos):
			routes.append(route)
			return True
		else:
			new_hasbeen = self.cast_2d_arr(hasbeen)
			new_hasbeen[pos.y][pos.x] = True
			chosen = False
			offsets_left = [
				Vector2(-1, 0),
				Vector2(0, -1),
				Vector2(1, 0),
				Vector2(0, 1)
				]
			while not chosen:
				print(len(offsets_left))
				if len(offsets_left) == 0:
					return False
				offset = random.choice(offsets_left)
				offsets_left.remove(offset)
				if not self.out_of_bounds(Vector2(pos.x + offset.x, pos.y + offset.y)):
					if not hasbeen[pos.y][pos.x-1]:
						route_step = route.copy()
						route_step.append(offset)
						if self.step(pos.castadd(offset), exit_pos, new_hasbeen, routes, route_step, i + 1):
							self.chosen = True
							return True


				# offset = Vector2(-1, 0)				
				# if not self.out_of_bounds(Vector2(pos.x + offset.x, pos.y + offset.y)):
				# 	if not hasbeen[pos.y][pos.x-1]:
				# 		route_step = route.copy()
				# 		route_step.append(offset)
				# 		self.step(pos.castadd(offset), exit_pos, new_hasbeen, routes, route_step, i + 1)
				# offset = Vector2(0, -1)
				# if not self.out_of_bounds(Vector2(pos.x + offset.x, pos.y + offset.y)):
				# 	if not hasbeen[pos.y-1][pos.x]:
				# 		route_step = route.copy()
				# 		route_step.append(offset)
				# 		self.step(pos.castadd(offset), exit_pos, new_hasbeen, routes, route_step, i + 1)
				# offset = Vector2(1, 0)
				# if not self.out_of_bounds(Vector2(pos.x + offset.x, pos.y + offset.y)):
				# 	if not hasbeen[pos.y][pos.x+1]:
				# 		route_step = route.copy()
				# 		route_step.append(offset)
				# 		self.step(pos.castadd(offset), exit_pos, new_hasbeen, routes, route_step, i + 1)
				# offset = Vector2(0, 1)
				# if not self.out_of_bounds(Vector2(pos.x + offset.x, pos.y + offset.y)):
				# 	if not hasbeen[pos.y+1][pos.x]:
				# 		route_step = route.copy()
				# 		route_step.append(offset)
				# 		self.step(pos.castadd(offset), exit_pos, new_hasbeen, routes, route_step, i + 1)

	def cast_2d_arr(self, arr):
		arr_cast = []
		for y in range(len(arr)):
			arr_cast.append(arr[y].copy())
		return arr_cast

	def out_of_bounds(self, pos):
		if pos.x < 0 or pos.x >= self.size.x:
			return True
		if pos.y < 0 or pos.y >= self.size.y:
			return True
		return False

	def print_maze(self):
		for y in range(self.size.y):
			for x in range(self.size.x):
				print("+", end='')
				if y == 0:
					if self.map[y][x].n:
						print("---", end='')
					else:
						print("   ", end='')
				else:
					if self.map[y-1][x].s or self.map[y][x].n:
						print("---", end='')
					else:
						print("   ", end='')
			print("+")
			for x in range(self.size.x):
				if x == 0:
					if self.map[y][x].w:
						print("|", end='')
					else:
						print(" ", end='')
				else:
					if self.map[y][x].w or self.map[y][x-1].e:
						print("|", end='')
					else:
						print(" ", end='')
				print("   ", end='')
			if self.map[y][self.size.x-1].e:
				print("|")
			else:
				print(" ")
		for x in range(self.size.x):
			print("+", end='')
			if self.map[y][x].s:
				print("---", end='')
			else:
				print("   ", end='')
		print("+")

	def random_map(self):
		self.map = []
		for y in range(self.size.y):
			self.map.append([])
			for x in range(self.size.x):
				self.map[y].append(Cell(
					random.choice([False, True]),
					random.choice([False, True]),
					random.choice([False, True]),
					random.choice([False, True])))


class Cell():
	def __init__(self, n=False, s=False, e=False, w=False):
		self.n = n
		self.s = s
		self.e = e
		self.w = w

maze = Maze()
