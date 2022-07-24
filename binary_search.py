# Iterative way of implementing binary search
def binarySearch(arr, x):
    """"
    Iterative way is to set left and right pointers and move 
    towards the middle number, which is the base case
    runtime: O(logN)
    """
    left, right = 0, len(arr)-1
    mid = (left + right) // 2
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1


result = binarySearch([1,2,3,4,6,7,8,9], 7)
if result == -1:
    print('x is not found')
else:
    print('The number found at index: ' + str(result))
