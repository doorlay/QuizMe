# store terms in a data base via a text file
# quizlet type of document


# Welcome message to be displayed upon initial running of the program
def welcome():
	print("Welcome to the vocabulary practice!")
	name = input("What's your name?")
	print("Welcome, {}! Let's begin." .format(name))
		  

# Name the database text file with the vocab, "vocab.txt"
vocab_list = open("vocab.txt")
vocab = vocab_list.splitlines()

