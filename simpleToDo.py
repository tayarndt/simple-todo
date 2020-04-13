import os.path
from os import path

def main():
	welcome()


def welcome():
	if  (path.exists("items.txt")):
		file =  open("items.txt","a")
		menu()
	else:
		file =  open("items.txt","a")
		print("it appears you don't have a text file for your items to be stored in. We will create it now. ")
		print("file created successfully. You may now use the program.")
		file.close()
		return file


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


def readFile ():
	fileToRead = open("items.txt","r")
	for line in fileToRead:
		line = fileToRead.readlines()
		print(line)
		return fileToRead
		fileToRead.close()


def writeFile():
	fileToWrite = open("items.txt","a")
	while True:
		task = input("task name:")

		if task != "1":
			fileToWrite.write(task)
			fileToWrite.write("\n")
		else:
			break
			return fileToWrite
			fileToWrite.close()

main()