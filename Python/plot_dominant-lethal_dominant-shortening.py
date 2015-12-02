###########
# Imports #
###########

from math import *

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

        p0_next = (2*e*p1*q1 + e*p1*q2 + e*p1*q3 + e*p2*q1 + e*p3*q1 + pow(p1,2) + p1*p2 + p1*p3)/pow((1-p0),2)
        p1_next = (-e*p1*q1 + e*p1*q2*r + e*p1*q3*r - e*p1*q3 - e*p2*q1*r + e*p2*q1 + 2*e*p2*q2 + e*p2*q3 - e*p3*q1*r + e*p3*q2 + p1*p2 + p1*q1 - p1*q2*r + p1*q2 - p1*q3*r + p1*q3 + pow(p2,2) + p2*p3 + p2*q1*r + p3*q1*r)/pow((1-p0),2)
        p2_next = (-e*p1*q2*r + e*p1*q3 + e*p2*q1*r - e*p2*q1 - e*p2*q2 + e*p2*q3*r + e*p3*q1 - e*p3*q2*r + e*p3*q2 + 2*e*p3*q3 + p1*p3 + p1*q2*r + p2*p3 - p2*q1*r + p2*q1 + p2*q2 - p2*q3*r + p2*q3 + pow(p3,2) + p3*q2*r)/pow((1-p0),2)
        p3_next = (-(e - 1)*(p1*q3*r + p2*q3*r - p3*q1*r + p3*q1 - p3*q2*r + p3*q2 + p3*q3))/pow((1-p0),2)
        q0_next = 0
        q1_next = (-e*p1*q1 - e*p1*q2*r - e*p1*q3*r + e*p2*q1*r - e*p2*q1 + e*p3*q1*r - e*p3*q1 + p1*q1 + p1*q2*r + p1*q3*r - p2*q1*r + p2*q1 - p3*q1*r + p3*q1 + pow(q1,2) + q1*q2 + q1*q3)/pow((1-p0),2)
        q2_next = (e*p1*q2*r - e*p1*q2 - e*p2*q1*r - e*p2*q2 - e*p2*q3*r + e*p3*q2*r - e*p3*q2 - p1*q2*r + p1*q2 + p2*q1*r + p2*q2 + p2*q3*r - p3*q2*r + p3*q2 + q1*q2 + pow(q2,2) + q2*q3)/pow((1-p0),2)
        q3_next = (e*p1*q3*r - e*p1*q3 + e*p2*q3*r - e*p2*q3 - e*p3*q1*r - e*p3*q2*r - e*p3*q3 - p1*q3*r + p1*q3 - p2*q3*r + p2*q3 + p3*q1*r + p3*q2*r + p3*q3 + q1*q3 + q2*q3 + pow(q3,2))/pow((1-p0),2)

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
e = 0.7 # e, homing rate, e.g. 0.5 means homing occurs in 50% of the zygotes, converting the zygote from h/H to H/H
r = 0.5 # recombination frequency, e.g. 0.5 means there is a cross-over event that occurs in half the zygotes
# gamete freq
p0 = 0.0 # HT0 
p1 = 0.0 # HT1
p2 = 0.0 # HT2
p3 = 0.2 # HT3
q0 = 0.0 # hT0
q1 = 0.0 # hT1
q2 = 0.0 # hT2
q3 = 0.8 # hT3

#
# simulate t generations/lifecycles of dynamics, at homing rate e and recombination frequency r
#
timeseries_gametes = simulate_timeseries( [p0, p1, p2, p3, q0, q1, q2, q3], t = 20, e = 0.8, r = 0.5)


def convert_timeseries_gametes_to_alleles( timeseries_gametes ):
    """ takes timeseries_gametes (see: "def simulate_timeseries") and generates the H-allele and h-allele frequencies

    """

    timeseries_gametes = np.array(timeseries_gametes)

    H_timeseries = timeseries_gametes[0:,0:4+1].sum(axis=1)

    h_timeseries = timeseries_gametes[0:,4:8+1].sum(axis=1)

    return H_timeseries



import matplotlib.pyplot as plt

plt.figure()

p = plt.plot(H_timeseries)

plt.show()













