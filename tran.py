'''Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).'''
#For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
# is the ratio of the total number of transitions to the total number of transversions, 
# where symbol substitutions are inferred from mismatched corresponding symbols as when calculating 
# Hamming distance (see “Counting Point Mutations”).
fasta_input1='''>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT'''
fasta_input2='''
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT'''
#transitions:a purine is substituted by another purine and a pyrimidine by another pyrimidine
#ex:A->G or viceversa
# C->T or viceversa
#transvertion:a purine is substituted by a pyrimidine and viceversa
#ex
#A->C
#A->T
#G->C
#G->T
#put them in ratio
def parse_fasta(fasta_input):
    sequence=''
    for line in fasta_input.strip().splitlines():
        if not line.startswith('>'):
            sequence+=line.strip()
    return sequence

def find_ratio(s1,s2):
    transitions={'A':'G','G':'A','C':'T','T':'C'}#for definition of transitions
    transvertions={'A':['C','T'], 'C':['A','G'],'T':['A','G'],'G':['C','T']}
    n_trans=0
    n_transv=0
    for i in range(len(s1)):
        base1=s1[i]
        base2=s2[i]#indices
        if base1!=base2:
            if base1 in transitions and base2==transitions[base1]:#verifies if base2 is partner of base1 as written in the dictionary
                n_trans+=1
            elif  base1 in transvertions and base2 in transvertions[base1]:#verifies if base2 is transvertion of base1 as written in the list
                n_transv+=1
    if n_transv==0:
        return float('inf') if n_trans>0 else 0 #return infinity
    return n_trans/n_transv
s1=parse_fasta(fasta_input1)
s2=parse_fasta(fasta_input2)
fin_ratio=find_ratio(s1,s2)
print(fin_ratio)
    