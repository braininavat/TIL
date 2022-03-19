abcd = list(map(int,input().split()))
result = 1e9
def dist(t):
    x1 = abcd[0]+(abcd[2]-abcd[0])*t
    x2 = abcd[4]+(abcd[6]-abcd[4])*t
    y1 = abcd[1]+(abcd[3]-abcd[1])*t
    y2 = abcd[5]+(abcd[7]-abcd[5])*t
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def tsearch(start,end):
    global result
    if end - start <= 10**-10:
        return
    midlo = start+(end-start)/3
    midhi = start+2*(end-start)/3
    distlo = dist(midlo)
    disthi = dist(midhi)
    result = min(distlo,disthi,result)
    if distlo > disthi:
        tsearch(midlo,end)
    else:
        tsearch(start,midhi)
        

tsearch(0,1)
print("{:.10f}".format(result))
