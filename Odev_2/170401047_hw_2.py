import sys

#İşçilerin çıkış aylarına göre histogram biligisini oluşturup medyanını ve ortalamasını bulan kod
deneme=open(sys.argv[1]+'/input_hw_2.csv','r')
liste=[]
liste2=[]
liste3=[]
aylistesi=[]
for a in deneme:###Dosyadaki ";" işaretine göre ayırıyoruz
    for word in a.lower().split(";"):
        liste.append(word)
#print(liste)
boy=len(liste)
#print(boy)

for i in range(3,boy+1,4): ###"   " göre ayırıyoruz
    x=liste[i].split()
    for j in range(0,2):
        liste2.append(x[j])
#print(liste2)

for c in range(0,len(liste2),2):###"-" göre ayırıyoruz
    y=liste2[c].split("-")
    for e in range(0,3):
        liste3.append(y[e])
#print(liste3)

for f in range(1,len(liste3),3): ###Ay kısımlarını alıp diziye atıyoruz
    aylistesi.append(liste3[f])
#print(aylistesi)

aysözlüğü=dict()###Ay listesindeki ay sayılarına göre histogram bilgisi oluşturuyoruz
for z in aylistesi:
    if z in aysözlüğü:
        aysözlüğü[z] += 1
    else:
        aysözlüğü[z] = 1
#print(aysözlüğü)

toplam=0 ###Ortalamayı buluyoruz
liste4=[]
for g in aysözlüğü.values():
    toplam=toplam+g
    liste4.append(g)
ortalama=toplam/len(aysözlüğü.values())
int(ortalama)
#print(ortalama)
#print(liste4)

n=len (liste4)###Listenin medyanını bulmak için sıralıyoruz
for i in range (0,n):
    kucuk=liste4[i]
    for j in range (i+1,n):
        if(liste4[j]<=kucuk):
            kucuk=liste4[j]
            indis=j
    if(kucuk!=liste4[i]):
        temp=liste4[i]
        liste4[i]=liste4[indis]
        liste4[indis]=temp
    #print(liste4)
sortedlist=liste4

c=len(sortedlist)###Sıralanmış listenin  medyanını buluyoruz
if (c % 2 == 1):
    middle = int(n / 2) + 1
    median = sortedlist[middle - 1]
else:
    middle_1 = int(n / 2) - 1
    middle_2 = middle_1 + 1
    median = (sortedlist[middle_1] + sortedlist[middle_2]) / 2
#print(median)

dosya=open(sys.argv[2]+"/170401047_hw_2_output.txt","w")
dosya.write("ortalama")
dosya.write("  ")
dosya.write(str(ortalama))
dosya.write("\n")
dosya.write("medyan")
dosya.write("  ")
dosya.write(str(median))
