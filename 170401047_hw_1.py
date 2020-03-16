#input.txt dosyasından kelimeleri tespit edip frekans çıkartır ve size en yüksek frekanslı kelimeyi önerir...
#Önerilern kelimelerle birlikte yeni bir dosyaya yazdırır

def oneri(p,list):
    boy=len(list)
    x=0
    for i in range(0,boy):
        if list[i] in p:
            if(p[list[i]]>x):
                x=p[list[i]]
                string=list[i]
    return string
def dizi_yazdirma(dizi):
    for i in range(0,len(dizi)):
        f.write(dizi[i])
        f.write("  ")
sozluk=dict()
sozluk2=dict()
sozluk3=dict()
sozluk4=dict()
sozluk5=dict()
deneme=open('input.txt','r')
liste=[]
for i in range(1,11):
    f= open(str(i)+'.txt','r')
    for a in f:
        for word in a.lower().split():
            liste.append(word)
    #print(liste)
    boy=len(liste)
    #print(boy)
print(liste)
for s in deneme:
        #print(s)
        liste2=[]
        uzunluk=0
        for kelime in s.lower().split():
            liste2.append(kelime)
        uzunluk=len(liste2)
        for c in range(0,boy):
                if(uzunluk>5):
                    print("5 ten fazla kelime girmeyiniz......")
                if(uzunluk==1):
                    if(liste[c]==liste2[0]):
                        if liste[c+1] not in sozluk:
                                sozluk[liste[c+1]]=1
                        else:
                                sozluk[liste[c+1]]=sozluk[liste[c+1]]+1
                    list2=liste2
                if(uzunluk==2):
                    if (liste[c] == liste2[0] and liste[c+1]==liste2[1]):
                        if liste[c + 2] not in sozluk2:
                                sozluk2[liste[c + 2]] = 1
                        else:
                                sozluk2[liste[c + 2]] = sozluk2[liste[c + 2]] + 1
                    list3=liste2
                if(uzunluk==3):
                    if (liste[c] == liste2[0] and liste[c+1]==liste2[1] and liste[c+2]==liste2[2]):
                        if liste[c + 3] not in sozluk3:
                                sozluk3[liste[c + 3]] = 1
                        else:
                                sozluk3[liste[c + 3]] = sozluk3[liste[c + 3]] + 1
                    list4=liste2
                if(uzunluk==4):
                    if (liste[c] == liste2[0] and liste[c+1]==liste2[1] and liste[c+2]==liste2[2] and liste[c+3]==liste2[3]):
                        if liste[c + 4] not in sozluk4:
                                sozluk4[liste[c + 4]] = 1
                        else:
                                sozluk4[liste[c + 4]] = sozluk4[liste[c + 4]] + 1
                    list5=liste2
                if(uzunluk==5):
                    if (liste[c] == liste2[0] and liste[c+1]==liste2[1] and liste[c+2]==liste2[2] and liste[c+3]==liste2[3] and liste[c+4]==liste2[4]):
                        if liste[c + 5] not in sozluk5:
                                sozluk5[liste[c + 5]] = 1
                        else:
                                sozluk5[liste[c + 5]] = sozluk5[liste[c + 5]] + 1
                    list6=liste2

#print(sozluk,sozluk2,sozluk3,sozluk4,sozluk5)
print(oneri(sozluk,liste))
print(oneri(sozluk2,liste))
print(oneri(sozluk3,liste))
print(oneri(sozluk4,liste))
print(oneri(sozluk5,liste))

f=open("170401047_hw_1_output","w")
dizi_yazdirma(list2)
f.write(oneri(sozluk,liste))
f.write("\n")
dizi_yazdirma(list3)
f.write(oneri(sozluk2,liste))
f.write("\n")
dizi_yazdirma(list4)
f.write(oneri(sozluk3,liste))
f.write("\n")
dizi_yazdirma(list5)
f.write(oneri(sozluk4,liste))
f.write("\n")
dizi_yazdirma(list6)
f.write(oneri(sozluk5,liste))




