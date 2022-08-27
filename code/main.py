class Operations:
	def calculator(swi, n1, n2):
		if swi == 1:
			return (n1+n2)
		elif swi == 2:
			return (n1-n2)
		elif swi == 3:
			return (n1*n2)
		elif swi == 4:
			if n2 == 0:
				return ("Error denominator can not be zero")
			else:
				return (n1/n2)
		return "EXITING..."
