# Complete the function below.

def target_sum(arr, stage_arr, target):
    curr_sum = sum(stage_arr) if len(stage_arr) > 0 else None
    if len(arr) == 0 and curr_sum != target:        
        print 'False'
        return False

    print '\nArr:', arr, 'Target:', target
    print 'Stage:', stage_arr, 'Sum:', curr_sum
    
    if curr_sum == target:
        return True
    
    # for i, num in enumerate(arr):
    i = 0
    num = arr[0]
    if target_sum(arr[:i] + arr[i+1:], stage_arr + [num], target):
        return True
    if target_sum(arr[:i] + arr[i+1:], stage_arr, target):
        return True
    
    print 'False'
    return False

def check_if_sum_possible(arr, k):    
    stage_arr = []
    return target_sum(arr, stage_arr, k)
    
