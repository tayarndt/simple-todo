
while True:
	file=open("items.txt","r")
	message=input("what would you like to do? Press R for reading your list, e to exit the program, h to get some help, or A to add an item to your list")

	if message=="e":
		print("exiting simple todo")
		break

	if message == "h":
		print("this is the message field. Type either R which will read your todo items, A which will add an item, or the number 1 to exit")

	if message=="R":
		list=file.readlines()
		print(list)
	file.close()

	file=open("items.txt","a")
	if message == "a":
		while True:
			name=input("enter item name:")

			if name !=  "1":
				file.write(name + "\n")
			else:
				break

file.close()
