# imports
import os.path
from os import path

# main function
def main():
	welcome()


#  function to check if file exists and if not creats an empty file for the user
def welcome():
#checks to see if we have the items.txt file. If we do, then the menu function is ran.
	if  (path.exists("items.txt")):
		menu()
	else:
		message = input("Is it okay to create a new file for your items. This app must have a text file to function. Type Y for Yes, or N for no.")
		if message.upper() == "Y":
			file =  open("items.txt","a")
			print("file created successfully. You may now use the program.")
			print("You are going to be taken to the main menu so you can use the program.")
			menu()
		elif message == "N":
			print("Please note that you must have a file for this ap.")
			return file

# function to ask users what options they want
def menu():
	while True:
		message = input("what would you like to do? Type A to add a task, E to exit,H to get some help, R to read your list")
		if message.upper() == "H":
			print("Welcome to the help. Type A to add tasks, R to read your tasks, or E to exit this application.")
		elif message.upper() == "E":
			break
		elif message.upper() =="R":
			readFile()
		elif message.upper() == "A":
			writeFile()

# function to read a file to the user of all there tasks
def readFile ():
	fileToRead = open("items.txt","r")
#need to assign the file in question to another variable because the module won't allow file objects. This module checks the size of the file and tells the user if they have an empty file.
	emptyFile = "items.txt"
	if os.path.getsize(emptyFile) == 0:
		print("You have an empty file of tasks. Try adding some tasks first by typing E to go to the menu and then typing A to add.")
	else:
		line = fileToRead.read()
		line = line.rstrip("\n")
		print(line)
		return fileToRead

# function to append to the file and add items
def writeFile():
	fileToWrite = open("items.txt","a")
	while True:
		task = input("task name:")

		if task.upper() != "E":
			fileToWrite.write(task)
			fileToWrite.write("\n")
		else:
			break
			return fileToWrite
			fileToWrite.close()

main()