'''
Task 0.6.6: makeInverseIndex(strlist)
input: list of strings
returns: dictionary that maps each word to the set consisting of the document numbers of documents
in which that word appears. 
'''
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

print(makeInverseIndex(stories))