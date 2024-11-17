'''Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings 
exist, then you may return any one of them.)'''
fasta_input='''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
'''
#parse fasta file to extract dna strings and put sequences into a list named sequences
def parse_fasta(fasta_input):
    sequences=[]#list for extracted sequences
    curr_seq=[]#temporary list
    for line in fasta_input.splitlines():
        line=line.strip()
        if line.startswith('>'):
            if curr_seq:
                sequences.append(''.join(curr_seq))
                curr_seq=[]
        else:
            curr_seq.append(line)#if it's a sequence line it's added
    if curr_seq:
        sequences.append(''.join(curr_seq))#if at the end, it still stores sequences, they are added to the final list
    return sequences

#profile matrix
def prof_mat(sequences):
    length=len(sequences[0]) 
    profile={'A':[0]*length,#initialize dictionary with zero for each position of sequence
             'C':[0]*length,
             'G':[0]*length,
             'T':[0]*length}
    for seq in sequences:
        for i in range(len(seq)):
            nucleotide=seq[i]
            profile[nucleotide][i]+=1#each time checks position to see if nucleotide is present and is added
    return profile
#write consensus sequence 
def cons_string(profile):
    consensus=''#initialize empty string for consesous sequence
    for i in range(len(profile['A'])):
        nucleotide_max=max(['A','C','G','T'],key=lambda x:profile[x][i])#nucleotide with highest count in prof matrix
        consensus+=nucleotide_max#that nucleotide is added to consensus string
    return(consensus) 
sequences=parse_fasta(fasta_input)
profile=prof_mat(sequences)
consensus=cons_string(profile)
print(consensus)
for nucleotide in ['A','C','G','T']:
    print(f"{nucleotide}:{' '.join(map(str, profile[nucleotide]))}")