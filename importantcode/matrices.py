#Energy of a 6 by 6 matrice
import numpy as np
from scipy import linalg as lg

def energy(x1,x2,x3,x4,x5,x6):
    A1 = [x for x in x1]
    A2 = [x for x in x2]
    A3 = [x for x in x3]
    A4 = [x for x in x4]
    A5 = [x for x in x5]
    A6 = [x for x in x6]

    M = np.array([A1,A2,A3,A4,A5,A6])
    
    m1 = lg.eig(M)
    m2 = np.array([m1[0].real])
    m3 = m2.transpose()#m1.transpose()
    res1 = m2.dot(M)
    return res1.dot(m3)

#Using the function to compute energy

Enegy = []

N = len(close.CLOSE) - 6

for i in range(N):
    a = i
    b = i + 6
    #Compute coefficients
    EN = energy(close.c1[a:b], close.c2[a:b], close.c3[a:b], close.c4[a:b], close.c5[a:b], close.CLOSE[a:b])
    Enegy.append(EN[0][0])

#Matrice linear regression
def compute_cofficients(x1,x2,x3,x4,x5,x6,x7):
    forcast = np.array([[x] for x in x7])
    Matrix = np.array([[x for x in x1], [x for x in x2], [x for x in x3], [x for x in x4], [x for x in x5], [x for x in x6]])
    Matrix = Matrix.transpose()
    Inv = lg.inv(Matrix)
    E = lg.eig(Matrix)
    coff = Inv.dot(forcast)
    return coff, Matrix, E

#Using the trained co-efficients to make predictions
def forcast_train(coef, matrx):
    return matrx.dot(coef)

def predict(cof, matrx):
    return matrx.dot(cof)

#Normalize a function
def normalize(x):
    norm = []
    max1 = max(x)
    min1 = min(x)
    for i in x:
        cal = (i-min1)/(max1-min1)
        norm.append(cal)
    return norm