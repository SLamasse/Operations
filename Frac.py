#!/usr/bin/env python3

import sys

class Frac(object):
	def __init__(self,n,d):
		self.n = n
		if d != 0:
			self.d = d
		else:
			raise ValueError('Division par 0')
		if self.d < 0:
			self.n = - self.n
			self.d = - self.d
		self.__reduction__()
			
	# affichage
	def __str__(self):
		if self.n == 0:
			return "0"
		elif self.d == 1:
			return str(self.n)
		else:
			return str(self.n)+"/"+str(self.d)

	# reduction de la fraction (Euclide)
	def __reduction__(self):
		a = abs(max(self.d,self.n))
		b = abs(min(self.d,self.n))
		while b != 0:
			tmp = b
			b = a % b
			a = tmp
		self.n = self.n // a
		self.d = self.d // a
		
	# surcharge addition
	def __add__(self,f):
		n = self.n * f.d + f.n * self.d
		d = self.d * f.d
		return Frac(n,d)

	# surcharge soustraction
	def __sub__(self,f):
		n = self.n * f.d - f.n * self.d
		d = self.d * f.d
		return Frac(n,d)
	
	# surcharge multiplication
	def __mul__(self,f):
		n = self.n * f.n
		d = self.d * f.d
		return Frac(n,d)
		
	# surcharge puissance
	def __pow__(self,p):
		return Frac(self.n**p,self.d**p)
	
	# surcharge de l'opérateur & pour le calcul du nombre moyen par ajout des numérateurs et dénominateurs
	def __and__(self,f):
		return Frac(self.n+f.n,self.d+f.d)
		
	# surcharge opérateurs de comparaison
	def __lt__(self,f):
		if isinstance(f,Frac):
			f = f.n/self.d
		return self.n/self.d < f
	
	def __gt__(self,f):
		if isinstance(f,Frac):
			f = f.n/self.d
		return self.n/self.d > f
	
	def __le__(self,f):
		if isinstance(f,Frac):
			f = f.n/self.d
		return self.n/self.d <= f
	
	def __ge__(self,f):
		if isinstance(f,Frac):
			f = f.n/self.d
		return self.n/self.d >= f
		

	# convertion en nombre à virgule
	def float(self):
		return self.n/self.d
		
if __name__ == '__main__':
	pass
