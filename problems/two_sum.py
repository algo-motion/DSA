def twoSum(arr, sum):
    mp = {}
    for index, value in enumerate(arr):
        if(value not in mp):
            mp[value] = index
    
    for i in range(len(arr)):
        need_find = sum - arr[i]
        if need_find in mp and mp[need_find] != i: 
            return [i, mp[need_find]]
    
    return None

print (twoSum ([3,4,5,8], 6))