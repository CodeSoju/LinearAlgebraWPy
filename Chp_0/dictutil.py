from imp import reload

def dict2List(dct, kl):
    return [v for (k,v) in dct.items() for i in kl if i==k] 

def list2dict(L, kl):
    return {k:v for k,v in zip(kl, L)}

def listrange2dict(L):
    return {k:v for k in range(len(L)) for v in L if v == L[k]}

print(listrange2dict(['A', 'B', 'C']))
