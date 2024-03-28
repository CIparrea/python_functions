# ____________________________________________________________________
# calling a function with some parameters

# def add(a,b):
#     return a+b

# def sub(a, b):
#   return a - b

# def compute(a, b, op):
#   return op(a, b)

# print( compute(1, 5, sub) )




# ____________________________________________________________________
# printing all parameters passed to the function


# def my_function(*args):
#   print( type(args) )
#   for arg in args:
#     print(arg)

# my_function(1, 2, 'SEI')




# ____________________________________________________________________
# breaking the parameters, the first argument is a name and then the rest will be considered as args

# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': []}
#   for skill in args:
#     dev['skills'].append(skill)
#   return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))




# ____________________________________________________________________
# same as the previous one, just that instead of mapping them we're just creating a list

# def dev_skills(dev_name, *args):
#   dev = {'name': dev_name, 'skills': list(args)}
#   return dev

# print(dev_skills('Alex', 'HTML', 'CSS', 'JavaScript', 'Python'))



# ____________________________________________________________________
# KWARGS KewWordARGumentS breaks the arguments into a DICTIONARY(JS object) so now we have key value pairs instead of calling them with the index
# KWARGS ONLY TAKES KEY VALUE PAIRS 

# def dev_skills(dev_name, **kwargs):
#   # kwargs will be a dictionary!
#   dev = {'name': dev_name, 'skills': kwargs}
#   return dev

# print(dev_skills('Jackie', HTML=5, CSS=3, JavaScript=4, Python=2))



# ____________________________________________________________________
# KWARGS deconstruction to get keyword and value (line 79)
# item is every key-value-pair inside a dictionary on this case it is called unpacking

# def arg_demo(pos1, pos2, *args, **kwargs):
#   print(f'Positional params: {pos1}, {pos2}')
#   print('*args:')
#   for arg in args:
#     print(' ', arg)
#   print('**kwargs:')

# # must be called like this, if not it will not recognize that you're calling both of the key-value-pairs
#   for keyword, value in kwargs.items():
#     print(f'  {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')



# ____________________________________________________________________
