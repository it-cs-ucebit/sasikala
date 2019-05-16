# Python Program - Compare Two Strings
		
while True:
	print("Enter 'x' for exit.")
	string1 = input("Enter string1: ")
	string2 = input("Enter string2: ")
	if string1 == 'x':
		break
	else:
		if string1 == string2:
			print("Both Strings are Equal.\n")
		else:
			print("Strings are Not Equal.\n")
