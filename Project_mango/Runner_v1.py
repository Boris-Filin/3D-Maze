import random
import time
from colorconsole import terminal
from threading import Thread
from GameMap import GameMap
from Camera import Camera
from Tools import Vector2, Segment


screen = terminal.get_terminal()
screen.clear()

class Runner1():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		self.map_parts = []
		if parts > 1:
			self.separate_map(parts)

		self.create_threads()
		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		for y in range(len(self.map_)):
			for x in range(len(self.map_[y])):
				screen.print_at(x, len(self.map_) - y - 1, self.map_[y][x])

	def update(self):
		self.camera.rotation.rotate(-10)
		self.map_ = self.camera.send_screen()
		for piece in self.map_parts:
			piece.update(self.map_)
		# self.print_map()
		# self.camera.update()
		# self.camera.test_print()

	def create_threads(self):
		for i in range(len(self.map_parts)):
			new_drawing_thread = Thread(target = self.handle_a_piece_of_map, args=[self.map_parts[i], 0.01])
			new_drawing_thread.start()
		# self.handle_a_piece_of_map(self.map_parts[0], 0.01)

	def separate_map(self, parts):
		x_step = len(self.map_[0]) // parts
		y_step = len(self.map_) // parts
		for i in range(parts):
			for j in range(parts):
				new_piece = []
				
				lower_border = i * y_step
				left_border = j * x_step

				if i < parts - 1:
					upper_border = (i + 1) * y_step
				else:
					upper_border = len(self.map_) - 1

				if j < parts - 1:
					right_border = (j + 1) * x_step
				else:
					right_border = len(self.map_[0]) - 1

				for y in range(lower_border, upper_border):
					new_piece.append([])
					for x in range(left_border, right_border):

						# screen.print_at(5, 5, y)

						new_piece[y - lower_border].append(self.map_[y][x])

				self.map_parts.append(Map_Reference(new_piece, left_border, lower_border))

	def handle_a_piece_of_map(self, map_reference, delay):
		i = 0
		while True:
			map_ = map_reference.map_
			x0 = map_reference.x
			y0 = map_reference.y
			for y in range(len(map_)):
				for x in range(len(map_[0])):
					screen.print_at(x0 + x, y0 + y, map_[y][x])
					# screen.print_at(x0, y0, i)
			i += 1


# class Controls1():
class Runner2():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		self.map_parts = []
		if parts > 1:
			self.separate_map(parts)

		self.create_threads()
		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		for y in range(len(self.map_)):
			for x in range(len(self.map_[y])):
				screen.print_at(x, len(self.map_) - y - 1, self.map_[y][x])

	def update(self):
		self.camera.rotation.rotate(-2)
		self.camera.update()
		self.map_ = self.camera.send_screen()
		for piece in self.map_parts:
			piece.update(self.map_)
		self.create_threads()
		# self.print_map()
		# self.camera.update()
		# self.camera.test_print()

	def create_threads(self):
		threads = []
		for i in range(len(self.map_parts)):
			new_drawing_thread = Thread(target = self.handle_a_piece_of_map, args=[self.map_parts[i]])
			threads.append(new_drawing_thread)
			new_drawing_thread.start()
		for thread in threads:
			thread.join()
		# self.handle_a_piece_of_map(self.map_parts[0], 0.01)

	def separate_map(self, parts):
		x_step = len(self.map_[0]) // parts
		y_step = len(self.map_) // parts
		for i in range(parts):
			for j in range(parts):
				new_piece = []
				
				lower_border = i * y_step
				left_border = j * x_step

				if i < parts - 1:
					upper_border = (i + 1) * y_step
				else:
					upper_border = len(self.map_) - 1

				if j < parts - 1:
					right_border = (j + 1) * x_step
				else:
					right_border = len(self.map_[0]) - 1

				for y in range(lower_border, upper_border):
					new_piece.append([])
					for x in range(left_border, right_border):

						# screen.print_at(5, 5, y)

						new_piece[y - lower_border].append(self.map_[y][x])

				self.map_parts.append(Map_Reference(new_piece, left_border, lower_border))

	def handle_a_piece_of_map(self, map_reference):
		map_ = map_reference.map_
		x0 = map_reference.x
		y0 = map_reference.y
		for y in range(len(map_)):
			for x in range(len(map_[0])):
				screen.print_at(x0 + x, y0 + y, map_[y][x])


class Map_Reference():
	def __init__(self, map_, x, y):
		self.map_ = map_
		self.x = x
		self.y = y

	def update(self, new_map):
		for y in range(len(self.map_)):
			for x in range(len(self.map_[y])):
				current_x = self.x + x
				current_y = self.y + y
				self.map_[y][x] = new_map[current_y][current_x]

class Runner3():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		for y in range(len(self.map_)):
			screen.print_at(1, len(self.map_) - y - 1, "")
			for x in range(len(self.map_[y])):
				print(self.map_[y][x], end='')

	def update(self):
		self.camera.rotation.rotate(-2)
		self.map_ = self.camera.send_screen()
		self.print_map()
		# self.camera.update()
		# self.camera.test_print()


class Runner3():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		for y in range(len(self.map_)):
			screen.print_at(1, len(self.map_) - y - 1, "")
			for x in range(len(self.map_[y])):
				print(self.map_[y][x], end='')

	def update(self):
		self.camera.rotation.rotate(-2)
		self.map_ = self.camera.send_screen()
		self.print_map()
		# self.camera.update()
		# self.camera.test_print()


class Runner3():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		# for y in range(len(self.map_)):
		#	 screen.print_at(1, len(self.map_) - y - 1, "")
		#	 for x in range(len(self.map_[y])):
		#		 print(self.map_[y][x], end='')
		char_map, num_map = convert_map()

	def convert_map(self):
		resulting_char_map = []
		resulting_num_map = []
		for y in range(len(self.map_)):
			resulting_char_map.append([])
			resulting_num_map.append([])
			previous_symbol = None
			i = -1
			for x in range(len(self.map_[y])):
				if self.map_[y][x] != previous_symbol:
					previous_symbol = map_[y][x]
					resulting_char_map[y].append(map_[y][x])
					resulting_num_map[y].append(1)
					i += 1
				else:
					resulting_num_map[y][i] += 1
		return resulting_char_map, resulting_num_map

	def update(self):
		self.camera.rotation.rotate(-2)
		self.map_ = self.camera.send_screen()
		self.print_map()
		# self.camera.update()
		# self.camera.test_print()


class Runner4():
	def __init__(self, parts=1):
		objects = [Segment(Vector2(-10, 1), Vector2(5, 1))]
		objects.append(Segment(Vector2(-10, -1), Vector2(3, -1)))
		objects.append(Segment(Vector2(5, 1), Vector2(5, -2)))
		# objects = [Segment(Vector2(0, 2), Vector2(-1, 2))]
		self.camera = Camera()
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		# self.camera.test_print()

	def print_map(self):
		self.camera.update()
		self.map_ = self.camera.send_screen()
		screen.gotoXY(1, 1)
		self.camera.test_print()
		# for y in range(len(self.map_)):
		#	 screen.print_at(1, len(self.map_) - y - 1, "")
		#	 for x in range(len(self.map_[y])):
		#		 print(self.map_[y][x], end='')

	def update(self):
		self.camera.rotation.rotate(-2)
		self.map_ = self.camera.send_screen()
		self.print_map()
		# self.camera.update()
		# self.camera.test_print()

if __name__ == "__main__":
	runner = Runner4(4)
	while True:	
		runner.update()

# def cursor_locker():
#	 while True:
#		 screen.gotoXY(0, 20)









