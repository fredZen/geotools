#!/usr/bin/python
#
# Exemple d'utilsation
# ====================
# Sous windows
#  python extract_well_x_y_elev.py *.las sortie.txt
#
# Sous unix
#  python extract_well_x_y_elev.py "*.las" sortie.txt
#
# Analyse tous les fichiers .las du repertoire courant et produit un fichier sortie.txt

import sys
import re
from glob import glob

well_re = re.compile(r"^WELL *\. *([^ ]*):")
xcoord_re = re.compile(r"^XCOORD *\. *([0-9.]*):")
ycoord_re = re.compile(r"^YCOORD *\. *([0-9.]*):")
elev_re = re.compile(r"^ELEV *\. *([-0-9.]*):")

liste_fichiers_las = glob(sys.argv[1])

sortie = open(sys.argv[2], 'w')

def analyse(nom_las):
	entree_las = open(nom_las, 'r')

	well = None
	xcoord = None
	ycoord = None
	elev = None

	for ligne in entree_las:
		match = well_re.match(ligne)
		if match:
			well = match.group(1)

		match = xcoord_re.match(ligne)
		if match:
			xcoord = match.group(1)

		match = ycoord_re.match(ligne)
		if match:
			ycoord = match.group(1)

		match = elev_re.match(ligne)
		if match:
			elev = match.group(1)

		if well and xcoord and ycoord and elev:
			break

	entree_las.close()
	return (well + "      " + xcoord + "      " + ycoord + "      " + elev + "\n")

for las in liste_fichiers_las:
	sortie.write(analyse(las))

sortie.close()
