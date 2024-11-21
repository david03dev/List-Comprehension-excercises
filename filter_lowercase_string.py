#Task 4: Filter and Convert Strings

#From the list ["Python", "java", "C++", "ruby", "JavaScript"], create a new list containing only strings that start with an uppercase letter, converted to lowercase.

#initialize the given list
given_list = ["Python", "java", "C++", "ruby", "JavaScript"]

#Generate a new list
filtered_lowercase_strings = [x.lower() for x in given_list if x[0] == x[0].upper()]

#print the result
print(new_list)
