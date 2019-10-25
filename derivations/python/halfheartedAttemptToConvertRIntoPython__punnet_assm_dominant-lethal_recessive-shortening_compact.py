
###########
# Imports #
###########

import numpy as np

#############
# Functions #
#############

# case_fill = def cow(punnet,caseX, gamete_frequencies):

#   row_start = caseX[1]
#   row_end   = caseX[2]
#   col_start = caseX[3]
#   col_end   = caseX[4]
  
#   for i in range(row_start,row_end):
#     for (j in col_start:col_end){ # cols
            
#       #gamete_frequencies_tmp = gsub("i-1",i_minus_1-1,gamete_frequencies) # replace the i with the index of the punnet x-axis
#       #gamete_frequencies_tmp = gsub("j-1",j_minus_1-1,gamete_frequencies_tmp) # replace the j with the index of the punnet y-axis
#       #gamete_frequencies_tmp = gsub("i",i-1,gamete_frequencies_tmp) # replace the i with the index of the punnet x-axis
#       #gamete_frequencies_tmp = gsub("j",j-1,gamete_frequencies_tmp) # replace the j with the index of the punnet y-axis
      
#       p_or_q_i = unlist(strsplit(rownames(punnet)[i],"=")) # e.g. [pi, 1]
      
#       i_letter = substr(p_or_q_i[1],1,1)
#       i_index  = p_or_q_i[2]
      
#       print(i_letter)
#       print(i_index)
      
#       p_or_q_j = unlist(strsplit(colnames(punnet)[j],"=")) # e.g. [qi, 2]
      
#       j_letter = substr(p_or_q_j[1],1,1)
#       j_index  = p_or_q_j[2]
            
#       # i (x-axis)
#       gamete_frequencies_tmp = gsub(p_or_q_i[1],paste(i_letter,i_index),gamete_frequencies) # replace the i with the index of the punnet x-axis
#       gamete_frequencies_tmp = gsub(p_or_q_j[1],paste(j_letter,j_index),gamete_frequencies_tmp) # replace the j with the index of the punnet y-axis
      
#       print(gamete_frequencies_tmp)
      
#       # j (y-axis)      
      
#       punnet[i,j] <- gamete_frequencies_tmp

#     } 
#   }    
#   return(punnet)
# }

#######
# Run #
#######

gametes_x = ["pi=0", "pi=1", "pi=2", "pi=3", "qi=0", "qi=1", "qi=2", "qi=3"]
gametes_y = ["pj=0", "pj=1", "pj=2", "pj=3", "qj=0", "qj=1", "qj=2", "qj=3"]

punnet = np.array([len(gametes_x), len(gametes_y)])

# rownames(punnet) <- gametes_x
# colnames(punnet) <- gametes_y

# these are instances of the case_fill( ..., caseX, ...) arg:
#                   r r c c
case1a_indices = [2, 4, 6, 8]  # Top-right:     HTi meets hTj, i.e. mutant vs. wild
case1b_indices = [6, 8, 2, 4]  # Bottom-left:   hTi meets HTj, i.e. wild vs. mutant
case2_indices  = [2, 4, 2, 4]  # Top-left:      HTi meets HTj, i.e. mutant vs. mutant
case3_indices  = [6, 8, 6, 8]  # Bottom-right:  hTi meets hTj, i.e. wild vs. wild

# Final Gamete frequencies for all mating cases
#
case1a_gamete_frequencies = " hTi=qipj(1-r)(1-e)/2 \n\
							   HTi=qipjr(1-e)/2 \n\
							   HTi-1=qipj((1-r)e+re)/2 \n\
							   hTj=qipjr(1-e)/2 \n\
							   HTj=qipj(1-r)(1-e)/2 \n \
							   HTj-1=qipj((1-r)e+re)/2"

case1b_gamete_frequencies = " hTi=qipj(1-r)(1-e)/2 \n \
								HTi=qipjr(1-e)/2 \n \
								HTi-1=qipj((1-r)e+re)/2 \n \
								hTj=qipjr(1-e)/2 \n \
								HTj=qipj(1-r)(1-e)/2 \n \
								HTj-1=qipj((1-r)e+re)/2"

case2_gamete_frequencies  = "HTi-1=pipj/2 \n \
								HTj-1=pipj/2"

case3_gamete_frequencies  = "hTi=qiqj/2 \n \
								qiqj/2"

# Insert Gamete frequencies into punnet
#

punnet = case_fill(punnet, case1a_indices, case1a_gamete_frequencies) # generate array representing the punnet square

punnet = case_fill(punnet, case1b_indices, case1b_gamete_frequencies) # generate array representing the punnet square
punnet = case_fill(punnet, case2_indices, case2_gamete_frequencies) # generate array representing the punnet square
punnet = case_fill(punnet, case3_indices, case3_gamete_frequencies) # generate array representing the punnet square

################
# save to file #
################

setwd("C:/Users/Andrew Brockman/Dropbox/1_P2_hegTelomereTimebomb/! DRAFT/2014/Michael maths _2015-04-28/R")

write.csv(punnet,"punnet.csv")

# #p_or_q_i = unlist(strsplit(rownames(punnet)[1],"=")) # e.g. [pi, 1]

