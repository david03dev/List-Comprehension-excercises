#Task 1: Generate Squares

#Write a list comprehension to create a list of squares for numbers from 1 to 10.

#initialize the list
given_list = [1,2,3,4,5,6,7,8,9,10]

#generate a list with squares of given list
list_of_squares = [x**2 for x in given_list]

#print the results
print(list_of_squares)
