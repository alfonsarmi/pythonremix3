globalsParameter = {'__builtins__' : None}
localsParameter = {'print': print, 'dir': dir}
exec('print(dir())', globalsParameter, localsParameter)

#Example 1: How exec() works?
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

#Example 2: Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human' ]
print( h_letters)

#Example 3: Using Lambda functions inside List
letters = list(map(lambda x: x, 'human'))
print(letters)

#Example 4: Using if with List Comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

#Example 5: Nested IF with List Comprehension 
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

