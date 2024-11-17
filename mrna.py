'''Given: A protein string of length at most 1000 aa.
Return: The total number of different RNA strings from which the protein could have been translated, 
modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)'''
prot_str='MA'
#dictionary to which we associate a certain number of na codons to each aminoacids:number of codons possible
#for each aminoacid
cod_table = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4, 'Stop:codon':3}
count=1
for amino_a in prot_str:
    count= (cod_table [amino_a]*count)%1000000#cod_table gets n of codons for that amino acid, count
    #is the n of total possible rna sequences and we take the result modulo 1000000
count=(cod_table['Stop:codon']*count)%1000000#we alawys have to consider the stop codon in the sequence or 
#the number of codons would be underestimated
print(count)