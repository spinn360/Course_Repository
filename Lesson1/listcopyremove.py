expt_samples = []

tokens = input().split()
for token in tokens:
    expt_samples.append(int(token))
  
print('Original samples:', end=' ')
for samples in expt_samples:
    print(samples, end=' ')
print()

''' Your code goes here '''
for val in expt_samples[:]: # create copy of list[:] so it doesn't change as you modify original
    if val >= 55:
        print(val,'erased')
        expt_samples.remove(val)  #remove value from original list

print('Filtered samples:', end=' ')
for samples in expt_samples:
    print(samples, end=' ')
print()