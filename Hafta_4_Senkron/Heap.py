def min_heapify(array,i):
    left=2*i + 1
    right=2*i + 2
    length=len(array)-1
    smallest=i
    if left<=length and array[i]>array[left]:
        smallest=left
    if right<=length and array[smallest]>array[right]:
        smallest=right
    if smallest !=i:
        array[i],array[smallest]=array[smallest],array[i]
        min_heapify(array,smallest)
#min_heapify()--> **Parametre olarak üzerinde işlem yapılacak diziyi ve indis numarasını alır.Geriye bir şey döndürmez.
#                 **Verilen indis numarasındaki değeri sağ ve sol çocukla karşılaştırarak büyük(min heap ise) ise gerekli değişimi gerçekleştirir.
def build_min_heap(array):
    for i in reversed(range(len(array)//2)):
        min_heapify(array,i)
#build_min_heap()-->**Parametre olarak diziyi alır.Geriye bir şey döndürmez.
#                   **Dizinin yarısından başlayarak tersten min_heapify() fonskiyonunu çağırarak tüm diziyi min heap yapısına çevirir.
def heap_sort(array):
    array=array.copy()
    build_min_heap(array)
    sorted_array=[]
    for i in range(len(array)):
        array[0],array[-1]=array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array
#heap_sort()-->**Parametre olarak dizi alır.Geriye bir şey döndürmez.
#              **Kökteki  dizinin en küçük elemanı ile dizinin son elemanı yer değistirir.En sona alınan eleman diziden çıkarılır ve sorted_array
#                dizisine eklenir.min_heapify() çağrılarak heap yapısı min heap e dönüstürülür.Bu işlemi dizinin tüm elemanları için yapınca sıralanmış
#                sorted_array elde edilir.
def insert_item_to_heap(my_heap_1,item):
    my_heap_1.append(item)
#   build_min_heap(my_heap_1)
    length=len(my_heap_1)-1
    baba=int((length-1)/2)
    while(length>=0 and my_heap_1[baba]>my_heap_1[length]):
         temp=my_heap_1[baba]
         my_heap_1[baba]=my_heap_1[length]
         my_heap_1[length]=temp
         length=baba
         baba=int((length-1)/2)
#insert_item_to_heap()-->**Parametre olarak diziyi ve indisi alır.Geriye bir şey döndürmez.
  #                       **Eğer çocuk düğüm ebeveynden küçük ise elemanlar yer değiştirir.while döngüsü içinde root a kadar bu kontrol edilir.
def remove_item_from(my_heap):
    my_heap[0]=my_heap[len(my_heap)-1]
    my_heap.pop()
    build_min_heap(my_heap)
#remove_item_from()-->**Parametre olarak diziyi alır.Geriye bir şey döndürmez.
#                      **Kökü silmek için dizinin son elemanını köke yazarız ve dizinin son elemanını pop() ile diziden sileriz.build_min_heap() çağrılarak
#                       min heap tekrar oluşturulur.
my_array=[]
insert_item_to_heap(my_array,7)
insert_item_to_heap(my_array,6)
insert_item_to_heap(my_array,45)
insert_item_to_heap(my_array,32)
insert_item_to_heap(my_array,5)
insert_item_to_heap(my_array,2)
insert_item_to_heap(my_array,20)
my_array_2=heap_sort(my_array)
print(my_array)
print(my_array_2)
remove_item_from(my_array)
print(my_array)
