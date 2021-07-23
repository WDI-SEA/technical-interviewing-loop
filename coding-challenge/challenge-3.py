
# first we have the array
arr = [453, "hello", 293, True]
# then we have to have a counter to display (should return 15)
count = 0 
# need to convert array into string
stringlist = ''.join(map(str,arr))
# print(stringlist)

# for index of the range between 0 and the number of characters, 
# if the character isnt blank, add 1 to counter
# print('number of characters: ', str(count))
for i in stringlist:
  count = count + 1
print("number of characters: ", count)


