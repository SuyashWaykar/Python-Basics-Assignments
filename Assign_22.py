
# 1. What is the result of the code, and explain?

X = 'iNeuron'
def func():
   print(X)

func()

#ANS: The result of this code is iNeuron, because the function initialy looks for the variable X in its local scope,
# but since there is no local variable X, it returns the value of global variable x i.e. iNeuron

# 2. What is the result of the code, and explain?

X = 'iNeuron'
def func() :
   X = 'NI!'
   print(X)

func()

#ANS: The result of this code is NI!, because the function initially looks for the variable X in its local scope if X
# not available then it checks for variable X in the global scope, since here the X is present in the local scope, it
# prints the value NI!

# 3. What does this code print, and why?

X = 'iNeuron'
def func() :
   X = 'NI'
   print(X)
func()
print(X)

#ANS: The output of the code is NI and iNeuron. X = NI is in the local scope of the function func() and hence the
# function prints the X value as NI. X = 'iNeuron' is in the global scope. Hence print(X) prints output as iNeuron.

# 4. What output does this code produce? Why?

X = 'iNeuron'
def func() :
   global X
   X = 'NI'
func()
print(X)

#ANS: The output of the code is NI. The global keyword allows a variable to be accessible in the current scope. Since
# we are using global keyword inside the function func it directly access the variable in X in global scope and changes
# its value to NI. Hence the output of the code is NI.

# 5. What about this code - what's the output, and why?

X = 'iNeuron'
def func() :
   X = 'NI'
   def nested() :
      print(X)
   nested()
func()
X

#ANS: The output of the code is NI. The reason for this output is if a function wants to access a variable, if its not
# available in its localscope, it looks for the variable in its global scope. Similarly here also function nested looks
# for variable X in its global scope. Hence the output of the code is NI.

# 6. How about this code: what is its output in Python 3, and explain?

def func() :
   X = 'NI'
   def nested() :
      nonlocal X
      X = 'Spam'
   nested()
   print(X)
func()

#ANS: The output of the code is Spam. nonlocal keyword in python is used to declare a variable as not local. Hence the
# statement X = "Spam" is modified in the global scope. Hence the output of print(X) statement is Spam.






