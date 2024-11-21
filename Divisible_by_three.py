#Task 2: Extract Numbers Divisible by 3

#From the list [3, 6, 9, 12, 15, 18, 20, 21, 25], create a new list of numbers divisible by 3.

#Initialize given list
given_list = [3, 6, 9, 12, 15, 18, 20, 21, 25]
#generate a new list of numbers divisible by 3.
list_of_3_divisions = [x for x in given_list if x % 3 == 0]
#print the results
print(list_of_3_divisions)
