principal = float(input('Enter amount: '))
t = float(input('Enter time: '))
rate = float(input('Enter rate: '))

si = (float)(principal*t*rate)/100
ci = (float)(principal * ((1+rate/100)**t - 1))

print("Simple interest is:",si)
print("Compound interest is:",ci)