'''
Problem 0.8.1: increments(L)
input: list L of numbers
output: list of numbersw in which the i-th element is one plus the i-th element of L

'''

def increments(L):
    return [k + 1 for k in L]

print(increments([1, 5, 7]))

'''
Problem 0.8.2: cubes(L)
input: list L of numbers
output: list of numbers in which the i-th element is the cube of the i-th element of L.
'''

def cubes(L):
    return [k**3 for k in L]

print(cubes([1, 2, 3]))

'''
Problem 0.8.3: tuple_sum(A, B)
input: lists A and B of the same length, where each element in each list is a pair (x, y) of numbers 
output: list of pairs (x, y) in which the 1st element of the i-th pair is the sum of the first element of the i-th pair in A and the first element of the i-th pair in B

'''
def tuple_sum(A, B):
 pass
