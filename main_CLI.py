from encode_cli import encode
from decode_cli import decode


def main():
    """
    Runs the Encoder-Decoder application from the command line.  This asks the
    the user for an input and a code index and either encodes or decodes the
    input, based on the user option.
    """

    option = input("press 'E' for encode or 'D' for decode: ").lower()
    if option == 'e':
        print(
              "This program takes known index number (0-5) "\
              "and a number of any length and encodes the number into an "\
              "encoded text string.")
        index = input("Please enter your index: ")
        index = int(index)
        while index < 0 or index > 12:
            print("index is out of range.")
            index = input("Please re-enter your index: ")
            index = int(index)
        encodedresponse = encode(index)

    elif option == 'd':
        index = input("Please enter your index: ")
        index = int(index)
        while index < 0 or index > 12:
            print("index is out of range.")
            index = input("Please re-enter your index: ")
            index = int(index)
        decodednumber = decode(index)
    else:
        print("Invalid response")


main()

# prompts the user for whether they want to rerun the program or quit.
while True:
    responsestr = "\nWould you like to continue?\nPress 'Q' to quit or 'Y' "\
        "to continue: "
    response = input(responsestr).lower()
    if response == 'q':
        break
    elif response == 'y':
        main()
        continue
    else:
        print("Invalid response")
        continue
