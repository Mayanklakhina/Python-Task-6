# a simple program on list comprehension without conditions

letters = [ letter for letter in 'mayank' ]
print( letters)


# List comprehension with conditions
num = [i for i in range(100) if i % 3 == 0 if i % 5 == 0]
print(num)