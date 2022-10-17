
# 1. What is the result of the code, and why?

def func(a,b=6,c=8) :
    print(a,b,c)
func(1,2)

# ANS: The result of the above code is 1 2 8 because the function uses the default value of c i.e. 8, which is
# provided at the time of declaration.

# 2. What is the result of this code, and why?

def func(a,b,c=5) :
    print(a,b,c)
func(1,c=3,b=2)

# ANS: The result of the above code is 1 2 3 because the function will use default values only when a value for a
# argument is not provided and if argument name is mentioned while doing a function call, the order of arguments is
# also ignored by the python interpreter.

# 3. How about this code: what is its result, and why?

def func(a, *pargs) :
    print(a,pargs)
func(1,2,3)

# ANS: The result of the code is 1 (2,3). *pargs stands for variable length arguments. This format is used when we are
# not sure about the no. of arguments to be passed to a function. All the values under this argument will be stored in
# a tuple.

# 4. What does this code print, and why?

def func(a, **kargs) :
    print(a,kargs)
func(a=1,c=3,b=2)

# ANS: The result of the above code is 1 {'c':3,'b':2}. **kargs stands for variable length keyword arguments. This
# format is used when we want pass key value pairs as input to a function. All the key value pairs will be stored in a
# dictionary.

# 5. What gets printed by this, and explain?

def func(a,b,c=8,d=5) :
    print(a,b,c,d)
func(1,*(5,6))

# ANS: The Output of the above is 1 5 6 5. This reason for this function not throwing as error is because, this
# function expects 4 arguments. The value for a is provided explicitly whereas for arguments b and c, the function will
# expand the *(5,6) and consider the value of b as 5 and value of c as 6. Since the default value of d is provided in
# function declaration d value will be 5. However it is recommended to use the feature of positional arguments at the
# end.

# 6. What is the result of this, and explain?

def func(a, b, c) : a = 2; b[0] = 'x'; c['a'] = 'y'
l = 1; m = [1]; n = {'a':0}
func(l, m, n)
l,m,n

# ANS: The output of above code is 1,['x'],{'a':'y'}.





