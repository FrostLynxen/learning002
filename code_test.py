# implement a function that splits a string by whitespace
def split_string_by_spaces(input_string):
    return input_string.split()


# implement a function that counts the number of words in a string
def count_words(input_string):
    words = input_string.split()
    return len(words)


def main():
    try:
        input_string = input("Enter a string: ")
    except EOFError:
        input_string = ""

    result = split_string_by_spaces(input_string)
    word_count = count_words(input_string)

    print("The split string is:", result)
    print("The number of words in the string is:", word_count)


if __name__ == "__main__":
    main()