
#############
# Functions #
#############

case_fill <- function(punnet,caseX, gamete_frequencies){

  # target a region of the punnet square with the appropriate case (case 1a, case 1b, case 2, case 3, etc.)
  row_start = caseX[1]
  row_end   = caseX[2]
  col_start = caseX[3]
  col_end   = caseX[4]
  
  # iterate throught the targeted region's cells, adding the non-symbolic "final gamete frequencies" - w.r.t i and j - to them
  for (i in row_start:row_end){   # rows
    for (j in col_start:col_end){ # cols
      # replace the symbolic i and j with actual numbers
      #
      # i (x-axis) 
      p_or_q_i = unlist(strsplit(rownames(punnet)[i],"=")) # e.g. [pi, 1]
      i_index  = p_or_q_i[2] # e.g. 1
      gamete_frequencies_tmp = gsub("i-1",as.numeric(i_index)-1,gamete_frequencies) # replace the i-1 with i_index-1
      gamete_frequencies_tmp = gsub("i",i_index,gamete_frequencies_tmp) # replace the i with i_index
      # j (y-axis)
      p_or_q_j = unlist(strsplit(colnames(punnet)[j],"=")) # e.g. [qj, 2]
      j_index  = p_or_q_j[2] # e.g. 2
      gamete_frequencies_tmp = gsub("j-1",as.numeric(j_index)-1,gamete_frequencies_tmp) # replace the j-1 with j_index-1
      gamete_frequencies_tmp = gsub("j",j_index,gamete_frequencies_tmp) # replace the j with j_index
      # fill in the punnet square cells with the non-symbolic gamete frequencies       
      punnet[i,j] <- gamete_frequencies_tmp
    } 
  }    
  return(punnet)
}

#######
# Run #
#######

gametes_x <- c("pi=0","pi=1","pi=2","pi=3","qi=0","qi=1","qi=2","qi=3") 
gametes_y <- c("pj=0","pj=1","pj=2","pj=3","qj=0","qj=1","qj=2","qj=3")

punnet <- data.frame(matrix(nrow=length(gametes_y),ncol=length(gametes_x)))

rownames(punnet) <- gametes_y
colnames(punnet) <- gametes_x

# these are instances of the case_fill( ..., caseX, ...) arg:
#                   r r c c 
case1a_indices <- c(2,4,6,8) # Top-right:     HTi meets hTj, i.e. mutant vs. wild
case1b_indices <- c(6,8,2,4) # Bottom-left:   hTi meets HTj, i.e. wild vs. mutant
case2_indices  <- c(2,4,2,4) # Top-left:      HTi meets HTj, i.e. mutant vs. mutant
case3_indices  <- c(6,8,6,8) # Bottom-right:  hTi meets hTj, i.e. wild vs. wild

# Final Gamete frequencies for all mating cases
#
case1a_gamete_frequencies <- "hTi=qi*pj*(1-r)*(1-e)/2 \n HTi=qi*pj*r*(1-e)/2 \n HTi-1=qi*pj*((1-r)*e+r*e)/2 \n hTj=qi*pj*r*(1-e)/2 \n HTj=qi*pj*(1-r)*(1-e)/2 \n HTj-1=qi*pj*((1-r)*e+r*e)/2"
case1b_gamete_frequencies <- "hTi=qi*pj*(1-r)*(1-e)/2 \n HTi=qi*pj*r*(1-e)/2 \n HTi-1=qi*pj*((1-r)*e+r*e)/2 \n hTj=qi*pj*r*(1-e)/2 \n HTj=qi*pj*(1-r)*(1-e)/2 \n HTj-1=qi*pj*((1-r)*e+r*e)/2"
case2_gamete_frequencies  <- "HTi-1=pi*pj/2 \n HTj-1=pi*pj/2"
case3_gamete_frequencies  <- "hTi=qi*qj/2 \n hTj=qi*qj/2"

# Insert Gamete frequencies into punnet
#
punnet <- case_fill(punnet, case1a_indices, case1a_gamete_frequencies) # generate array representing the punnet square
punnet <- case_fill(punnet, case1b_indices, case1b_gamete_frequencies) # generate array representing the punnet square
punnet <- case_fill(punnet, case2_indices, case2_gamete_frequencies) # generate array representing the punnet square
punnet <- case_fill(punnet, case3_indices, case3_gamete_frequencies) # generate array representing the punnet square

################
# save to file #
################

setwd("/home/qiime/Desktop/TelomereTimeBomb/R")
write.csv(punnet,"punnet.csv")
