import math


class Angle:
	def __init__(self, angle=0):
		self.angle = angle
		self.check()
		self.update_rads()

	def convert_from_rads(self, angle_in_rads):
		self.angle = angle_in_rads / math.pi * 180
		self.check()
		self.update_rads()
		return self.angle
		
	def check(self):
		if self.angle >= 360:
			self.angle -= 360
			self.check()
		if self.angle < 0:
			self.angle += 360
			self.check()
			
	def update_rads(self):
		if self.angle <= 180:
			self.rads = self.angle * math.pi / 180
		else:
			self.rads = (self.angle - 360) * math.pi / 180
		
	def rotate(self, angle):
		self.angle += angle
		self.check
		self.update_rads()
		
	def add(self, angle):
		return self.angle + angle
		
	def divide(self, times):
		return self.angle / times
		
	def multiply(self, times):
		return self.angle * times

