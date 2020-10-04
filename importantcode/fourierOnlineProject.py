#This section fits a polynomial of degree 1 to the curve
x = 253
xlist = [x for x in range(x)]
valueonly= data.CLOSE[:x]

pl  = polyfit(xlist, valueonly,1)
plvals = polyval(pl, xlist)
plt.plot(valueonly, label = "actual")
plt.plot(plvals, label = "pred")
plt.ylabel('Stock Value (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.title('Tesla Stock Data (USD) With Least Mean Square Polynomial of Degree 1')
plt.legend()
plt.show() 
print('The equation of the least mean square line is \ny = '+ str(round(pl[0],3))+ 'x'+' + '+str(round(pl[1],3)))

#This section fits a polynomial of degree 2 to the curve
pl2  = polyfit(xlist, valueonly,2)
plvals2 = polyval(pl2, xlist)
plt.plot(valueonly, label = "actual")
plt.plot(plvals2, label = "pred")
plt.ylabel('Stock Value (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.title('Tesla Stock Data (USD) With Least Mean Square Polynomial of Degree 2')
plt.legend()

plt.show()
print('The equation of the least mean square line is \ny = '+ str(round(pl2[0],3))+ 'x^2'+' + '+str(round(pl2[1],3))+'x'+' + '+str(round(pl2[2],3)))

#This section fits a polynomial of degree 3 to the curve
pl3  = polyfit(xlist, valueonly,3)
plvals3 = polyval(pl3, xlist)
plt.plot(valueonly, label = "actual")
plt.plot(plvals3, label = "pred")
plt.ylabel('Stock Value (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.title('Tesla Stock Data (USD) With Least Mean Square Polynomial of Degree 3')
plt.legend()

plt.show()
print('The equation of the least mean square line is \ny = '+str(round(pl3[0],3))+ 'x^3'+' + '+ str(round(pl3[1],3))+ 'x^2'+' + '+str(round(pl3[2],3))+'x'+' + '+str(round(pl3[3],3)))

#This section fits a polynomial of degree 1 to the curve
pl4  = polyfit(xlist, valueonly,4)
plvals4 = polyval(pl4, xlist)
plt.plot(valueonly, label = "actual") 
plt.plot(plvals4, label = "pred")
plt.ylabel('Stock Value (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.title('Tesla Stock Data (USD) With Least Mean Square Polynomial of Degree 4')
plt.legend()
plt.show()
print('The equation of the least mean square line is \ny = '+str(round(pl4[0],3))+ 'x^4'+' + '+str(round(pl4[1],3))+ 'x^3'+' + '+ str(round(pl4[2],3))+ 'x^2'+' + '+str(round(pl4[3],3))+'x'+' + '+str(round(pl4[4],3)))

#This section computes the absolute mean error between the poly fit of degree 1 and the actual prices
z = 0
diff1 = []
avg = 0

while z<200:
    diff1.append(valueonly[z]-plvals[z])
    avg += abs(diff1[z])
    z+=1

plt.plot(diff1)
plt.title('Difference Between Least Mean Square of Degree 1 and Stock Data (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

plt.show()
print('\n' + 'The average difference between the least mean square prediction and the stock price is ' + str(round(avg/253,3)))

#This section computes the absolute mean error between the poly fit of degree 2 and the actual prices
w = 0
diff2 = []
avg = 0

while w<200:
    diff2.append(valueonly[w]-plvals2[w])
    avg += abs(diff2[w])
    w+=1

plt.plot(diff2)
plt.title('Difference Between Least Mean Square of Degree 2 and Stock Data (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

plt.show()
print('\n' + 'The average difference between the least mean square prediction and the stock price is ' +str(round(avg/253,3)))

#This section computes the absolute mean error between the poly fit of degree 3 and the actual prices
u = 0
diff3 = []
avg = 0

while u<200:
    diff3.append(valueonly[u]-plvals3[u])
    avg += abs(diff3[u])
    u+=1

plt.plot(diff3)
plt.title('Difference Between Least Mean Square of Degree 3 and Stock Data (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

plt.show()
print('\n' + 'The average difference between the least mean square prediction and the stock price is ' +str(round(avg/253,3)))

#This section computes the absolute mean error between the poly fit of degree 4 and the actual prices
n = 0
diff4 = []
avg = 0

while n<200:
    diff4.append(valueonly[n]-plvals4[n])
    avg += abs(diff4[n])
    n+=1

plt.plot(diff4)
plt.title('Difference Between Least Mean Square of Degree 4 and Stock Data (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')
plt.show()
print('\nThe average difference between the least mean square prediction and the stock price is ' +str(round(avg/253,3)))

#This section computes the fourier co-eeficients and plots and amplitude

print('\nGiven the forth degree polynomial had the smallest average error, we will use this difference moving forward')

plt.title('Abs(FFT) of the Difference Between Least Mean Squareand Stock Data First 200 Days(USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('FFT')
W = fft(diff4);
plt.plot(abs(W))
plt.show()

Y = W
plt.title('Difference Between IFFT of the ABS(FFT)\n and the Original stock difference (USD)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

Z = ifft(Y);
ifftdiff = [];

for i in range(200):
    ifftdiff.append(diff4[i]-Z[i])

plt.plot(ifftdiff)
plt.show()

plt.title('FFT of Difference Using the First Eight Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('FFT')

Y8 = []

for i in range(200):
    if i<8:
        Y8.append(abs(Y[i]))
    else:
        Y8.append(0)

plt.plot(Y8)
plt.show()

plt.title('FFT of Difference Using the First Ten Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('FFT')
Y10 = []

for i in range(200):
    if i<10:
        Y10.append(abs(Y[i]))
    else:
        Y10.append(0)

plt.plot(Y10)
plt.show()

plt.title('FFT of Difference Using the First Twelve Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('FFT')

Y12 = []

for i in range(200):
    if i<12:
        Y12.append(abs(Y[i]))
    else:
        Y12.append(0)

plt.plot(Y12)
plt.show()

plt.title('IFFT for FFT Using First 8 Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

ifft8 = ifft(Y8)
plt.plot(ifft8)
plt.show()

plt.title('IFFT for FFT Using First 10 Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

ifft10 = ifft(Y10)
plt.plot(ifft10)

plt.show()

plt.title('IFFT for FFT Using First 12 Points')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

ifft12 = ifft(Y12)
plt.plot(ifft12)

plt.show()

plt.title('IFFT for FFT Using Only Points That \nare Larger Than 5 Percent of the First Point')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

Yfive = abs(fft(diff4))

for i in range (200):
    if Yfive[i] < (Yfive[0]*.05):
        Yfive[i] = 0

plt.plot(ifft(Yfive))
plt.show()

plt.title('IFFT for FFT Using Only Points That \nare Larger Than 10 Percent of the First Point')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

Yten = abs(fft(diff4))

for i in range (200):
    if Yten[i] < (Yten[0]*.1):
        Yten[i] = 0

plt.plot(ifft(Yten))
plt.show()

plt.title('IFFT for FFT Using Only Points That \nare Larger Than 15 Percent of the First Point')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

Yfift = abs(fft(diff4))

for i in range (200):
    if Yfift[i] < (Yfift[0]*.15):
        Yfift[i] = 0

plt.plot(ifft(Yfift))
plt.show()

plt.title('IFFT for FFT Using the First 8 Points Minus Original Difference')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

eightdiff = ifft8-diff4
plt.plot(eightdiff)
plt.show()

plt.title('IFFT for FFT Using Only Points That are Larger Than 5 Percent\n of the First Point Minus the Original Difference')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Difference in Price (USD)')

tendiff = ifft(Yten) - diff4
plt.plot(tendiff)
plt.show()

def predict(YY,inputfft):
    a = []
    b = []
    
    for i in range(253):
        YY.append(0)
        
    for n in range(200,253):
        YY[n]=0
        
        for k in range(200):
            a.append( np.real (inputfft[k]))
            b.append(-1*np.imag(inputfft[k]))
            omk = 2*pi*(k-1)/200
            YY[n] = YY[n]+a[k]*cos(omk*(n-1))+b[k]*sin(omk*(n-1))   
        YY[n] = -YY[n]/200
    
    for i in range (200):
        YY[i] = diff4[i]
    
    return YY


final = []

for i in range(253):
    final.append(plvals4[i]+predict([],Yten)[i])

plt.plot(valueonly, 'g')
plt.plot(final, 'r')
plt.title('Actual Stock (green) vs Prediction using values that are\n greater than 10% of the first value (red)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Stock Price (USD)')

plt.show()

avgfinal1 = 0

for i in range (200,253):
    avgfinal1 += abs(valueonly[i]-final[i])

print ('The average difference between the predicted and actual values is ' + str(round(avgfinal1/53,3))+' dollars')
plt.show()

a = []
b = []
x = []

for i in range(253):
    x.append(0)

for n in range(200,253):
    x[n]=0
    
    for k in range(200):
        a.append( np.real (Y10[k]))
        b.append(-1*np.imag(Y10[k]))
        omk = 2*pi*(k-1)/200
        x[n] = x[n]+a[k]*cos(omk*(n-1))+b[k]*sin(omk*(n-1))   
        
    x[n] = -x[n]/200

for i in range (200):
    x[i] = diff4[i]

final2 = []

for i in range(253):
    final2.append(plvals4[i]+x[i])
    
plt.plot(valueonly, 'g')
plt.plot(final2, 'r')
plt.title('Actual Stock (green) vs Prediction using the first 10 digits (red)')
plt.xlabel('Business Days Since 8/3/2017')
plt.ylabel('Stock Price (USD)')
plt.show()

avgfinal1 = 0

for i in range (200,253):
    avgfinal1+= abs(valueonly[i]-final2[i])

print ('The average difference between the predicted and actual values is ' + str(round(avgfinal1/53,3))+' dollars')