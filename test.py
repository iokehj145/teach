import random
import time

class Sort:
    def __init__(self, n): # ініціалізація масиву
        self.n = n
        self.array = list(range(1, self.n + 1))
        random.shuffle(self.array)

    def fun_sel(self, fun): # функція для виклику інших функцій
        start = time.time()
        if fun == 1:
         self.quicksort()
        elif fun == 2:
         self.sel_sort()
        elif fun == 3:
         self.insertion_sort()
        elif fun == 4:
         self.bogoSort()
        elif fun == 5:
         self.bubble_sort()
        elif fun == 6:
            self.array = self.merge_sort(self.array)
        count = round(time.time() - start, 4)
        return self.array, count
    def insertion_sort(self):  # сортування вставками
        for i in range(1, self.n):
          key = self.array[i]
          j = i - 1
          while j >= 0 and self.array[j] > key:
            self.array[j + 1] = self.array[j]
            j -= 1
          self.array[j + 1] = key

    def sel_sort(self):  # Вибіркове сортування
        for i in range(self.n):
            minimal = i
            for j in range(i + 1, self.n):
                if self.array[j] < self.array[minimal]:
                    minimal = j
            self.array[minimal], self.array[i] = self.array[i], self.array[minimal]


    def quicksort(self):  # Швидке сортування
        self.quicksort1(0, self.n - 1)

    def quicksort1(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quicksort1(low, pivot_index - 1)
            self.quicksort1(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def cycle(self):  # бульбашкове сортування
        check = True
        for i in range(0, self.n - 1):
            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                check = False
        return check
    def bubble_sort(self):
        check = False
        while check is False:
            check = self.cycle()
    
    def bogoSort(self):  # Бого сорт
        while self.bog_check() is False:
            random.shuffle(self.array)
    def bog_check(self):
        for i in range(0, self.n - 1):
            if self.array[i] > self.array[i + 1]:
                return False
        return True

    def merge_sort(self, arra): # сортування злиттям
        if len(arra) <= 1:
            return arra
        mid = len(arra) // 2
        left_arr = self.merge_sort(arra[:mid])
        right_arr = self.merge_sort(arra[mid:])
        return self.merge(left=left_arr, right=right_arr)
    def merge(self, left, right):
        merged = []
        ind_le, ind_ri = 0, 0
        while ind_le < len(left) and ind_ri < len(right):
            if left[ind_le] < right[ind_ri]:
                merged.append(left[ind_le])
                ind_le += 1
            else:
                merged.append(right[ind_ri])
                ind_ri += 1
        merged.extend(left[ind_le:])
        merged.extend(right[ind_ri:])
        return merged

while True:
  n = int(input("Число елементів масиву: "))
  array = Sort(n)
  fun = int(input("1--quicksort, 2--selection sort, 3--insertion sort, \n4--Bogo sort, 5--bubble sort, 6--merge sort\nОберість функцію: "))
  print('Не відсортований масив: ', array.array)
  array, count =array.fun_sel(fun)
  print('А теперь відсортований: ', array, '\nЧас:', count)
