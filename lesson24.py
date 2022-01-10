import sys

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

if a == 0: sys.exit()

D = (b * b) - (4 * a * c)
if D < 0: print('No real roots')
elif D == 0: 
    x = -b/(2 * a)
    print(f'x={x}')
else:
    x1 = (-b + D ** 0.5)/(2 * a)
    x2 = (-b - D ** 0.5)/(2 * a)
    print(f'x1={x1}')
    print(f'x2={x2}')