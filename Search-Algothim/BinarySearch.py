#Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

# Binary Search Approach: Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n). The basic steps to perform Binary Search are:

# Begin with an interval covering the whole array. 
# If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. 
# Otherwise, narrow it to the upper half. 
# Repeatedly check until the value is found or the interval is empty.

def BinarySearch(arr,l,r,x):
    if r >= l:
        mid = l + (r-l)//2
    if arr[mid]== x:
        return mid

    if arr[mid] > x:
        BinarySearch(arr,l,mid-1,x)
    if arr[mid] < x:
        BinarySearch(arr,mid+1,r,x)
    else:
        return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 5
  
# Function call
result = BinarySearch(arr, 0, len(arr)-1, x)
  
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")