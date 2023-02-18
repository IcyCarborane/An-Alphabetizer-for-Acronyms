"""number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)"""

"""input_string = input("Enter all family members name separated by space  ")
# Split string into words
family_list = input_string.split(" ")
print("\n")
# Iterate a list
print("Printing all family member names")
for name in family_list:
    print(name)"""

words = input("Provide a list of words that are comma-separated: ")

words_split = [x for x in words.split(',')]

words_split.sort()

print("User input of words: ")

print(words)

print("User words sorted alphabetically: ")

print(','.join(words_split))