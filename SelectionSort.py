
arr = [-60, 0, 50, 30, 10, 20]

for i in range(len(arr)-1):
    minI = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[minI]:
            minI = j
    arr[i], arr[minI] = arr[minI], arr[i]
print(arr)



