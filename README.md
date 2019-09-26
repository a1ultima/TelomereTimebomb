# Telomere-Timebomb

##########
# Readme #
##########

#############################
# Team Allocation (Authors) #
#############################

# @H1 - Vic Chang - https://www.linkedin.com/in/vic-chang-9a7600176/

# @H2 - Eric Tam - https://www.linkedin.com/in/chon-teng-tam-2b4667166/

# @H3 - Amol Dhaliwal - @TODO
#     & Hemat Sanaie -  @TODO



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


@@punnet table / @@gene-pool (use a real code editor to see proper formatting, like vim, emacs or ST*):

  vvv--- Possible @@gamete genotypes ---vvv

       pi=0  pi=1   pi=2  pi=3  qi=0 qi=1  qi=2  qi=3   <-- alt. symbol for @gamete genotypes
_______________________________________________________
|[0/0]| HT0 | HT1 | HT2 | HT3 | hT0 | hT1 | hT2 | hT3 | 
|_____|_[1]_|_[2]_|_[3]_|_[4]_|_[5]_|_[6]_|_[7]_|_[8]_| 
|HT0[1]  x  |  x  |  x  |  x  |  x  |  x  |  x  |  x  | pj=0
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|HT1[2]  x  |     |     |     |  x  |     |     |     | pj=1
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|HT2[3]  x  |     |Case2|     |  x  |     |Case1a     | pj=2
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|HT3[4]  x  |     |     |     |  x  |     |     |     | pj=3
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|hT0[5]  x  |  x  |  x  |  x  |  x  |  x  |  x  |  x  | qj=0
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|hT1[6]  x  |     |     |     |  x  |     |     |     | qj=1
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|hT2[7]  x  |     |Case1b     |     |  x  |Case3|     | qj=2
|_____|_____|_____|_____|_____|_____|_____|_____|_____|
|hT3[8]  x  |     |     |     |  x  |     |     |     | qj=3
|_____|_____|_____|_____|_____|_____|_____|_____|_____|

#
# pipeline map 
#

phase 1 (Vic & Eric):  create punnet squares (manually), adn generate a set of equations for phase 2

note: there is an odf equivalent of derivations/dominant lethal - recessive shortening - todo/Det_eqns_assm_dominant-lethal_recessive-shortening.docx

	manually create the punnet square outputting into .csv format

data out:

	derivations/dominant lethal - dominant shortening - done/MW_Det_eqns_310714.docx

	derivations/dominant lethal - recessive shortening - double-check/Det_eqns_assm_dominant-lethal_recessive-shortening.docx

	derivations/dominant lethal - recessive shortening - todo/Det_eqns_assm_dominant-lethal_recessive-shortening.docx

phase 2 (Daniel): collapseGametes_to_collectPunnetGametes.py

	collapses the punnet square

data in: 

	Manually create a new csv for the second modelling assumption (refer to ./R/punnet.csv)

data out: 

	Collapsing new punnet tsv from the input (refer to punnet_collapsed.tsv)

phase 3 (Eric): collapseGames_to_collectPunnetGametes.py 

	represent equations using numpy/sympy

data in: 

	punnet_collapsed.tsv

data out: 

	final_gamete_frequencies.tsv 

phase 3 (Vic): use the output of phase 3 to simulate the time evolution of the mosquito population

data in: 

	final_gamete_frequencies.tsv

data out: 

	/plots/*


#
# pipeline map (old (r))
#

phase 1 (Vic & Eric):  create punnet squares (manually)

	manually create the punnet square outputting into .docx format

data out:

	derivations/dominant lethal - dominant shortening - done/MW_Det_eqns_310714.docx

	derivations/dominant lethal - recessive shortening - double-check/Det_eqns_assm_dominant-lethal_recessive-shortening.docx

	derivations/dominant lethal - recessive shortening - todo/Det_eqns_assm_dominant-lethal_recessive-shortening.docx

phase 2 (Vic & Eric): @todo: determine what scripts perform collapsing

	@2019-04-09 : it turns out the description for phase 2 is deprecated OR the input data is incorrect // old: collapse punnet square

	@todo: urgent testing hypothesis 1 the LHS of OR:
		@H1 

	@todo: urgent testing hypothesis 2 on the RHS of OR: 
		@H2 

data in: 

@todo: determine what the inputs are for the collapsing script


data out: 

	punnet_collapsed.tsv



phase 3 (Eric): Python/collapseGames_to_collectPunnetGametes.py 

	generate equations using numpy
	- dominant lethal / recessive shortening
	- dominant lethal / dominant shortening
	- recessive lethal / recessive shortening
	- recessive lethal / dominant shortening


data in: 

	punnet.csv

data out: 

	punnet_collapsed.tsv

phase 4 (Vic): use the output of phase 3 to simulate the time evolution of the mosquito population

data in: 

	final_gamete_frequencies.tsv

data out: 

	/plots/*

# @H1


phase 5: (R/gameteFreq_to_Punnet.r)

	producing plots from mathmatical equations

data in: 

	punnet_collapsed.tsv (large matrix of numpy)

data out:

	/plots/*

# Master
"""
