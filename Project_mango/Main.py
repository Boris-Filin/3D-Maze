import random
import time
from colorconsole import terminal
from threading import Thread
from GameMap import GameMap


screen = terminal.get_terminal()
screen.clear()

def iter():
	map_ = []
	for y in range(8):
		map_.append([])
		for x in range(8):
			map_[y].append(random.randint(0, 3))
	return map_
	
def detect_intersection(map_):
	if map_.walls[0].intersects(map_.walls[1]):
		screen.print_at(2, 22, "Intersection!")
	
def print_map(map_):
	for y in range(len(map_)):
		for x in range (len(map_[y])):
			screen.print_at(2 * (x + 1), y + 1, map_[y][x])

def cursor_locker():
	while True:
		screen.gotoXY(0, 20)

def m():
	while True:
		if screen.getche() == "d":
			screen.print_at(0, 21, "!")

	
def runner():
	map_ = GameMap()
	while True:
#		map_ = iter()
		detect_intersection(map_)
		print_map(map_.get_map())
		time.sleep(0.1)

	
def main():
	thread1 = Thread(target = runner)
	thread2 = Thread(target = cursor_locker)
	mT = Thread(target = m)
	thread1.start()
	thread2.start()
#	mT.start()

if __name__ == "__main__":
	main()









