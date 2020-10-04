def fourier(t,y,num):
    Ak = []
    Bk = []
    Ks = []
    Series = np.mean(y)/2
    for k in range(num):
        a1 = np.dot(y, np.sin((k+1)*t))
        b1 = np.dot(y, np.cos((k+1)*t))
        Series = Series + a1*np.sin((k+1)*t) + b1*np.cos((k+1)*t)
        Ak.append(a1)
        Bk.append(b1)
        Ks.append(k+1)
    return Series, Ak, Bk, Ks


def forcast(t,Ak,Bk,Ks,data):
    Xer = np.mean(data)/2
    for i in range(len(Ks)):
        Xer = Xer + Ak[i]*np.sin((Ks[i])*t) + Bk[i]*np.cos((Ks[i])*t)
    return Xer


def sinosoid(t,y,num):
    Ak = [] #Amplitude
    Ks = [] #Frequencies
    Series = np.zeros(len(y))
    for k in range(num):
        a1 = np.dot(y, np.sin((k+1)*t))
        Series = Series + a1*np.sin((k+1)*t)
        Ak.append(a1)
        Ks.append(k+1)
    return Series, Ak, Ks

def cosisoid(t,y,num):
    Bk = [] #Amplitude
    Ks = [] #Frequencies
    Series = np.mean(y)/2
    for k in range(num):
        a1 = np.dot(y, np.cos((k+1)*t))
        Series = Series + a1*np.cos((k+1)*t)
        Bk.append(a1)
        Ks.append(k+1)
    return Series, Bk, Ks

def euler(t,y,num):
    Ek = [] #Amplitude
    Ks = [] #Frequencies
    Series = np.mean(y)/2
    for k in range(num):
        a1 = np.dot(y, np.e**np.array((t*(k+1))))
        Series = Series + a1*(np.e**np.array(((k+1)*t)))
        Ek.append(a1)
        Ks.append(k+1)
    return Series, Ek, Ks