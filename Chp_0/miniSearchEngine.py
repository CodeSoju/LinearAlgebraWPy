'''
Task 0.6.6: makeInverseIndex(strlist)
input: list of strings
returns: dictionary that maps each word to the set consisting of the document numbers of documents
in which that word appears. 
'''
from collections import defaultdict

f = open('stories_small.txt')
stories = list(f)

def makeInverseIndex(strlist):
    keys = []
    values = []

    for x in strlist:
        temp = x.split()
        keys += temp 
    keys = list(set(keys))

    for i in keys:
        value = []
        for n in range(len(strlist)):
            for e in strlist[n].split(' '):
                if e == i:
                    value.append(n)
        values.append({x for x in value})
    mydict = {}

    for i in range(len(keys)):
        mydict[keys[i]] = values[i]
    return mydict

#print(makeInverseIndex(stories))

#enumerate
'''
Often, when dealing with iterators, we also get a need to keep a count of iterations. Enumerate() method adds a counter to an iterable and return 
it in a form of enumerating object can then be used directly for loops or converted into a list of tuples using the list() method

enumerate(iterable, start=0)
'''

def makeInverseIndexEnum(strlist):
    keys = []
    values = []
    
    for x in strlist:
        temp = x.split()
        keys += temp
    keys = list(set(keys))
    print(keys)
    
    D = {}
    for i, s in enumerate(keys):
        D.setdefault(s, set()).add(i)

    print(D)

print(makeInverseIndexEnum(stories))