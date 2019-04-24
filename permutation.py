//find permutations of a list
def perm(l):
    if (l == []):
        return []
    if (len(l) == 1):
        return l
    out = []
    for i in range(len(l)):
        m = l[i]
        remList = l[:i]+l[i+1:]
        for p in perm(remList):
            out.append(m+p)
    return out
