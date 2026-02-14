#implement a fucntion that splits a string by spaces
def split_string_by_spaces(input_string):
    return input_string.split(' ')

input_string = input("Enter a string: ")
result = split_string_by_spaces(input_string)
print("The split string is:", result)

