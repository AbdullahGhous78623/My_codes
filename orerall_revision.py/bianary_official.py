def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        
        # Check if the target is at mid
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half
        else:
            high = mid - 1  # Discard the right half
            
    return -1  # Target not found


def binary_search(arr, x):
    """Performs binary search on a sorted array to find the index of the target element.

  Args:
    arr: A sorted list of elements.
    x: The target element to search for.

  Returns:
    The index of the target element in the array if found, otherwise -1.
  """

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
arr = [2,2,2,3,3,3,3,3,2,2,2,4,4,4,4,4,3,4,10,40]
x = 2

result = binary_search(arr, x)

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")