def calc_average(nums):
    total = 0
    for pos, val in enumerate(nums):
        total += val
    avg = total / len(nums)
    return avg  
    # Type your code here.
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0