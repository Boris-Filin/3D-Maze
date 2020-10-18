import math
from Tools import Vector2, Segment, MathRay


class BetterRay:
	def __init__(self, current_pos,
		direction, render_distance, objects=[]):
		self.current_pos = current_pos.cast()
		self.direction = direction.cast()
		self.render_distance = render_distance
		self.objects = objects
		self.intersected = False
		self.distance = None
		self.ray = MathRay(self.current_pos, direction)
		
	def cast(self):
		intersections = {}
		for object_ in self.objects:
			dist = self.ray.count_intersection(object_)
			if dist != None:
				if dist <= self.render_distance:
					intersections[dist] = object_
		if intersections:
			self.intersected = True
			self.distance = min(intersections)
		return self.intersected




