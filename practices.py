### linear search 


def linear_search(list,target):
    
    """
    Returns the index position of the target if found, else none
    """
    
    
    for idx in range(0,len(list)):
        
        if list[idx] == target:
            return idx
        
    return None 

def verify(target):
    
    if target:
        print("The target find in the index: ", target)
        
    else:
        print("The target is not found")
        


def binary_search(list, target):
    
    
    first_idx = 0
    
    last_idx = len(list) - 1
    
    while first_idx <= last_idx:
        
        midpoint = (first_idx + last_idx)//2
        
        if list[midpoint] == target:
            
            return midpoint
        elif list[midpoint] < target:
            first_idx = midpoint + 1
        else:
            last_idx = midpoint - 1      
    return None


def recursive_binary_search(list,target):
    
    if len(list)== 0:
        return False 
    
    else:
        
        midpoint = len(list) // 2
        
        if list[midpoint] == target:
            return True 
        
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:],target)
        else:
            return recursive_binary_search(list[:midpoint],target)
        
            


if __name__ == '__main__':
    
   # numbers = [num for num in range(1,11)]
    
   # result = recursive_binary_search(numbers,5)
    
    verify(result)
    
    
