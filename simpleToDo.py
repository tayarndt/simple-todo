# imports
import os.path
from os import path

# main function
def main():
	welcome()


#  function to check if file exists
def welcome():
	if  (path.exists("items.txt")):
		file =  open("items.txt","a")
		menu()
	else:
		message = input("Is it okay to create a new file for your items. This app must have a text file to function. Type Y for Yes, or N for no.")
		if message.upper() == "Y":
			file =  open("items.txt","a")
			print("file created successfully. You may now use the program.")
		elif message == "N":
			print("Please note that you must have a file for this ap.")
			file.close()
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
	line = fileToRead.readlines()
	print(line)
	return fileToRead
	fileToRead.close()

# function to append to the file and add items
def writeFile():
	fileToWrite = open("items.txt","a")
	while True:
		task = input("task name:")

		if task.upper() != "E":
			taskData = task,"\n"
			fileToWrite.write(str(taskData))
		else:
			break
			return fileToWrite
			fileToWrite.close()

main()