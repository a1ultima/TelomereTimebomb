# Telomere-Timebomb

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

@@H-locus: consists of two possible alleles: @H and @h. You can engineer the homing component to engineer the target locus of of an organism

@@T-locus: @TODO:@2019-03-01: need to write
.

@@H-allele / @@h-allele / @@Gene conversion: is dominant for the phenotype of 
"@@homing", which, when expressed by a @HEG, causes a conversion of any @h alleles 
in the gamete/diploid cell into an @H allele, at a probability, e, which is commonly 
referred to as the HEG's "@homing rate". This conversion of it's competing wild-type 
h allele for occupancy of the @H-locus is exemplary of "selfish gene" behaviour. Keeping in mind, for our study we target telomerase, i.e. telomerase is h.

@@HEG: ...@todo... Acronym for: @@Homing Endonuclease Gene, a selfish gene that 
simultaneously expresses two phenotypes: (i) @@Homing reaction and (ii) A gene 
@@Knock-out, of a bespoke target gene.

@@Homing Rate (e) / @@Homing reaction / @@Knock-out (@@KO): The @homing reaction 
is a phenotype expressed by the @@H-allele, which causes @gene conversion of 
it's wild-type competitor: @h-allele, to change into a @H-allele, which effectively
@knocks out the @h-allele, turning off it's otherwise expressed phenotype. The 
@HEG can be genetically engineered to target bespoke genes, and hence turn-off 
their phenotypic functionality (K/O). For purposes of this project, the @h-allele targeted 
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
propagate the selfish-@H-alleles within the species' @gene pool, prior to the 
shortening-telomeres' reaching such critically short, lethal lengths, in terms 
of natural selective pressures acting on the telomeres; such silent-propagation
of these - eventually species-dooming - alleles gives the Telomere Timebomb a 
means to overcome the wasteful process of natural selection, common to most 
genetic-engineering-oriented approaches to vector control, such as SIT or RIDL. 


@@telomeres: for simplicity, we @assume every diploid individual carries two 
telomere "alleles" at any time, one originating from said individual's mother 
and the other from said individual's father. The @T-locus: these telomeres occupy 
is N-allelic, where N represents the number of possible @@telomere-lengths (N enumerates({0,1,2,3}) ) said 
individual's species' can harbour. @telomere-length (in generations) is measured 
in terms of numbers-of-generations of telomere shortening that can be experienced
by an N-length-telomere before it reaches a critically short length, under which 
any individual carrying the short-telomere experiances instant death, thus
removing it, and its alleles, from the species's @gene-pool.


@@punnet table / @@gene-pool:

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

@@ @TODO:@2019-03-01:Other punnets

"""
