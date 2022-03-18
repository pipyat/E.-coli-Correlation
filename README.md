# E.-coli-Correlation
# This code was based on a project I carried out at the University of Surrey. The aim was to model E. coli division based on the random sharing of some division factor.
# This approach allows us to control sister-sister and mother-daughter division time correlation - some experimental findings demonstrated a lack of correlation between mothers and daughters but found high sister-sister correlation, as if a genetic dice was thrown upon division.

# On division, N molecules (division factor) are generated via sampling from a Gaussian distribution. These are then shared (via binomial distribution so sharing is unequal) between two cells on division with M transferred into one, and therefore N-M into the other. 
# Division time is then proportional to the number of this molecule inherited as well as some rate, R. 

# Division time correlation can be controlled by altering statistical parameters
