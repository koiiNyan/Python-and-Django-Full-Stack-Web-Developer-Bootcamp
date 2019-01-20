#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])
# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[4:])
# Bonus: Use indexing to reverse the string
print(s[::-1])

###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
print(l)
l[-1][-1] = 'goodbye'
print(f"l after reassigning: {l}")

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}

d2 = {'k1':{'k2':'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(f"Dic1: {d1}")
d1_hello = d1['simple_key']
print(f"Grabbing 'hello' from the 1rst dic: {d1_hello}")

print(f"Dic1: {d2}")
d2_hello = d2['k1']['k2']
print(f"Grabbing 'hello' from the 2nd dic: {d2_hello}")

print(f"Dic1: {d3}")
d3_hello = d3['k1'][0]['nest_key'][1][0]
print(f"Grabbing 'hello' from the 3rd dic: {d3_hello}")


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
uniq = set(mylist)
print(uniq)

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print(f"Hello my dog's name is {name} and he is {age} years old")
