array = []
a = []
import random
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
  for j in range(1,n+1): # наповнюємо спочатку перший массив з чіткою послідовністю
     a.append(j)
  for i in range(n): # а теперь у випадковій послідовності кидаємо все ті самі елементи в інший массив
     num = random.choice(a)
     a.remove(num) # видалємо елементи з першого массиву для того щоб двічі не повторювалися
     array.append(num)
n=int(input("Число елементів массиву: ")) 
arr_mad(n)
print("Не відсортований массив: ", array)
print('А теперь відсортований: ', sel_sort(array))
