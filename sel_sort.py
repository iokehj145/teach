import random
array = {}
# функція вибірки(Виглядає ніби сходи якщо не дивитись на кінець)
def sel_sort(array):
    n = len(array)# щоб двічі не повторюватися
    for i in range(n):# Пройдемося по всім елементам
        minemal = i
        for j in range(i+1, n): # цей цикл шукає нам найменший елемент
           if array[j] < array[minemal]:
               minemal = j
        array[minemal], array[i] = array[i], array[minemal]
    return array
# генерація масиву.
def arr_mad(n):
  array = list(range(1, n + 1)) # генерація массиву але з чіткою послідовністю
  print(array)
  random.shuffle(array) # Мішає елементи між собою
  return array
n=int(input("Число елементів массиву: ")) 
array = arr_mad(n)
print("Не відсортований массив: ", array)
print('А теперь відсортований: ', sel_sort(array))
