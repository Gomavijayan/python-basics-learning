def sortInWave(arr, n):
    arr.sort()
    for i in range(0,n-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0,len(arr)):
print arr[i]
