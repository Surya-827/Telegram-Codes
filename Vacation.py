import sys

 

try:

t = int(input())

virus_length = int(input())

virus_rna = input()

vaccines = []

vaccines_length = []

reactions = []

virus_g = virus_rna.count('G')

virus_c = virus_rna.count('C')

for _ in range(t):

vaccine_length = int(input())

vaccine_rna = input()

vaccine_g, vaccine_c = vaccine_rna.count('G'),vaccine_rna.count('C')

reaction = vaccine_c*virus_g + vaccine_g * virus_c

vaccines.append(vaccine_rna)

vaccines_length.append(vaccine_length)

reactions.append(reaction)

 

highest_reactive = max(reactions)

final_vaccine = vaccines[reactions.index(highest_reactive)]

if( reactions.count(highest_reactive) >1):

for i in range(len(reactions)):

if(reactions[i] == highest_reactive):

if(len(final_vaccine) > vaccines_length[i]):

final_vaccine = vaccines[i]

print(vaccines.index(final_vaccine)+1)

 

 

except:

print("Error :", sys.exc_info()[1])

Vaccination code
