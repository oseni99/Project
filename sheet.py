import random 
random.seed(101)
def acct():
    mylst = [0,1,2,3,4,5,6,7,8,9]
    x = random.choices(population=mylst,k=9)
    print("-".join(map(str,x)))
acct()
    


import random

my_list = [1, 2, 3, 4, 5]
sample_size = 3

# Use random.choices to sample items with replacement
sampled_items = random.choices(my_list, k=sample_size)

# Convert the sampled items to a string with a custom separator
sampled_items_str = '---'.join(map(str, sampled_items))

# Print the resulting string
print(sampled_items_str)
