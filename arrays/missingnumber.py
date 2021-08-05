def finder(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print (result)
        
    return result

arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder(arr1,arr2))
