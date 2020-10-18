import pygame
import random
import time
import os
from multiprocessing import Process
from colorconsole import terminal
from threading import Thread
from Runner import Runner
from Tools import Vector2, Segment


screen = terminal.get_terminal()
screen.clear()
pygame.init()

class MainMenuRunner():
	def __init__(self, actions, size=Vector2(200, 55)):
		screen.set_color(15, 0)
		self.actions = actions
		self.size = size
		self.stage = 0
		self.map = []
		self.fill_map_stage0()
		self.pointer_pos = 0

	def print_map(self):
		screen.gotoXY(1, 1)
		for y in range(self.size.y):
			print()
			for x in range(self.size.x):
				print(self.map[y][x], end='')


	def fill_map_stage0(self):
		self.map = []
		for y in range(self.size.y):
			self.map.append([])
			for x in range(self.size.x):
				if y == 0 or y == self.size.y - 1 or x == 0 or x == self.size.x - 1:
					self.map[y].append("█")
				else:
					self.map[y].append(" ")
		self.put_string("Please resize your screen so that the white outline looks like a rectangle", Vector2(100, 25), True)
		self.put_string("Press SPACE when ready", Vector2(100, 27), True)
		self.put_string("The project is dedicated to Dmitry Filin!", Vector2(100, 15), True)
		self.put_string("HAPPY BIRTDAY! =D", Vector2(100, 17), True)

	def fill_map_stage1(self):
		for y in range(self.size.y):
			for x in range(self.size.x):
				if y == 0 or y == self.size.y - 1 or x == 0 or x == self.size.x - 1:
					self.map[y][x] = "█"
				else:
					self.map[y][x] = " "
		self.put_string("Choose level:", Vector2(100, 5), True)
		self.put_string("(Use ARROW UP or ARROW DOWN to navigate, press SPACE when ready)", Vector2(100, 7), True)
		self.put_string("Use ESC to quit", Vector2(100, 48), True)
		self.put_string("Use W, S to move around", Vector2(100, 50), True)
		self.put_string("Use A, D to rotate the camera", Vector2(100, 52), True)
		for l in self.levels:
			if not ".txt" in l:
				self.levels.remove(l)
		for i in range(len(self.levels)):
			height =  12 + i * 3 - self.pointer_pos * 3
			if height <= 10:
				self.put_string(" . . . ", Vector2(100, 10), True)
			elif height >= 45:
				self.put_string(" . . . ", Vector2(100, 45), True)				
			else:
				if i == self.pointer_pos:
					self.put_string("===>   -= " + self.levels[i].replace(".txt", "") + " =-   <===", Vector2(100, height), True)
				else:
					self.put_string("-= " + self.levels[i].replace(".txt", "") + " =-", Vector2(100, height), True)

	def put_string(self, s, pos, centered=False):
		for i in range(len(s)):
			try:
				if centered:
					self.map[pos.y][pos.x - len(s) // 2 + i] = s[i]
				else:
					self.map[pos.y][pos.x + i] = s[i]
			except:
				pass

	def update(self):
		if not self.stage == 2:
			self.handle_input()
			self.print_map()
		if self.stage == 0:
			if self.actions.has("continue"):
				self.stage = 1
				self.actions.clear()
				self.levels = os.listdir("Custom_Maps")
				self.fill_map_stage1()
		if self.stage == 1:
			if self.actions.has("up") and self.pointer_pos > 0:
				self.pointer_pos -= 1
				self.actions.remove("up")
				self.fill_map_stage1()
			if self.actions.has("down") and self.pointer_pos < len(self.levels) - 1:
				self.pointer_pos += 1
				self.actions.remove("down")
				self.fill_map_stage1()
			if self.actions.has("continue"):
				self.actions.clear()
				self.game_runner = Runner(self.actions, self.levels[self.pointer_pos])
				self.stage = 2
		if self.stage == 2:
			self.game_runner.update()

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					screen.gotoXY(1, 57)
					quit()
			if self.stage == 0:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.actions.add("continue")
			if self.stage == 1:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.actions.add("up")
					if event.key == pygame.K_DOWN:
						self.actions.add("down")
					if event.key == pygame.K_SPACE:
						self.actions.add("continue")


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

	def clear(self):
		self.actions = []


if __name__ == "__main__":
	actions = CurrentActions()

	runner = MainMenuRunner(actions)
	while True:	
		runner.update()
		time.sleep(0.03)




# █, ▓, ▒, ░,  




