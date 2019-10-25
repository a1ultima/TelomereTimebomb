##########
# Readme #
##########

""" README_v2015-05-01:

    @@Cases 1-3 are statistically independent sequences of life-cycle events, 
    starting with mating, and finishing with telomere shortening. 
    Death can be seen as a fourth case, which happens at the beginning of the life 
    cycle prior to any of the cases 1-3; these are marked as crosses in the punnet.
    All cases are represented as non-X cells in the punnet. 

    @@Chromosomes are represented in two ways:

        (i) as characterised by the alleles on two loci: @H-locus, and @T-locus. 

        (ii) as characterised by the alleles that represent length of @telomeres.

    @@H-locus: consists of two possible alleles: @H and @h. 

    @@T-locus: 

    @@H-allele / @@h-allele / @@Gene conversion: is dominant for the phenotype of 
    "@@homing", which, when expressed by a @HEG, causes a conversion of any @h alleles 
    in the gamete/diploid cell into an @H allele, at a probability, e, which is commonly 
    referred to as the HEG's "@homing rate". This conversion of it's competing wild-type 
    h allele for occupancy of the @H-locus is exemplary of "selfish gene" behaviour. 

    @@HEG: ...@todo... Acronym for: @@Homing Endonuclease Gene, a selfish gene that 
    simultaneously expresses two phenotypes: (i) @@Homing reaction and (ii) A gene 
    @@Knock-out, of a bespoke target gene.

    @@Homing Rate (e) / @@Homing reaction / @@Knock-out (@@KO): The @homing reaction 
    is a phenotype expressed by the @@H-allele, which causes @gene conversion of 
    it's wild-type competitor: @h-allele, to change into a @H-allele, which effectively
    @knocks out the @h-allele, turning off it's otherwise expressed phenotype. The 
    @HEG can be genetically engineered to target bespoke genes, and hence turn-off 
    their phenotypic functionality. For purposes of this project, the @h-allele targeted 
    for @HEG's @knocking-out is assumed to be the @@telomerase gene, whose wild-type
    function is necessary for the supply of @@telomerase enzymes, whose biological 
    role is to prevent the shortening of telomere's within the gametes of all 
    dipoid eukaryotic organisms; hence solving the @@End-replication-problem, which
    otherwise, would mean an individual's old-age to be inherited by such an 
    individual's offspring. Therefore, in the absence of telomerase, caused by 
    a @HEG engineered to @Knock-out - and selfishly convert - a @h-allele, the 
    gametes of an individual would experience the non-wild-type effect of telomere 
    shortening, which are then passed onto the offspring of that individual, and 
    from that individual to future generations, until, at some number of generations
    away from the original H-mutant bearing ancestor, critically short telomeres 
    - perhaps those that cannot form a key functional-structural unit called T-loops
    - will cause lethality to all further offspring-generations embryos: thus dooming 
    such lines of descendents to extinction. Such h-mutant ancestors would be silently,
    propagating the selfish-@H-alleles within the species' @gene pool, prior to the 
    shortening-telomeres' reaching such critically short, lethal lengths, in terms 
    of natural selective pressures acting on the telomeres; such silent-propagation
    of these - eventually species-dooming - alleles gives the Telomere Timebomb a 
    means to overcome the wasteful process of natural selection, common to most 
    genetic-engineering-oriented approaches to vector control, such as SIT or RIDL. 


    @@telomeres: for simplicity, we assume every diploid individual carries two 
    telomere "alleles" at any time, one originating from said individual's mother 
    and the other from said individual's father. The @T-locus these telomeres occupy 
    is X-allelic, where X represents the number of possible @@telomere-lengths said 
    individual's species' can harbour. @@telomere-length (in generations) is measured 
    in terms of numbers-of-generations of telomere shortening that can be experienced
    by an x--length-telomere before it reach a critically short length, under which 
    any individual carrying the short-telomere experiances instant death, thus
    removing it, and its alleles, from the species's @gene-pool.


    @@punnet-table / @@gene-pool / @@cases (@@caseX (@@case1a / @@case1b / 
    @@case2 / @@case3)) / @@genotype-frequency / @@gamete-frequency:

      vvv--- Possible @@gamete genotypes ---vvv

           pi=0  pi=1   pi=2  pi=3  qi=0 qi=1  qi=2  qi=3   <-- alt. symbol for @gamete genotypes
    _______________________________________________________
    |[0/0]| HT0 | HT1 | HT2 | HT3 | hT0 | hT1 | hT2 | hT3 | 
    |_____|_[1]_|_[2]_|_[3]_|_[4]_|_[5]_|_[6]_|_[7]_|_[8]_| 
    |HT0[1]  x  |  4  |  4  |  4  |  4  |  4  |  4  |  x  | pj=0  <-- Case4 
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |HT1[2]  x  |     |     |     |  x  |     |     |     | pj=1
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |HT2[3]  x  |     |Case2|     |  x  |     |Case1a     | pj=2
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |HT3[4]  x  |     |     |     |  x  |     |     |     | pj=3
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |hT0[5]  x  |  4  |  4  |  4  |  4  |  4  |  4  |  4  | qj=0  <-- Case4  
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |hT1[6]  x  |     |     |     |  x  |     |     |     | qj=1
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |hT2[7]  x  |     |Case1b     |  x  |     |Case3|     | qj=2
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    |hT3[8]  x  |     |     |     |  x  |     |     |     | qj=3
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|

            ^Case4 

    ^ An @@uncollapsed representation of this (^) @punnet-table is generated:
        - by ./R/gameteFreq_to_Punnet.r
        - at: ./R/
        - as: ./R/punnet.csv
    ^ A @@collaped version of the @uncollapsed @punnet-table is generated:
        - by: ./R/Python/punnet_to_collaseGametes.py 
            - as: Numpy.array ("result" (var))
        - at: ./Python/
        - as: ./Python/test.csv

"""


###########
# Imports #
###########

import csv 
import numpy as np
import pdb
from copy import copy

#############
# Functions #
#############

def collapse_punnet(caseX,list_or_array):

    """ ...
    caseX:          see: case1a
    list_or_array:  "list" or "array"
    """

    #
    #
    #

    caseX_copy = copy(caseX)

    #
    #
    #

    print("Caste is: "+str(caseX))

    for j,row in enumerate(caseX): # each row has multiple columns, each of which represent independent matings, e.g. ['hT3=q3q1/2 \n hT1=q3q1/2', 'hT3=q3q2/2 \n hT2=q3q2/2', 'hT3=q3q3/2 \n hT3=q3q3/2']

        print("Row is :"+str(j))

        for i,col in enumerate(row): # each col has all the gamete frequencies ultimately resulting from a single mating, e.g. hT3=q3q1 \n hT1=q3q1/2

            print("Column is: "+str(i))

            g_collapsed = {}

            # e.g. col = 'hT1=q1q1/2 \n hT1=q1q1/2'

            gametes = "".join(list(col)).replace(" ","").split("\n") # ['hT1=q1q1/2', 'hT1=q1q1/2']    

            "hT1","q1q1/2"
            "hT1","q1q1/2"

            # split the gametes by hT1 and q1q1/2
            for gamete in gametes: # e.g. gamete = hT1=q1q1/2 

                # if not ("=" in gamete):
                #     print("Row number: "+str(j)+" and column number: "+ str(i) + " are causing this mess...!")
                #     pdb.set_trace() # @latest

                g,f = gamete.split("=")     # e.g. g = hT1, f = q1q1/2

                if g_collapsed.has_key(g):
                    g_collapsed[g].append(f)    # e.g. g_collapsed = {'hT1': ['q1q1/2', 'q1q1/2']}
                else:
                    g_collapsed[g] = [f]        # e.g. g_collapsed = hT1: ['q1q1/2']


            gametes_in_col = []

            # for each unique gamete (hT1), sum it's multiple expressions (['q1q1/2', 'q1q1/2'])
            for g in g_collapsed.keys():

                f = " + ".join(g_collapsed[g])

                gametes_in_col.append(g+"="+f)

            # join up the various gametes in a @punnet_table element (cell), delimited by " ; ", and assign it to the caseX
            caseX_copy[j,i] = " ; ".join(gametes_in_col)

    if list_or_array == "list":
        return caseX_copy.tolist()
    elif list_or_array == "array":
        return caseX_copy

def get_caseX_indices_matching_symbol_list(result,match_symbols = ["NA"]):

    """ Achieves "def get_caseX_indices_matching_symbol" but on a list of symbols.

    """
    #
    # Sub-function
    #
    def get_caseX_indices_matching_symbol(result,match_symbol = "NA"):
        """ get a list of indices of case4 (see: @caseX) elements from @result

        Args:
            result:         @@result: an @uncollasped punnet square, which represents the @punnet imported as an R-like dataframe from: ../R/punnet.csv
            match_symbol:   default: "NA", the string that represents elements in the @@punnet that have been killed, carrying a critically-short @telomere, T0
        Returns:
            @todo

        """

        caseX_matching    = np.in1d(result.ravel(),[match_symbol]).reshape(result.shape) # Case4: (_T0)&(__): critically short, lethal T0-carring diploid individuals die
        caseX_indices_tmp = np.where(caseX_matching) # locations (indicies)
        caseX_indices     = zip(caseX_indices_tmp[0],caseX_indices_tmp[1])

        return caseX_indices
    #
    # Main
    #
    caseX_indices = []  # indexes are (x,y) coordinates on the punnet (result) that the symbol is found in, e.g. (2,6)

    symbol_to_index = {}

    for symbol in match_symbols:

        #..Generate matching indices on @Punnet-table (result) 
        match_index = get_caseX_indices_matching_symbol(result,symbol)

        #..Multiple matching indices to symbol AND symbol is a gamete frequency 
        if (len(match_index)>1) and (not symbol == "NA"):

            symbol_to_index[symbol] = match_index

        #..Multiple matching indices to symbol AND symbol=="NA" (i.e. death)
        elif (len(match_index)>1) and (symbol == "NA"):
            caseX_indices = match_index
            symbol_to_index[symbol] = match_index
            break

        #..Only one matching index to symbol
        else:
            caseX_indices.append(match_index)
            symbol_to_index[symbol] = match_index

    return caseX_indices, symbol_to_index

def map_case_to_punnet_indices(caseX, caseX_sym_to_coord):

    """ Maps the locations of symbols in caseX to the corresponding symbols in @punnet-table

    Args:
        CaseX:                  ...@CaseX... 
        caseX_sym_to_coord:     ...outputted by "def get_caseX_indices_matching_symbol_list"... e.g. case1a_sym_to_coord

    """

    caseCoord_to_punnetCoord = {}

    for y,j in enumerate(caseX):
        for x,i in enumerate(j):

            case_coord = (y,x)

            punnet_coord = caseX_sym_to_coord[i]

            caseCoord_to_punnetCoord[case_coord] = punnet_coord

    return caseCoord_to_punnetCoord

def replace_punnet_with_collapsed_cases(punnet,map_caseX_to_punnet,caseX_collapsed):

    """ Replaces elements of the @punnet-table using elemts of caseX_collapsed via a map_caseX_to_punnet

    """

    for case_coord in map_caseX_to_punnet.keys():

        punnet_coords = map_caseX_to_punnet[case_coord]

        for punnet_coord in punnet_coords:

            punnet[punnet_coord] = caseX_collapsed[case_coord]

    return punnet


########
# Main #
########
#
# Read .csv file representing the punett
#
reader      = csv.reader(open("../R/punnet.csv","rb"),delimiter=",")
#                          ^create a python file object
#               ^call the csv lib and run the reader() method, which        


data        = list(reader)
result      = np.array(data)
result_copy = copy(result)

#
# Specify indices of each case      @@settings: user settings must match between this and the ones specified in ../R/gameteFrequencies_to_punnet.r
#                j1,2,i1,2
case1a_indices = [2,4,6,8] # Case1a: (hTi)&(HTj): wild-type sperm (hTi) meets mutant egg (HTj)
#              y0, y1, x0, x1         ^ small h must be on the X-axis, i.e. this is in the top right
case1b_indices = [6,8,2,4] # Case1b: (HTi)&(hTj): mutant sperm (HTi) meets wild-type egg (hTj)
#                                     ^ big H must be on the X-axis, i.e. this is in the botton left
case2_indices  = [2,4,2,4] # Case2:  (HTi)&(HTj): mutant sperm (HTi) meets mutant egg (HTj)
#                                     ^ big H must be on the X axis, i.e. this is on the top left
case3_indices  = [6,8,6,8] # Case3:  (hTi)&(hTj): wild-type sperm (hTi) meets wild-type egg (hTj)
#                                     ^ small h must be ont he X-axis, i.e. this is on the bottom right
case4_indices  = get_caseX_indices_matching_symbol_list(result,match_symbols = ["NA"]) # indices of @result (@punnet-table) elements dead due to T0, T0->Death



#
# Separate the @cases (@caseX)
#                     
case1a = result[case1a_indices[0]:case1a_indices[1]+1,case1a_indices[2]:case1a_indices[3]+1] 

# import pprint
# pprint.pprint(case1a)
# pdb.set_trace()

# e.g. slice a rectangle from ^ to  ^ (y, row)       , and from ^      to ^ (x, column) 
#  ...                        2 to  4
case1b = result[case1b_indices[0]:case1b_indices[1]+1,case1b_indices[2]:case1b_indices[3]+1]
case2  = result[case2_indices[0]:case2_indices[1]+1,  case2_indices[2]:case2_indices[3]+1  ]
case3  = result[case3_indices[0]:case3_indices[1]+1,  case3_indices[2]:case3_indices[3]+1  ]





#
# Coordinates of elements in caseX matching to result (@punnet table)
#
case1a_flat = case1a.flatten().tolist()
case1b_flat = case1b.flatten().tolist()
case2_flat  = case2.flatten().tolist()
case3_flat  = case3.flatten().tolist()
#
case1a_coord, case1a_sym_to_coord  = get_caseX_indices_matching_symbol_list(result, match_symbols = case1a_flat)
case1b_coord, case1b_sym_to_coord  = get_caseX_indices_matching_symbol_list(result, match_symbols = case1b_flat)
case2_coord , case2_sym_to_coord   = get_caseX_indices_matching_symbol_list(result, match_symbols = case2_flat)
case3_coord , case3_sym_to_coord   = get_caseX_indices_matching_symbol_list(result, match_symbols = case3_flat)
case4_coord , case4_sym_to_coord   = case4_indices
#
# map coordinates from @caseX to @punnet-table, so that later when we collapse the @caseXs we can map them back to the @punnet-table
#
map_case1a_to_punnet = map_case_to_punnet_indices(case1a,case1a_sym_to_coord)
map_case1b_to_punnet = map_case_to_punnet_indices(case1b,case1b_sym_to_coord)
map_case2_to_punnet = map_case_to_punnet_indices(case2,case2_sym_to_coord)
map_case3_to_punnet = map_case_to_punnet_indices(case3,case3_sym_to_coord)
#
# collapse the punnet's gamete frequencies, case by case 
#
case1a_collapsed = collapse_punnet(case1a,"array") # top-right     punnet_collapsed_stiching_top_right = np.array()
case1b_collapsed = collapse_punnet(case1b,"array") # bottom-left   punnet_collapsed_stiching_bottom_left = np.array()
case2_collapsed = collapse_punnet(case2,"array")   # top-left      punnet_collapsed_stiching_top_left = np.array()
case3_collapsed = collapse_punnet(case3,"array")   # bottom-right
#
# Replace non-collapsed @punnet-table elements with collapsed
# 
punnet_collapsed = replace_punnet_with_collapsed_cases(result_copy     ,map_case1a_to_punnet,case1a_collapsed) 
punnet_collapsed = replace_punnet_with_collapsed_cases(punnet_collapsed,map_case1b_to_punnet,case1b_collapsed) 
punnet_collapsed = replace_punnet_with_collapsed_cases(punnet_collapsed,map_case2_to_punnet,case2_collapsed) 
punnet_collapsed = replace_punnet_with_collapsed_cases(punnet_collapsed,map_case3_to_punnet,case3_collapsed) 
#
# Save to file
#
np.savetxt("punnet_collapsed.tsv",punnet_collapsed, delimiter="\t", fmt="%s")

