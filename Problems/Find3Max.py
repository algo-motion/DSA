def find3Max(arr):
    max1 = max2 = max3 = arr[0]
    for i in range(len(arr)):
        if arr[i] > max1: 
            max1, max2, max3 = arr[i], max1, max2
        elif arr[i] > max2: 
            max2, max3 = arr[i], max2        
        elif arr[i] > max3: 
            max3 =  arr[i]
    return max1, max2, max3

arr = [1, 9, 8, 5]
print (find3Max(arr))