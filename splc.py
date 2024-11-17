'''Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. 
(Note: Only one solution will exist for the dataset provided.)'''
fasta_input='''>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
'''

#parse fasta input into a list of sequences
def parse_fasta(fasta_input):
    lines=fasta_input.strip().split('\n')
    sequences=[]
    curr_seq=None
    for line in lines:
        if line.startswith('>'):
            if curr_seq:
                sequences.append(curr_seq)
            curr_seq=''#to extract dna sequence
        else:
            curr_seq+=line.strip()#append dna sequence line to current sequence, because the line doesn't
            #start with > we must not exclude the last sequence, so
    if curr_seq:
        sequences.append(curr_seq)   
    return sequences
#remove sequences of introns
def remove_introns(dna,introns):
    for intron in introns:
        dna=dna.replace(intron,'')
    return dna
#dna->rna
def transcribed(dna):
    return dna.replace('T','U')
#we transform the rna codon table into a dctionary where the keys are the triplets and the values is the symbol of the corresponding
#protein
rna_codon_table='''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''
tokens=rna_codon_table.split()
rna_codon_dict={}
for i in range(0,len(tokens),2):#by 2 we want the loop to work with 2 items at a time, so the triplet and the amino acid symbol
    codons=tokens[i]
    amino_acid=tokens[i+1]
    rna_codon_dict[codons]=amino_acid
def translate(rna):
    protein=''
    for i in range(0,len(rna), 3):#code reads through each codon, a set of 3 rna bases in the rna sequence
        codon=rna[i:i+3]
        if codon in rna_codon_dict:
            amino_acid=rna_codon_dict[codon]
            if amino_acid=='Stop':
                break
                #for each 3-base segment, if the aminoacid is not stop, the aminoacid is added to the protein(all stop codons are skipped)
            protein += amino_acid
    return(protein)
#parse fasta input
sequences=parse_fasta(fasta_input)
dna_sequence=sequences[0]
introns=sequences[1:]
#remove introns
exons=remove_introns(dna_sequence,introns)
rna=transcribed(exons)
protein=translate(rna)
print(protein)