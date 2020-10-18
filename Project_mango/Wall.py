from Tools import Segment
import math


class Segment():
	def __init__(self, pos_a, pos_b, height=3):
		self.pos_a = pos_a
		self.pos_b = pos_b
		self.height = height
		self.plane = Segment(pos_a, pos_b)
		
	