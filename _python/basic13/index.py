# 1.) Print 1-255
# for x in range(1, 256):
#     print(x)

# 2.) Print Ints and Sum 0-255
# sum = 0
# for x in range(0, 256):
#     sum += x
#     print('x is ' + str(x))
#     print('sum is ', sum)

# 3.) Print Max of Array
myList = [5,8,1,3,10,2,7]
# print(max(myList))

# 4.) Return Odds Array 1-255
# oddsList = []
# for x in range(1, 256, 2):
#     oddsList.append(x)

# print(oddsList)

# 5.) Return Array Count Greater than Y
# count = 0
# y = 6
# for x in myList:
#     if x > y:
#         count += 1
#         print('mylist value: ', x, ' is greater than: ', y)

# print(count)

# 6.) Print Max, Min, Average Array Values
# print(max(myList))
# print(min(myList))
# print(sum(myList)/len(myList))

# 7.) Swap String for Array Negative Values

# 8.) Print Odds 1-255

# 9.) Print Array Values

# 10.) Print Average of Array

# 11.) Square Array Values

# 12.) Zero Out Array Negative Numbers

# 13.) Shift Array Values Left
print(myList[:1])
print(myList[1:])
print(myList)

myList2 = myList[1:] + myList[:1]
print(myList2)
print(myList.pop(3))
print(myList)