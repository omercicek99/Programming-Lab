#Bir pdf grafiğinde belirtilen aralıkda ortalama değerin olma olasılığı...
from sympy import Symbol,exp,sqrt,pi,Integral
x=Symbol('x')
p=exp(-(x-10)**2/2)/sqrt(2*pi)
print(Integral(p,(x,11,12)).doit().evalf())

--->#0.135905121983278
