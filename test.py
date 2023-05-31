import random
import time
class Sort:
    def mk_arr(n):# Створення массиву
        array = list(range(1, n + 1))
        random.shuffle(array)
        return array
    
    def fun_sel(fun, array, n): # функція для виклику інших функцій
        start = time.time()
        if fun == 1:
         array = Sort.quicksort(array, n)
        elif fun == 2:
         array = Sort.sel_sort(array, n)
        elif fun == 3:
         array = Sort.insertion_sort(array, n)
        elif fun == 4:
         array = Sort.bogoSort(array, n)
        elif fun == 5:
         array = Sort.bubble_sort(array, n)
        count = round(time.time() - start, 4)
        return array, count

    def insertion_sort(array, n): # сортування вставками
        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def sel_sort(array, n): # Вибіркове сортування
        for i in range(n):
            minimal = i
            for j in range(i + 1, n):
                if array[j] < array[minimal]:
                    minimal = j
            array[minimal], array[i] = array[i], array[minimal]
        return array

    def quicksort(array, n): # Швидке сортування
     if n <= 1:
         return array
     pivot = array[n // 2]
     left = [x for x in array if x < pivot]
     middle = [x for x in array if x == pivot]
     right = [x for x in array if x > pivot]
     return Sort.quicksort(left, len(left)) + middle + Sort.quicksort(right, len(right))

    def cycle(n, arr, check):  # бульбашкове сортування
      check = True
      for i in range(0, n-1):
         if arr[i] > arr[i+1]:
           arr[i],arr[i+1] = arr[i+1],arr[i]
           check = False
      return arr, check
    def bubble_sort(arr, n):
     check = False
     while check == False:
       arr, check = Sort.cycle(n, arr, check)
     return arr
    
    def bogoSort(array, n): # Бого сорт
     while Sort.bog_check(array, n)==False:
        random.shuffle(array)
     return array
    def bog_check(array, n):
     for i in range(0, n-1):
         if (array[i] > array[i+1] ):
             return False
     return True
n = int(input("Число елементів масиву: "))
array = Sort.mk_arr(n)
fun = int(input("1--quicksort, 2--selection sort, 3--insertion sort, \n4--Bogo sort, 5--bubble sort\nОберість функцію: "))
print('Не відсортований масив: ', array)
array, count =Sort.fun_sel(fun, array, n)
print('А теперь відсортований: ', array, '\nЧас:', count)
