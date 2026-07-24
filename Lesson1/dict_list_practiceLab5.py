def in_order(nums):
    
    # Type your code here.
    for i in range(len(nums) - 1):# loop through the list of numbers, stopping at the second to last index
        if nums[i] < nums[i + 1]: #check if the current number is less than the next number
            return False #if the current number is less than the next number, return False
    return True #if the loop completes without returning False, return True

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1): # check if the list is in descending order
        print('In descending order') # if the list is in descending order, print 'In descending order'
    else:
        print('Not in order') # if the list is not in descending order, print 'Not in order'
        
    # Test in-order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2): #check if the list is in descending order
        print('In descending order')# if the list is in descending order, print 'In descending order'
    else:
        print('Not in order') #if the list is not in descending order, print 'Not in order'