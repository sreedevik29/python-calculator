def main():
	active = True

	while active:
		print("\nChoose which calculator function you'd like to use: ")
		print("Option 1 - Addition (Type in '1' to choose this option")
		print("Option 2 - Subtraction (Type in '2' to choose this option")
		print("Option 3 - Multiply (Type in '3' to choose this option")
		print("Option 4 - Division (Type in '4' to choose this option")
		print("Option 5 - Quit program (Type in '5' to choose this option")

		option = raw_input("Type in your option now: ")
		
		if option == "1":
			firstnum = raw_input("Type in your first number: ")
			secondnum = raw_input("Type in your second number: ")
			print("The answer is: " + str(int(firstnum) + int(secondnum)))
		elif option == "2":
			firstnum = raw_input("Type in your first number: ")
			secondnum = raw_input("Type in your second number: ")
			print("The answer is: " + str(int(firstnum) - int(secondnum)))
		elif option == "3":
			firstnum = raw_input("Type in your first number: ")
			secondnum = raw_input("Type in your second number: ")
			print("The answer is: " + str(int(firstnum) * int(secondnum)))
		elif option == "4":
			firstnum = raw_input("Type in your first number: ")
			secondnum = raw_input("Type in your second number: ")
			print("The answer is: " + str(int(firstnum) / int(secondnum)))
		else:
			print("Thanks for playing!")
			active = False
	
if __name__ == '__main__':
	main()