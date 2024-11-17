'''Given: A collection of k(k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any 
single solution.)'''
fasta_input='''>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA'''
#parse fasta file to extract dna strings
def parse_fasta(fasta_input):
    lines=fasta_input.strip().split('\n')
    sequences=[]
    curr_seq=''
    for line in lines:
        if line.startswith('>'):
            if curr_seq:
                sequences.append(curr_seq)
            curr_seq=''#to extract dna sequence
        else:
            curr_seq+=line.strip()#append dna sequence line to current sequence, because the line doesn't
            #start with >
        #we must not exclude the last sequence, so
    if curr_seq:
        sequences.append(curr_seq)   
    return sequences
#function to find the longest substring
def find_subs(dna_seq):
    smallest_seq=min(dna_seq, key=len)
    n=len(smallest_seq)
    for length in range(n,0,-1):#checking from largest to smallest substring
        for start in range(n-length+1):#check for all sunstrings of CURRENT length
            common_match=smallest_seq[start:start+length]
            if all(common_match in dna for dna in dna_seq):
                return common_match
    return ''
dna_sequences=parse_fasta(fasta_input)
result=find_subs(dna_sequences)
print(result)
