import pygame
import random
import time
from multiprocessing import Process
from colorconsole import terminal
from threading import Thread
from GameMap import GameMap
from Camera import Camera
from Loader import Loader
from Tools import Vector2, Segment


screen = terminal.get_terminal()
screen.clear()
pygame.init()

class Runner():
	def __init__(self, actions, map_name):
		loaded_map = Loader(map_name)
		objects = loaded_map.objects
		self.initial_pos = loaded_map.player_pos
		self.initial_rotation = loaded_map.player_rotation

		screen.set_color(15, 0)
		self.camera = Camera(self.initial_pos, self.initial_rotation)
		self.camera.update_objects(objects)
		self.camera.update()
		self.map_ = self.camera.send_screen()

		self.actions = actions

	def print_map(self):
		screen.gotoXY(1, 1)
		for y in range(len(self.map_)):
			print()
			for x in range(len(self.map_[y])):
				print(self.map_[y][x], end='')

	def update(self):
		self.handle_input()
		self.player_movement()

		self.camera.update()
		self.map_ = self.camera.send_screen()
		self.print_map()

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					screen.gotoXY(1, 57)
					quit()
				if event.key == pygame.K_a:
					self.actions.add("left")
				if event.key == pygame.K_s:
					self.actions.add("back")
				if event.key == pygame.K_w:
					self.actions.add("forward")
				if event.key == pygame.K_d:
					self.actions.add("right")

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					self.actions.remove("left")
				if event.key == pygame.K_s:
					self.actions.remove("back")
				if event.key == pygame.K_w:
					self.actions.remove("forward")
				if event.key == pygame.K_d:
					self.actions.remove("right")


	def player_movement(self):
		if self.actions.has("left"):
			self.camera.rotation.rotate(5)
		if self.actions.has("right"):
			self.camera.rotation.rotate(-5)
		if self.actions.has("back"):
			self.camera.move(-0.1)
		if self.actions.has("forward"):
			self.camera.move(0.1)


class CurrentActions():
	def __init__(self):
		self.actions = []

	def add(self, action):
		if not action in self.actions:
			self.actions.append(action)

	def remove(self, action):
		if action in self.actions:
			self.actions.remove(action)

	def has(self, action):
		if action in self.actions:
			return True
		return False

	def leave_only(self, action):
		self.actions = [action]


# if __name__ == "__main__":
# 	actions = CurrentActions()

# 	runner = Runner(actions)
# 	while True:	
# 		runner.update()
# 		time.sleep(0.01)








