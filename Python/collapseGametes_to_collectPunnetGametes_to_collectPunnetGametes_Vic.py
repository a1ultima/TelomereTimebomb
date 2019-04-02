
###########
# Imports #
###########

import csv 
import numpy as np
import pdb
from copy import copy
from sympy import *

#############
# Functions #
#############


########
# Main #
########
#
# Read .csv file representing the punett
#
reader      = csv.reader(open("./punnet_collapsed.tsv","rb"),delimiter="\t")
x           = list(reader)
punnet      = np.array(x)
punnet_copy = copy(punnet)


#
# Redeuce punnet_collapsed down to the unique gametes, summing their repeating frequencies
#
gamete_to_punnetFreq = {}

for row in punnet:
	for col in row:

		# If the element does not contain a gamete, such as: 'NA', or 'qj=3', then skip, otherwise...
		if len(col)>4:

			gametes = col.split(";")  # e.g. hT3=q2q3/2 ; hT2=q2q3/2 -> ['hT3=q2q3/2 ',' hT2=q2q3/2']

			for gamete in gametes:

				gamete = gamete.strip() # e.g. 'hT3=q2q3/2'
				gf = gamete.split("=") # e.g. ['hT3','q2q3/2']
				g  = gf[0] # e.g. hT3
				f  = gf[1] # e.g. q2q3/2

				# Collect the gamete (g) and its frequency (f)
				if gamete_to_punnetFreq.has_key(g):
					gamete_to_punnetFreq[g] = gamete_to_punnetFreq[g]+" + "+f
				else:
					gamete_to_punnetFreq[g] = f



#
# Symbolic maths: expand and simplify symbols
#

e = Symbol("e")
r = Symbol("r")

p0 = Symbol("p0")
p1 = Symbol("p1")
p2 = Symbol("p2")
p3 = Symbol("p3")
p4 = Symbol("p4")
p5 = Symbol("p5")
p6 = Symbol("p6")

q0 = Symbol("q0")
q1 = Symbol("q1")
q2 = Symbol("q2")
q3 = Symbol("q3")
q4 = Symbol("q4")
q5 = Symbol("q5")
q6 = Symbol("q6")


#
# Save to file
#

fo = open("./final_gamete_frequencies.tsv","wb")

for gamete in gamete_to_punnetFreq.keys():

	frequency = gamete_to_punnetFreq[gamete]

	frequency_symbolic = eval(frequency)

	frequency_symbolic_expanded = expand(frequency_symbolic)

	frequency_symbolic_expanded_simplified = simplify(frequency_symbolic_expanded)

	frequency_symbolic_expanded_simplified_factorised = factor(frequency_symbolic_expanded_simplified)

	gamete_frequency = gamete+"\t"+str(frequency_symbolic_expanded_simplified_factorised)+"\n" # e.g. 'hT3' \t 'q1p3r(1-e)/2 + q2p3r(1-e)/2 + q3p1(1-r)(1-e)/2 + q3p2(1-r)(1-e)/2 + q3p3(1-r)(1-e)/2 + q3p3r(1-e)/2 + q1p3r(1-e)/2 + q1q3/2 + q2p3r(1-e)/2 + q2q3/2 + q3p1(1-r)(1-e)/2 + q3p2(1-r)(1-e)/2 + q3p3(1-r)(1-e)/2 + q3p3r(1-e)/2 + q3q1/2 + q3q2/2 + q3q3/2 + q3q3/2'

	fo.write(gamete_frequency)

fo.close()













# Eric's Test 