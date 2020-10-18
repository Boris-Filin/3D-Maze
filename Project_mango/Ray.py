import math
from Tools import Vector2, Segment


class Ray:
	def __init__(self, current_pos,
		direction, render_distance, objects=[]):
		self.current_pos = current_pos.cast()
		self.direction = direction.cast()
		self.render_distance = render_distance
		self.current_iteration = 0
		self.objects = objects
		self.completed = False
		self.intersected = False
		self.distance = -1
		
	def iteration(self):
		self.current_iteration += 1
		if self.current_iteration > self.render_distance:
			self.completed = True
			return
		else:
			pos = Vector2(self.current_pos.x, self.current_pos.y)
			new_pos = self.current_pos.add(self.direction)
			segment = Segment(pos, new_pos)
			for object_ in self.objects:
				if segment.intersects(object_):
					self.completed = True
					self.intersected = True
					self.distance = self.current_iteration
					
	def cast(self):
		while not self.completed:
			self.iteration()
		return self.intersected
					




