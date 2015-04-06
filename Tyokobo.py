import random
class Object:
	def __init__(self):
		print 'hoge'
		
	def randx(self):
		x = random.randint(1,100)
		return(x)

	def randy(self):
		y = random.randint(1,100)
		return(y)

