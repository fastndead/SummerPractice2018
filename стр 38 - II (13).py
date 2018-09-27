def findNumberOfNumbers(str1):
    if any(char.isdigit() for char in str1) == False:
        return 0
    for c in str1:
        if c.isdigit():
            break
    return 1 + findNumberOfNumbers(str1.replace(c, ''))


str1 = input("Enter string 1 = ")
str2 = input("Enter string 2 = ")

if (findNumberOfNumbers(str1) > findNumberOfNumbers(str2)):
    print("First string contains more numbers")
elif (findNumberOfNumbers(str1) < findNumberOfNumbers(str2)):
    print("Second string contains more numbers")
else:
    print("Number of digits in both strings is equal")

