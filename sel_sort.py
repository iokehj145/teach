import random
def sel_sort(array):
    n = len(array)
    for i in range(n):
        mine = i
        for j in range(i+1, n):
           if array[j] < array[mine]:
               mine = j
        array[mine], array[i] = array[i], array[mine]
    return array
array=[]
a = []
for j in (1,10):
   a.append(j)
for i in range(10):
  num = int()
  b = 10-i
  num = (random.choice(a))
  a.remove(num)
  array.append(num)
print(array)