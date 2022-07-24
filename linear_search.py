# LINEAR SEARCH ALGORITHMS

# Method 1
def linearSearch(n, x):
    """
    Time complexity: O(n)
    Auxiliary Space: O(1)

    Linear search is rarely used practically because other search algorithms such as 
    the binary search algorithm and hash tables allow significantly faster searching
    compared to Linear search.
    """

    for i in range(len(n)):
        if n[i] == x:
            return i
    else:
        return -1

result = linearSearch([1,2,3,4],6)

if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)