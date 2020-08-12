Problem:
Suppose we had a list of n integers sorted in ascending order. How quickly could we check if a given integer is in the list?

Solution:
Because the list is sorted, we can use binary search to find the item in O(lgn) time and O(1) additional space.

## Time Complexity: T(n) = T(n/2) + c = O(logn)
## Space Complexity: O(1) in case of iterative implementation. In case of recursive O(logn) recursive call stack space.

# code

# recursive implementation
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1,x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1
        
        
if __name__ == '__main__':
    arr = [ 2,5,7,8,10]
    x = 10
    
    result = binarySearch(arr, 0, len(arr) - 1, x)
    
    if result != -1:
        print("Element is present at index {0}".format(result))
    else:
        print("Element is not present in array")
        
        
# iterative implementation

def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1
    
if __name__ == '__main__':
    arr = [2,5,7,8,10]
    x = 10
    
    result = binarySearch(arr, 0, len(arr) - 1, x)
    
    if result != -1:
        print("Element is present at index {0}".format(result))
    else:
        print("Element is not present in array")

