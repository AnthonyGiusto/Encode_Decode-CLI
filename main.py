from encode import Encode
from decode import Decode


def main():

	option = input("press 'E' for encode or 'D' for decode: ").lower()
	if option == 'e':

		month = input("Please enter your index: ")
		month = int(month)
		while month < 0 or month > 12:
				print("index is out of range.")
				month = input("Please re-enter your index: ")
				month = int(month)
				continue
		encodednumber = Encode(month)
		encodedresponse = encodednumber.encode()

	elif option == 'd':
		month = input("Please enter your index: ")
		month = int(month)
		while month < 0 or month > 12:
				print("index is out of range.")
				month = input("Please re-enter your index: ")
				month = int(month)
				continue
		decodednumber=Decode(month)
		decodedresponse = decodednumber.decode()
	else:
		print ("Invalid response")

main()
while True:
	response = input("\nWould you like to continue?\nPress 'Q' to quit or 'Y' to continue: ").lower()
	if response == 'q':
		break
	elif response == 'y':
		main()
		continue
	else:
		print ("Invalid response")
		continue