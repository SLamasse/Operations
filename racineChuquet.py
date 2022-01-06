#!/usr/bin/env python3

"""
Created on Sept 15 10:40:20 2021

@author: Fabrice Issac, Stephane Lamassé
Institutions: Pireh-Lamop
LICENCE GNU
This script aims at computing an imperfect square root according to Chuquet's work
"""

__version__ = "0.1.0"
__authors__ = "Stephane Lamassé", "Fabrice Issac"


from Frac import *
import math

# recherche de la racine entière inférieur d'un nombre 
# le principe consiste à essayer jusqu'à dépasser
# ici on incrémente de 1 jusqu'à dépasser 
# on doit pouvoir faire mieux, mais ce n'est pas ici le propos
def racineProche(n):
	i = 1
	while i*i <= n:
		i = i + 1
	return i - 1

# fonction pour l'affichage
def affichage(base,valeur,delta):
	print("Par",base,valeur,end="")
	if delta>0:
		print(" moins ",delta)
	else:
		print(" plus ",delta * Frac(-1,1))
#
# lecture des paramètres de la ligne de commande
#

# valeur qu'on recherche
nombre = int(sys.argv[1])
# le cas échéant nombre d'itérations (sinon 10)
if len(sys.argv)>2:
	nbe = int(sys.argv[2])	
else:
	nbe = 10

# initialisation
radicande = Frac(nombre,1)

# racine entière la plus proche
base = Frac(racineProche(nombre),1)

#
# recherche des premières bornes avec la règle des nombres moyens
#

# au départ le nombre moyen est 1/2
pivot = Frac(1,2)


# calcul du delta entre la "vrai" valeur et la valeur approchée

#delta = radicande - (base+pivot) * (base+pivot) 
delta = radicande - (base+pivot)**2 



# recherche de l'autre borne
daltaPrec = delta
affichage(base,pivot, delta)


if delta < 0: # si la différence est négative on dépasse donc on doit progresser en diminuant
	# règle de progression en diminuant (incrément du dénominateur)
	while delta<0:
		pivotPrec = pivot
		pivot = pivot & Frac(0,1)
		delta = radicande - (base+pivot)**2 
		affichage(base,pivot,delta)
	borneInf = pivot
	borneSup = pivotPrec
	
else: # sinon on augmente
	# règle de progression en augmentant (incrément numérateur et dénominateur)
	while delta>0:
		pivotPrec = pivot
		pivot = pivot & Frac(1,1)
		delta = radicande - (base+pivot)**2 
		affichage(base,pivot,delta)
	borneSup = pivot
	borneInf = pivotPrec

#
# maintenant qu'on a les premières bornes
#

# calcul du premier pivot par calcul du nombre moyen par ajout des numérateurs et dénominateurs
pivot = borneInf & borneSup
for i in range(nbe):
	# calcul du delta entre la "vrai" valeur et la valeur approchée
	delta = radicande - (base+pivot)**2 
	# changement de borne en fonction du signe du delta
	if delta < 0: # alors le pivot est la borne sup
		borneSup = pivot
	else:
		borneInf = pivot
	affichage(base,pivot,delta)
	# calcul du pivot avec les nouvelles bornes
	pivot = borneInf & borneSup


#
# affichage du résultat final
#

print("la racine de",nombre,"est approximé par",base,"+",pivot)
print("chuquet\t",base.float()+pivot.float())
print("math\t",math.sqrt(nombre))
