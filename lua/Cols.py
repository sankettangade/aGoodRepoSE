import re

class Cols:

	def __init__ (self, names):

		self.name = names
		self.all = {}
		self.klass = None
		self.x = {}
		self.y = {}
		for i in range(0,len(names)):
			c,s = i,names[i]
			self.all[s] = c

			# Sorts the Num type here
			if(s[0].isupper() and not re.search(":$",s)):
				self.x[s] = c
			# Sorts for the columns to be skipped
			elif(re.search(":$",s)):
				continue
			#Sorts the Sym type here
			elif(s[0].islower()):
				self.y[s] = c
			# elif(re.search("!",s[-1])):
			# 	self.klass[s] = c
			# If needed to classify independent and dependent for testing.
			# elif(re.search("[!+−]",s)):
			# 	self.x[s] = c