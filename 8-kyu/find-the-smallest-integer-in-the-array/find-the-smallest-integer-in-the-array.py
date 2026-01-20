def find_smallest_int(arr):
    # Code here
    smallest = arr[0]
    
    for i in arr:
        if i < smallest:
            smallest = i
    
    return smallest
            
            
           
          