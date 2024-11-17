'''Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we begin with Tom, 
who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, 
each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family 
tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.'''
#following mendel's second law, each gene has the ame probability of producing 1 of 4 possible combinations,so
#AaBb 25%
#Aabb 25%
#aaBb 25%
#aabb 25%
#the number of AaBb children in the 2k generation follows a binomial distribution, so
from math import comb
k=2 
N=1
def prob_of_N(k,N):
    total_children=2**k#children in tot in k generation
    p=0.25 #prob organism being AaBb
    prob=0
    for x in range(N):
        prob+=comb(total_children,x)*(p**x)*((1-p)**(total_children-x))#formula bin coefficient
    return 1-prob#complement to find P(X>=N)
result=prob_of_N(k,N)
print(result)
