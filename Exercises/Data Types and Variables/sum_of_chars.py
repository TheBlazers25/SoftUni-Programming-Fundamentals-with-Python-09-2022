number_of_lines = int(input())
counter = 0
for lines in range(number_of_lines):
    letter = str(input())
    counter  += ord(letter)
print(f"The sum equals: {counter}")

# name = input("Enter your name: ")
# for c in name:
#   print("The ASCII value for ", c, "is", ord(c))
# print("The total sum is: ",sum([ord(c) for c in name]))

