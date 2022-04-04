#Ömer ÇİÇEK 170401047
#Github Link:https://github.com/omercicek99/Programming-Lab/tree/master/Odev_3
from sympy import Symbol,exp,pprint
import sys
import matplotlib.pyplot as plt

#Grağini çizeceğimiz fonksiyon Üstel Dağılım(Exponential Distribution) 'dır.Olasılık kuramı ve istatistik bilim dallarında üstel dağılımı bir sürekli olasılık dağılımları grubudur.
# Sabit ortalama değişme haddinde ortaya çıkan bağımsız olaylar arasındaki zaman aralığını modelleştirirken bir üstel dağılım doğal olarak ortaya çıkar.
#Grafiği önerilen veya istediğiniz değerleri girerek çizdirebilirsiniz...
#        |λ.e^-λ.x   ,  x>=0, |
#f(x:λ)= |                    |
#       |   0       ,  x<0.  |
# "pprint(exponential_distribution)" komutuyla fonksiyonu yazdırabilirsiniz...
x=Symbol('x')
lambda_=Symbol('lambda')
#print('\u03BB')
exponential_distribution=lambda_*exp(-lambda_*x) ### Exponential Distribution fonksiyonunu gerekli değişkenleri tanımlayarak oluşturuyoruz.
print("Grafiği çizilecek fonksiyon denklemi:\n")
pprint(exponential_distribution)                ### Bu komutla fonksiyonu günlük matematik diliyle yazdırabiliriz.
print("Lütfen sırasıyla x değerlerinin aralığını giriniz:       Önerilen aralık:0-5")
a=int(input())
b=int(input())
print("Önerilen lambda değerinden birini giriniz: 1/2   1   3/2  ")
lambda_deger=input()
x_deger=[]
y_deger=[]
for deger in range(a,b+1):
    y=exponential_distribution.subs({lambda_:lambda_deger,x:deger}).evalf() ### Döngü içerisinde verilen değerlerle y değerini hesaplıyoruz...
    x_deger.append(deger)                                                   ### Gerekli x değerlerini diziye atıyoruz...
    y_deger.append(y)                                                       ### Hesaplanan y değerlerini diziye atıyoruz...
plt.plot(x_deger,y_deger)  ### Grafiği çizdirmek için  x ve y değerlerinin bulunduğu dizileri parametre olarak giriyoruz...
plt.show()                 ### Grafiği ayrı pencerede gösterir...
