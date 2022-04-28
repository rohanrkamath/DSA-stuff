l = [1,4,5,7,9,11,14,19]

def binarySearch(arr, n):
    l, r = 0, len(arr)-1
    
    while l <= r:
        m = l + ((r - l) // 2)

        if arr[m] == n:
            return m
        elif arr[m] < n:
            l = m+1
        else:
            r = m-1
        
    return 'Element not in the list.' 

print(binarySearch(l, 20))