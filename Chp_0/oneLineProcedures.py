#Comprehensions that iterate over the dictionaries
'''
You can write list comprehensions that iterate over the keys or the values of a dictionary
using keys() and values()

'''
x = [2*x for x in {4:'a', 3:'b'}.values()]
#print(x)

'''
Given two dictionaries A and B, you can write comps that iterate over the 
union or intersections of the keys, using union opertor '|' and intersection
operator '&' we learned about in Section 0.5.4
'''
y = [k for k in {'a': 1, 'b': 2}.keys() | {'b':3, 'c': 4}.keys()]
#print(y)

'''
Often you'll want a comprehension that iterates over the (key, value) pairs of a dictionary
using items(). Each pair is a tuple 
'''

'''
TASK 0.5.26: Suppose d is a dictionary that maps some employee IDs (a subset
of the integers from 0 to n-1) to salaries. Suppose L is an n-element list whose i-th element is
the name of employee number i. Write a comp whose value is a dictionary mapping employee names to salaries
'''
#test data
id2Salary = {0:1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', 'Moe']

z = {name:salary for name,salary in zip(names, id2Salary.values())}
#print(z) 

'''
TASK 0.5.28: Define a OLP nextInts(L) specified as follows:
'''
def nextInts(lst):
    return [x + 1 for x in lst]

#print(nextInts([1,5,7]))

'''
T 0.5.29: cube the elements in a list
'''
def cubeLst(lst):
    return [x**3 for x in lst]

#print(cubeLst([1, 2, 3]))

'''
T 0.5.30: dict2list(dct, keylist)
'''
def dict2List(dct, kl):
    return [v for (k,v) in dct.items() for i in kl if i==k] 


dit = {'a':'A', 'b':'B', 'c':'C'}
kl = ['b', 'c', 'a']
print(dict2List(dit, kl))

'''
T 0.5.31: list2dict(L, keylist)
'''
def list2dict(L, kl):
    return {k:v for k,v in zip(kl, L)}

innie = ['A', 'B', 'C']
keyL = ['a', 'b', 'c']
#print(list2dict(innie, keyL))
