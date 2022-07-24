# Ternary search algorithms

"""Ternary search is a decrease(by constant) and conquer algorithm 
that can be used to find an element in an array. It is similar
to binary search where we divide the array into two parts but 
in this algorithm, we divide the given array into three parts
and determine which has the key (searched element).
We can divide the array into three parts by taking mid1 and mid2 
which can be calculated as shown below. Initially, l and r will be equal
to 0 and n-1 respectively, where n is the length of the array. 

It is same as the binary search. The only difference is that,
it reduces the time complexity a bit more. Its time complexity 
is O(log n base 3) and that of binary search is O(log n base 2)."""

def ternarySearch(arr, x):
    # iterative way
    left, right = 0, len(arr)-1
    while left < right:
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3
        if x == arr[mid1]:
            return mid1
        elif x == arr[mid2]:
            return mid2
        elif x < arr[mid1]:
            right = mid1 - 1 
        elif x > arr[mid2]:
            left = mid2 + 1
        else:
            right = mid1 + 1
            left = mid2 - 1
    return -1 

# result = ternarySearch([1,2,3,4,6,7,8,9], 0)
# if result == -1:
#     print('x is not found')
# else:
#     print('The number found at index: ' + str(result))


def ternarySearchRec(arr, x, left, right):
    # recursive way
    if right >= left:
        
        mid1 = left + (right - left)//3
        mid2 = right - (right - left)//3

        if arr[mid1]==x:
            return mid1

        elif arr[mid2]==x:
            return mid2

        elif x < arr[mid1]:
            return ternarySearchRec(arr, x, left, mid1-1)

        elif x > arr[mid2]:
            return ternarySearchRec(arr, x, mid2+1, right)

        else:
            return ternarySearchRec(arr, x, mid1+1, mid2-1)

        
    return -1

arr = [1,2,3,4,6,7,8,9]
x = 8
left = 0
right = len(arr)-1
result = ternarySearchRec(arr, x, left, right)
if result == -1:
    print('x is not found')
else:
    print('The number found at index: ' + str(result))