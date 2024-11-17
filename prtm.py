'''Given: A protein string Pof length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.'''
prot_str='SKADYEK'
mass_table='''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 
'''
#transform in a dictionary where key=proteins  and values=weights
tokens=mass_table.split()
mass_dict={}
for i in range (0,len(tokens), 2):
    protein=tokens[i]
    weight=tokens[i+1]
    mass_dict[protein]=weight

for key in mass_dict:
    mass_dict[key]=float(mass_dict[key])
weight_tot=0.0
for amino_acid in prot_str:
    weight_tot+=mass_dict[amino_acid]

round_weight=round(weight_tot,3)
print(round_weight)