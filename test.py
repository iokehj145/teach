import random
import time
class Sort:
    def mk_arr(n):
        array = list(range(1, n + 1))
        random.shuffle(array)
        return array
    def fun_sel(fun, array):
        start = time.time()
        if fun == 1:
         array = Sort.quicksort(array)
        elif fun == 2:
         array = Sort.sel_sort(array)
        elif fun == 3:
         array = Sort.bubble_sort(array)
        count = time.time() - start
        return array, count
        elif fun == 4:
         array = Sort.bogoSort(array)
        count = round(time.time() - start, 4)
    def sel_sort(array):
        n = len(array)
        for i in range(n):
            minimal = i
            for j in range(i + 1, n):
                if array[j] < array[minimal]:
                    minimal = j
            array[minimal], array[i] = array[i], array[minimal]
        return array

    def quicksort(array):
     if len(array) <= 1:
         return array
     pivot = array[len(array) // 2]
     left = [x for x in array if x < pivot]
     middle = [x for x in array if x == pivot]
     right = [x for x in array if x > pivot]
     return Sort.quicksort(left) + middle + Sort.quicksort(right)

    def cycle(n, arr, check):
     check = True
     for i in range(0, n-1):
         if arr[i] > arr[i+1]:
           arr[i],arr[i+1] = arr[i+1],arr[i]
           check = False
         else:
         	pass
     return arr, check
    def bubble_sort(arr):
     n = len(arr)
     check = False
     while check == False:
       arr, check = Sort.cycle(n, arr, check)
     return arr
    def bogoSort(array):
     while Sort.bog_check(array)==False:
        random.shuffle(array)
     return array
    def bog_check(array):
     n = len(array)
     for i in range(0, n-1):
         if (array[i] > array[i+1] ):
             return False
     return True
n = int(input("Число елементів масиву: "))
array = Sort.mk_arr(n)
fun = int(input("1--quicksort, 2--selection sort, 3--bubble sort, 4--Bogo sort\nОберість функцію: "))
print('Не відсортований масив: ', array)
array, count =Sort.fun_sel(fun, array)
print('А теперь відсортований: ', array, '\nЧас:', count)
