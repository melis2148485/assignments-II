'''A degenerate triangle is a "flat" triangle in the sense that it is contained in a line segment. 
It has thus collinear vertices[3] and zero area. If the three vertices are pairwise 
distinct, it has two 0° angles and one 180° angle. If two vertices are equal, 
it has one 0° angle and two undefined angles. If all three vertices are equal, all three angles are undefined.'''

#we sort the sticks in non-decreasing order to find all possible comninations to form a triangle
#if a+b>c for each stick then it's a triangle
##function decription##
'''Complete the maximumPerimeterTriangle function in the editor below.
maximumPerimeterTriangle has the following parameter(s):
int sticks[n]: the lengths of sticks available
Returns
int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1'''
def maximumPerimeterTriangle(sticks):
    sticks.sort()#sort the stick lengths
    for i in range(len(sticks)-3,-1,-1):#stick has 3 elements to extract( backwards),-1 because at 0 the function stops, the other -1 indicates the backward step
        a,b,c=sticks[i],sticks[i+1],sticks[i+2]
        if a+b>c:#condition to have a triangle
            return [a,b,c]#return sides in non decreasing order
        else:
            return -1
n=5
sticks=[1, 1, 1, 3, 3]
print(maximumPerimeterTriangle(sticks))