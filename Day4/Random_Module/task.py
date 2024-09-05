import random
#import my_module

#To generate random numbers
random_integer = random.randint(1,10)
print(random_integer)

#to use your own module in the code
#print(my_module.my_favourite_number)

#To generate a random float number
random_number_0_t0_1 = random.random()
print(random_number_0_t0_1)

#to get floating number from 0 to 10 but not 10
print(random_number_0_t0_1 * 10)

#to generate random floating point number including 1 and 10 1 >= N <= 10
random_float = random.uniform(1,10)
print(random_float)