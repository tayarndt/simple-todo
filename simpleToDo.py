
while True:
	file=open("items.txt","r")
	message = input("what would you like to do? Press R for reading your list, E to exit the program, H to get some help, or A to add an item to your list")
	message = message.upper()

	if message=="E":
		break

	if message == "H":
		print("this is the message field. Type either R which will read your todo items, A which will add an item, or the number 1 to exit")

	if message== "R":
		list=file.readlines()
		print(list)
	file.close()

	file=open("items.txt","a")

	if message == "A":
		while True:
			name=input("enter item name:")

			if name !=  "1":
				file.write(name + "\n")
			else:
				break

file.close()
