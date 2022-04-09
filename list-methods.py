numbers=[30, 10, 5, 16, 4, 9, 10]
letters=["a", "b", "y", "h", "o"]

val=min(numbers)
val=max(numbers)       #==> en büyük rakamı seçer.
val=max(letters)       #==> en büyük harfi seçer.(alfabe sırasına göre düşünürsek.)
val=min(letters)
print(val)

result=numbers[:3]    
result=numbers[3:6]
result=numbers[4:]    
print(result)

numbers[0]=40            #==> ilk sayıyı 40 sayısı ile değitirir.
print(numbers)

numbers.append(70)       #==> listenin son kısmına 70 sayısını ekler.
print(numbers)

numbers.insert(1,111)    #==> örenkte 1. indekteki sayının SOLUNA 111 sayısını ekledi.
print(numbers)

numbers.pop(0)           #==> 0. indexdeki sayıyı siler.  
numbers.pop(-1) 
print(numbers) 

numbers.remove(111)       #==> 111 sayısını siler.   
print(numbers)

numbers.sort()            #==> sayıları veya harfleri küçükten büyüğe doğru sıralar.
print(numbers)

numbers.reverse()         #==> sayıları veya harfleri  büyükten küçüğe  doğru sıralar.
print(numbers)          

print(len(numbers))       #==> kaç eleman olduğunu söyler.

print(numbers.count(10))  #==> kaç tane 10 elemanı olduğunu söyler.

numbers.clear()           #==> listedeki tüm elemanları siler.
print(numbers)