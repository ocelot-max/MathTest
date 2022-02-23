def getYin(n,t):
    r = 1
    for i in range(n):
        if n%(i+1)==0:
            r+=1
        if r==t:
            return (i+1)
    return -1
print(getYin(16,1))
