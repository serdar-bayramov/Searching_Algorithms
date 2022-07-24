# Iterative way of implementing binary search

from selectors import EpollSelector


def binarySearch(arr, x):
    """"
    Iterative way is to set left and right pointers and move 
    towards the middle number, which is the base case
    runtime: O(logN)
    """
    left, right = 0, len(arr)-1
        
    while left <= right:
        mid = right + (right - left)//2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1


result = binarySearch([1,2,3,4,6,7,8,9], 3)
if result == -1:
    print('x is not found')
else:
    print('The number found at index: ' + str(result))


# Recursive binary search

def binarySearch(arr, left, right, x):

    if right >= left:
        mid = right + (right - left)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, left, mid-1, x)
        else:
            return binarySearch(arr, mid+1, right, x)
    
    else:
        return -1

