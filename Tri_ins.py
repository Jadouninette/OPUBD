def Tri_ins(t):
    for k in range(1,len(t)):
        temp = t[k]
        j = k
        while j>0 and abs(temp[0]) > abs(t[j-1][0]):
            t[j] = t[j-1]
            j-=1
        t[j] = temp
    return t
        
            