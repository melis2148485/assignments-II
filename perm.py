'''Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations 
(in any order).'''
from itertools import permutations
n=3
#A permutation of length n is an ordering of the positive integers {1,2,…,n}
#For example, π=(5,3,2,1,4) is a permutation of length 5.

#1 generate all possible permutations of the integer
#return the total number of permuations
#list all permutations
def generate_perm(nums):
    if len(nums)==0:#base case-list empty return an empty list
        return[]
    if len(nums)==1:#if list has one element return a list containing one element
        return[nums]
    permutations=[]#list to store permutations
    for i in range(len(nums)):
        curr=nums[i]#extract current element
        remaining=nums[:i]+nums[i+1:]
        for p in generate_perm(remaining):
            permutations.append([curr]+p)
    return(permutations)
numbers=list(range(1,n+1))
all_permutations=generate_perm(numbers)
print(len(all_permutations))
for perm in all_permutations:
    print(' '.join(map(str, perm)))