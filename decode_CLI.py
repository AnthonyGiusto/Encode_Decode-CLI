def decode(index):
    """Takes a user input value and decodes it with
    a predefined index"""

    # creates known lists of indexes for decoding
    nullcode = {'i': 1, 'c': 2, 'e': 3, 'd': 4, 'r': 5, 'a': 6,
                'g': 7, 'o': 8, 'n': 9, 's': 0}
    code_one = {'n': 1, 'e': 2, 'a': 3, 'r': 4, 'd': 5,
                'g': 6, 's': 7, 'i': 8, 'o': 9, 'c': 0}
    code_two = {'c': 1, 's': 2, 'g': 3, 'r': 4, 'd': 5, 'i': 6,
                'o': 7, 'a': 8, 'e': 9, 'n': 0}
    code_three = {'a': 1, 'e': 2, 'r': 3, 'n': 4, 's': 5, 'i': 6,
                  'o': 7, 'g': 8, 'c': 9, 'd': 0}
    code_four = {'d': 1, 'r': 2, 'a': 3, 's': 4, 'g': 5,
                 'o': 6, 'c': 7, 'i': 8, 'e': 9, 'n': 0}

    # Assigns each indexed code to the codelist list object.
    codelist = [nullcode, code_one, code_two, code_three, code_four]

    # Prompts for the code-string that is to be decoded into a number.
    code = input("enter the code: ")
    letterlist = []

    # Assigns the user-defined index to the corrilated code list.
    codeindex = codelist[index]
    for letter in code:
        letterlist.append(letter)
    for letter in letterlist:
        print(codeindex[letter], end="")
