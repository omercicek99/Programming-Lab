#Herhangi bir fonksiyonun türev tanımını kullanarak türevini alır...
from sympy import Symbol,Limit

x=Symbol('x')
fx=4*x**3+2*x**2+4*x
x1=Symbol('x1')
delta_x=Symbol('delta_x')
fx1=fx.subs({x:x1})
fx1_delta=fx.subs({x:x1+delta_x})
print(Limit((fx1_delta-fx1)/delta_x,delta_x,0).doit())

#-->12*x1**2 + 4*x1 + 4