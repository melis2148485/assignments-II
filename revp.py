'''Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
You may return these pairs in any order.'''
#identify all substrings of length between 4-12 that are reverse palyndromes
#for each rev pal, return its position(starting at 1)and length
#parse fasta input into a string
fasta_input='''>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
'''
def parse_fasta(fasta_input):
    sequence=''
    for line in fasta_input.strip().splitlines():
        if not line.startswith('>'):
            sequence+=line.strip()
    return sequence
#sequence=parse_fasta(fasta_input)
#print(sequence)
def reverse_complement(dna_sequence):
    complement = {'A':'T','T':'A','C':'G','G':'C'}#dixtionary complement to map each dna base to its complement
#    #reversed function to return string in reversed:we iterate for each base in string then we find complement using dictionary
    return ''.join(complement[base]for base in reversed(dna_sequence))

#check stubsrings of desired length
def find_reversed_palindromes(dna_str):
    result=[]
    n=len(dna_str)
    for length in range(4,13):
        for i in range(n-length+1):
            substr=dna_str[i:i+length]
            rev_compl=reverse_complement(substr)
            if substr==rev_compl:
                result.append((i+1,length))
    return result
dna_string=parse_fasta(fasta_input)
palindromes=find_reversed_palindromes(dna_string)
for position, length in palindromes:
    print(position,length)
        



                