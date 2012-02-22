#!/usr/bin/python
import sys
import re
import math

class Loi(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def perm(self, poro):
		return self.a * math.exp(self.b * poro)

coeffs = {
	"102.0000": Loi(0.005, 0.525),
	"103.0000": Loi(0.015, 0.549),
	"104.0000": Loi(0.098, 0.536),
}

loi_defaut = Loi(0.002, 0.471)

def get_loi(c):
	return coeffs.get(c, loi_defaut)

entree_las = open(sys.argv[1], 'r')
sortie_las = open(sys.argv[2], 'w')

whitespace = re.compile('[ \t]+')

ligne = ""
while ligne != "~Ascii":
	ligne = entree_las.readline().strip()
	sortie_las.write(ligne + "\n")

for ligne in entree_las:
	ligne = ligne.strip()
	elems = whitespace.split(ligne)
	
	loi = get_loi(elems[5])
	poro = float(elems[1])
	perm = loi.perm(poro)
	elems[5] = "{0:.4f}".format(perm)

	sortie_las.write("   ".join(map(str, elems))+"\n")
