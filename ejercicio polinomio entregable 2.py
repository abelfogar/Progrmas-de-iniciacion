import math 
polinomio=[1,-3,4]
a = polinomio[0]    
b = polinomio[1]
c = polinomio[2]
print(a)
print(b)
print(c)
discriminante = b**2-4*a*c
print(discriminante)

if discriminante > 0:
    x1=(-b + math.sqrt(discriminante)) / (2*a)
    x2=(-b - math.sqrt(discriminante)) / (2*a)
    listaRaices = [x1,x2]
    
elif discriminante == 0:
    x1=(-b + math.sqrt(discriminante)) / (2*a)
    listaRaices=[x1]
  
else:
    listaRaices=[]
print(listaRaices)
