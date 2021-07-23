

# define 'Hello World'
# if letters are upper cased, return to lowercase.
# else if letters are lowercase, return to uppercase.
# return 'hELLO wORLD'

#create a string for "Hello World", and create an empty string for "hELLO wORLD"
string= 'Hello World'
newstring = ''

#showing lower case and upper case methods
print(string.lower())
print(string.upper())
#showing true/false situations for string
print(string.isupper())
print(string.islower())

#a is for looping each letter in the string
for a in string:
  #if current character is upper,
  if (a.isupper()) == True:
    #converts case and adds to new string
    newstring += (a.lower())
  # else if current character is lower,
  elif (a.islower()) == True:
    #converts case and adds to string
    newstring += (a.upper())
  #else if is a space,
  elif (a.isspace()) == True:
    #adds space to string
    newstring += a

print('old string: ', string) 
print('new string: ', newstring)


