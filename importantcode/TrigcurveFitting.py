def sinx(x,k):
    return math.sin(x**k)

def create(k,num):
    x_range = [l for l in range(num)]
    result = [sinx(y, k) for y in x_range]
    starter1 = [100]
    for c in result:
        starter1.append(starter1[-1]+c)
    return starter1

def check_simi(range1, data):
    corr1 = []
    corr2 = []
    k1 = []
    k2 = []
    data1 = []
    data2 = []
    for x in range1:
        creat1 = create(k=x, num = len(data)-1)
        corr = np.corrcoef(data, creat1)[0][1]
        if corr > 0.90:
            corr1.append(corr)
            data1.append(creat1)
            k1.append(x)
        if corr < -0.90:
            corr2.append(corr)
            data2.append(creat1)
            k2.append(x)
    return corr1,corr2,data1,data2,k1,k2

