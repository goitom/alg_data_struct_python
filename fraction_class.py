def gcd(m, n):
	while m%n !=0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

class Fraction:

	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def __add__(self, otherfrac):
		newnum = self.num*otherfrac.den+otherfrac.num*self.den
		newden = self.den*otherfrac.den
		common = gcd(newnum, newden)
		return Fraction(newnum/common, newden/common)

	def __eq__(self, other):
		firstnum = self.num*other.den
		secondnum = other.num*self.den

		return firstnum==secondnum

myfraction = Fraction(3,5)
otherfraction = Fraction(1,5)