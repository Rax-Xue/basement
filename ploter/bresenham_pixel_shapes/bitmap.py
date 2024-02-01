from collections import namedtuple
from copy import copy

Colour = namedtuple('Colour','r,g,b')
Colour.copy = lambda self: copy(self)

black = Colour(0,0,0)
white = Colour(255,255,255) # Colour ranges are not enforced.

class Bitmap():
	'''
	reference: https://rosettacode.org/wiki/Bitmap/Python
	
	Usage:
	bitmap = Bitmap(20,10)
	bitmap.fillrect(4, 5, 6, 3)
	assert bitmap.get(5, 5) == black
	assert bitmap.get(0, 1) == white
	bitmap.set(0, 1, black)
	assert bitmap.get(0, 1) == black
	bitmap.chardisplay()
	'''
	def __init__(self, width = 40, height = 40, background=white):
		assert width > 0 and height > 0 and type(background) == Colour
		self.width = width
		self.height = height
		self.background = background
		self.map = [[background.copy() for w in range(width)] for h in range(height)]

	def fillrect(self, x, y, width, height, colour=black):
		assert x >= 0 and y >= 0 and width > 0 and height > 0 and type(colour) == Colour
		for h in range(height):
			for w in range(width):
				self.map[y+h][x+w] = colour.copy()

	def chardisplay(self):
		txt = [''.join(' ' if bit==self.background else 'o'
					   for bit in row)
			   for row in self.map]
		# Boxing
		txt = ['|'+row+'|' for row in txt]
		txt.insert(0, '+' + '-' * self.width + '+')
		txt.append('+' + '-' * self.width + '+')
		print('\n'.join(reversed(txt)))

	def set(self, x, y, colour=black):
		assert type(colour) == Colour
		self.map[y][x]=colour

	def setarray(self,array:list,colour=black):
		'''
		array shape must be ()
		'''
		assert type(colour) == Colour
		for item in array:
			self.set(item[0],item[1])
 
	def get(self, x, y):
		return self.map[y][x]
	
	def resize(self,width:int,height:int):
		assert width > 0 and height > 0

		if height <=self.height:
			self.map = self.map[:height]
		if width <= self.width:
			self.map = [row[:width] for row in self.map]

		if width > self.width:
			self.map = [row + [self.background]*(width - self.width) for row in self.map]
		if height > self.height:
			self.map = self.map + [[self.background]*width]*(height-self.height)

		self.width = width
		self.height = height

	
	def superposition(self, layer, bias:(int,int)=(0,0)):
		'''
		layer overlain to self.map
		size sticks to self.map
		every bit in layer differs from self.background is accepted, 
		meaning some of the bits in self.map will be covered

		bias - offset to self.map origin
		'''
		assert type(layer) == Bitmap

		# cut extra part to always suit self.map
		lmap = layer.map
		if layer.height > self.height:
			lmap = lmap[:self.height]
		if layer.width > self.width:
			lmap = [x[:self.width] for x in lmap]
			
		for i,row in enumerate(lmap):
			for j,bit in enumerate(row):
				if bit != self.background:
					self.map[i+bias[0]][j+bias[1]] = bit

	def findrow(self,row:int,color:Colour=black)->list():
		'''
		find color item in given row
		row: 0 to height-1
		return: list containing column index of given color at given row
		'''
		assert row >= 0 and row < self.height
		res = list()
		for index, bit in enumerate(self.map[row]):
			if bit == color:
				res.append(index)
		
		return res
	
	def findcol(self,col:int,color:Colour=black)->list():
		'''
		return: list containing row index of given color at given column
		'''
		assert col >= 0 and col < self.width
		res = list()
		for index in range(self.height):
			bit = self.map[index][col]
			if bit == color:
				res.append(index)

		return res
