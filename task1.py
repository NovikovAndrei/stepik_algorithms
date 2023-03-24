a = len(arr) - 1 #O(1)
out = list() # O(1)
while a > 0:
    out.append(arr[a]) #O(log1.7(n))
    a = a // 1.7 #O(1)
out.merge_sort() #O(n log(n)
# O(n log(n) log_1.7(n))
