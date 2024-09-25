#!/usr/bin/env python
# coding: utf-8

# Assignment_1
#1. In the below elements which of them are values or an expression? eg:- values can beinteger or string and expressions will be mathematical operators.

* = Expression (multiplication operator)
'hello' = Value (string)
-87.8 = Value (floating-point number)
- = Expression (subtraction operator)
/ = Expression (division operator)
+ = Expression (addition operator)
6 = Value (integer)#2. What is the difference between string and variable?

A variable stores any kind of data, while a string is a type of data that is written between '' or " ".

df = 'Hello'
Here df is a variable and 'Hello' is a string. #3. Describe three different data types.

1. Integer: Represents whole numbers (e.g., 10, -5, 0).
2. Floating-point: Represents decimal numbers (e.g., 3.14, -87.8).
3. String: Represents sequences of characters (e.g., 'hello', 'Python123').#4. What is an expression made up of? What do all expressions do?
An expression is made up of values, variables, and operators 
example:
x = 10
y = 2
x * y
20
All expressions are evaluated to produce a result (example: 2 + 3 evaluates to 5).
# In[5]:


x = 10
y = 2
x * y


# #5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# An expression produces a value when evaluated 
# x = 10
# y = 2
# x * y
# 20
# 
# A statement is a unit of code that performs an action (example: an assignment like spam = 10 is a statement because it assigns a value to a variable but does not itself produce a result).

# #6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 
# answer: The variable bacon is initially assigned the value 22.
# The expression bacon + 1 evaluates to 23, but it does not change the value of bacon because there is no assignment statement to update bacon with the result of bacon + 1.
# So, after this code runs, the value of bacon remains 22.

# #7. What should the values of the following two terms be?
# 
# 'spam' + 'spamspam' → 'spamspamspam' (concatenation of two strings)
# 'spam' * 3 → 'spamspamspam' (repetition of the string three times)

# In[8]:


'spam' + 'spamspam'


# In[10]:


'spam' * 3


# #8. Why is eggs a valid variable name while 100 is invalid?
# 
# eggs is valid because it follows variable naming rules (it starts with a letter and can contain letters and numbers).
# 100 is invalid because variable names cannot start with a number.
#9. What three functions can be used to get the integer, floating-point number, or string version of a value?

int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
# In[ ]:


#10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'


# In[11]:


'I have eaten ' + 99 + ' burritos.'


# In[13]:


#solution
'I have eaten ' + '99' + ' burritos.'


# In[ ]:




