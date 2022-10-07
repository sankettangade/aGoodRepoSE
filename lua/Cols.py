import re
import Num
import Sym

class Cols:

	def __init__ (self, names):

		self.name = names
		self.all = {}
		self.klass = None
		self.x = {}
		self.y = {}
		for i in range(0,len(names)):
			c,s = i,names[i]
			# Sorts for the columns to be skipped
			if(s[0].isupper()):
				self.all[s] = [c,Num.Num(c,s)]
			#Sorts the Sym type here
			elif(s[0].islower()):
				self.all[s] = [c,Sym.Sym(c,s)]

			if (not re.search(":$", s)):
				if(re.search("[!+-]",s)):
					print("In Y:", s)
					self.y[s] = self.all[s]
				else:
					print("In X:", s)
					self.x[s] = self.all[s]
			if(re.search("!$",s)):
				self.klass = self.all[s]
