def flatten(seq):
    newone =[]
    for a in seq:
        if isinstance(a,(list,tuple)):
            newone.extend(flatten(a))
        else:
            newone.append(a)
    return newone

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(seq))
