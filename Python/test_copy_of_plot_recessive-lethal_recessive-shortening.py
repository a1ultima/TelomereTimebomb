###########
# Imports #
###########

from math import *
import numpy as np
import pdb 
#############
# Functions #
#############

def simulate_timeseries( gamete_frequencies, t = 100, e = 0.7, r = 0.5):

    """ Simulate gamete frequency dynamics to t generations
    Args:
        gamete_frequencies (list):     list of initial gamete frequencies as such: [p0, p1, p2, p3, q0, q1, q2, q3]
        t (int):                       number of generations to iterate through, e.g. 50
        e (float):                     @homing rate
        r (float):                     @recombination frequency
    Returns:
        gf_timeseries (nested list):   gamete frequencies through time as such: [ t1, t2, ... ], e.g. t1: [p0, p1, p2, p3, q0, q1, q2, q3]
    """

    def next_generation( p0, p1, p2, p3, q0, q1, q2, q3, e, r):
        """

        takes values of all gamete frequencies, pi and qi, at generation N, to yield gamete frequencies at generation N+1

            p0 = HT0    q0 = hT0 
            p1 = HT1    q1 = hT1 
            p2 = HT2    q2 = hT2 
            p3 = HT3    q3 = hT3

        """

        p0_next = ((-6*e*p0*q1*r + 6*e*p0*q1 - 6*e*p0*q2*r + 6*e*p0*q2 - 6*e*p0*q3*r + 6*e*p0*q3 + 6*e*p1*q0*r + 6*e*p1*q1 + 6*e*p1*q2 + 6*e*p1*q3 + 6*e*p2*q0*r + 6*e*p2*q1 + 6*e*p3*q0*r + 6*e*p3*q1 + 22*p0*p1 + 5*p0*p2 + 5*p0*p3 + 6*p0*q1*r + 6*p0*q2*r + 6*p0*q3*r + 11*pow(p1,2) + 5*p1*p2 + 5*p1*p3 - 6*p1*q0*r + 6*p1*q0 - 6*p2*q0*r + 6*p2*q0 - 6*p3*q0*r + 6*p3*q0)/6)/pow((1-p0),2)
        p1_next = (e*p0*q1*r - e*p1*q0*r + e*p1*q0 - e*p1*q1 + e*p1*q2*r + e*p1*q3*r - e*p1*q3 - e*p2*q1*r + e*p2*q1 + 2*e*p2*q2 + e*p2*q3 - e*p3*q1*r + e*p3*q2 + p0*p2 - p0*q1*r + p0*q1 + p1*p2 + p1*q0*r + p1*q1 - p1*q2*r + p1*q2 - p1*q3*r + p1*q3 + p2*q1*r + p3*q1*r)/pow((1-p0),2)
        p2_next = (e*p0*q2*r - e*p1*q2*r + e*p1*q3 - e*p2*q0*r + e*p2*q0 + e*p2*q1*r - e*p2*q1 - e*p2*q2 + e*p2*q3*r + e*p3*q1 - e*p3*q2*r + e*p3*q2 + 2*e*p3*q3 + p0*p3 - p0*q2*r + p0*q2 + p1*p3 + p1*q2*r + p2*q0*r - p2*q1*r + p2*q1 + p2*q2 - p2*q3*r + p2*q3 + p3*q2*r)/pow((1-p0),2)
        p3_next = (e*p0*q3*r - e*p1*q3*r - e*p2*q3*r - e*p3*q0*r + e*p3*q0 + e*p3*q1*r - e*p3*q1 + e*p3*q2*r - e*p3*q2 - e*p3*q3 - p0*q3*r + p0*q3 + p1*q3*r + p2*q3*r + p3*q0*r - p3*q1*r + p3*q1 - p3*q2*r + p3*q2 + p3*q3)/pow((1-p0),2)
        q0_next = (-e*p0*q1*r - e*p0*q2*r - e*p0*q3*r + e*p1*q0*r - e*p1*q0 + e*p2*q0*r - e*p2*q0 + e*p3*q0*r - e*p3*q0 + p0*q1*r + p0*q2*r + p0*q3*r - p1*q0*r + p1*q0 - p2*q0*r + p2*q0 - p3*q0*r + p3*q0 + q0*q1 + q0*q2 + q0*q3)/pow((1-p0),2)
        q1_next = (e*p0*q1*r - e*p0*q1 - e*p1*q0*r - e*p1*q1 - e*p1*q2*r - e*p1*q3*r + e*p2*q1*r - e*p2*q1 + e*p3*q1*r - e*p3*q1 - p0*q1*r + p0*q1 + p1*q0*r + p1*q1 + p1*q2*r + p1*q3*r - p2*q1*r + p2*q1 - p3*q1*r + p3*q1 + q0*q1 + pow(q1,2) + q1*q2 + q1*q3)/pow((1-p0),2)
        q2_next = (e*p0*q2*r - e*p0*q2 + e*p1*q2*r - e*p1*q2 - e*p2*q0*r - e*p2*q1*r - e*p2*q2 - e*p2*q3*r + e*p3*q2*r - e*p3*q2 - p0*q2*r + p0*q2 - p1*q2*r + p1*q2 + p2*q0*r + p2*q1*r + p2*q2 + p2*q3*r - p3*q2*r + p3*q2 + q0*q2 + q1*q2 + pow(q2,2) + q2*q3)/pow((1-p0),2)
        q3_next = (e*p0*q3*r - e*p0*q3 + e*p1*q3*r - e*p1*q3 + e*p2*q3*r - e*p2*q3 - e*p3*q0*r - e*p3*q1*r - e*p3*q2*r - e*p3*q3 - p0*q3*r + p0*q3 - p1*q3*r + p1*q3 - p2*q3*r + p2*q3 + p3*q0*r + p3*q1*r + p3*q2*r + p3*q3 + q0*q3 + q1*q3 + q2*q3 + pow(q3,2))/pow((1-p0),2)

        return p0_next, p1_next, p2_next, p3_next, q0_next, q1_next, q2_next, q3_next 


    #
    # Main
    #
    p0, p1, p2, p3, q0, q1, q2, q3 = gamete_frequencies

    # initiate time series list
    timeseries = [gamete_frequencies]

    # iterate the recursive equations (see "def next_generation")
    for generation in range(0,t):

        p0, p1, p2, p3, q0, q1, q2, q3 = next_generation( p0, p1, p2, p3, q0, q1, q2, q3, e, r)

        timeseries.append([p0, p1, p2, p3, q0, q1, q2, q3])



    return timeseries


def convert_timeseries_gametes_to_alleles( timeseries_gametes ):
    """ takes timeseries_gametes (see: "def simulate_timeseries") and generates the H-allele and h-allele frequencies

    """

    timeseries_gametes = np.array(timeseries_gametes)

    H_timeseries = timeseries_gametes[0:,0:4+1].sum(axis=1)

    h_timeseries = timeseries_gametes[0:,4:8+1].sum(axis=1)
    #pdb.set_trace()
    return H_timeseries, h_timeseries

def tests( p0, p1, p2, p3, q0, q1, q2, q3, e, r):
    """ tests if:

        (i) initial gamete frequencies sum to 1

        (ii) e and r are between 0 and 1 

    """

    print("testing initial gamete frequencies sum to 1...")
    if sum([p0, p1, p2, p3, q0, q1, q2, q3])%1.0 < 0.000000000001:
        print("\t\tpassed")
    else:
        raise Exception("\tError: initial gamete frequencies do not add up to 1")
    print("testing e and r are between 0 and 1...")
    if 0<e<=1:
        print("\te \n\t\t passed")
    else:
        raise Exception("\tError: e must me between 0 and 1")
    if 0<r<=1:
        print("\tr \n\t\t passed")
    else:
        raise Exception("\tError: r must me between 0 and 1")

#######
# Run #
#######

# initial gamete frequencies & parameters
#
# params
e = 0.4 # e, homing rate, e.g. 0.5 means homing occurs in 50% of the zygotes, converting the zygote from h/H to H/H
r = 0.5 # recombination frequency, e.g. 0.5 means there is a cross-over event that occurs in half the zygotes
# gamete freq
list_e = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
p0 = 0.0 # HT0 
p1 = 0.0 # HT1
p2 = 0.0 # HT2
p3 = 0.1 # HT3
q0 = 0.0 # hT0
q1 = 0.0 # hT1
q2 = 0.0 # hT2
q3 = 0.9 # hT3

e_dict = {0.0:0.0, 0.1:0.2, 0.2:0.4, 0.3:0.5, 0.4:0.8, 0.5:1.0}

import matplotlib.pyplot as plt

cmap_H = plt.cm.get_cmap('Blues')
cmap_h = plt.cm.get_cmap('Oranges')
cmap_b = plt.cm.get_cmap('gray')

plt.figure()

for e in list_e:
    #
    # simulate t generations/lifecycles of dynamics, at homing rate e and recombination frequency r
    #
    timeseries_gametes = simulate_timeseries( [p0, p1, p2, p3, q0, q1, q2, q3], t = 20, e = e, r = r)


    H_timeseries , h_timeseries = convert_timeseries_gametes_to_alleles( timeseries_gametes )

    
    timeseries_gametes = np.array(timeseries_gametes)
    #print(timeseries_gametes)
    #print(type(timeseries_gametes))

    plt.plot(H_timeseries, color = cmap_b(0.1), label = e, linewidth = 2)
    plt.plot(H_timeseries, color = cmap_H(e), label = e, linewidth = 1.5)
    plt.plot(h_timeseries, color = cmap_b(0.1), label = e, linewidth = 2)
    plt.plot(h_timeseries, color = cmap_h(e), label = e, linewidth = 1.5)      

from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color = "white",lw = 5),
                Line2D([0], [0], color = cmap_H(0.0), lw = 5),
                Line2D([0], [0], color = cmap_H(0.1), lw = 5),
                Line2D([0], [0], color = cmap_H(0.2), lw = 5),
                Line2D([0], [0], color = cmap_H(0.3), lw = 5),
                Line2D([0], [0], color = cmap_H(0.4), lw = 5),
                Line2D([0], [0], color = cmap_H(0.5), lw = 5),
                Line2D([0], [0], color = "white",lw = 5),
                Line2D([0], [0], color = cmap_h(0.0), lw = 5),
                Line2D([0], [0], color = cmap_h(0.1), lw = 5),
                Line2D([0], [0], color = cmap_h(0.2), lw = 5),
                Line2D([0], [0], color = cmap_h(0.3), lw = 5),
                Line2D([0], [0], color = cmap_h(0.4), lw = 5),
                Line2D([0], [0], color = cmap_h(0.5), lw = 5)]

list_e_leg = ["HEG+"]
list_e_leg.extend(list_e)
list_e_leg.extend(["WT"])
list_e_leg.extend(list_e)

plt.title("Allele frequency HEG+ vs WT with variable e")
plt.ylabel("Allele frequency")
plt.xlabel("mosquito generations")
plt.legend(custom_lines, list_e_leg)
#plt.savefig("../plots/Allele_frequency_dynamics_recessive_lethal_recessive_shortening.png", dpi = 600)
plt.show()

#################################################################
#100% stacked plot for generational telomere length distribution#
#################################################################

#Formatting frequency array
A = timeseries_gametes[..., np.newaxis]
B = np.concatenate(A, axis = 1)

#Sum of HT1, HT2, HT3 frequencies
Freq_sum = B[1]+B[2]+B[3]

#Converting allele frequencies to "percentages"
#HT0_freq = b[0]
HT1_freq = B[1]/Freq_sum
HT2_freq = B[2]/Freq_sum
HT3_freq = B[3]/Freq_sum

x = np.arange(21)
y = np.vstack([HT1_freq, HT2_freq, HT3_freq])

labels = ["HT1", "HT2", "HT3"]

fig, ax = plt.subplots()
ax.stackplot(x, HT1_freq, HT2_freq, HT3_freq, labels = labels)
ax.legend(loc='upper right')
plt.title("Allele frequency HEG+ vs WT with variable e")
plt.ylabel("Allele frequency")
plt.xlabel("mosquito generations")
#plt.savefig("../plots/Allele_frequency_dynamics_recessive_lethal_recessive_shortening_Stacked_Plot.png", dpi = 600)
plt.show()





