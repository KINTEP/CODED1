def logistic_map3(x, r):
    return r*x*(1.00 - x)

def make_list(val, r1, n):
    data = [val]
    
    for _ in range(n):
        data.append(logistic_map3(x=data[-1], r = r1))
    return data

big_data = []
R = np.linspace(1,4,1000)
vali = 0.5

for rv in R:
    big_data.append(make_list(val = vali, r1 = rv, n = 1000)[-100:])