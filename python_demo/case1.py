def bubbleSort(arr):
    print(arr)
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    print(arr)
arr = [12,43,54,3,34,23]
bubbleSort(arr)