# Welcome message to be displayed upon initial running of the program
def welcome():
	print("Welcome to the vocabulary practice!")
	name = input("What's your name?")
	print("Welcome, {}! Let's begin." .format(name))
		  

# Set vocab_list to the content of vocab.txt
vocab_list = open("vocab.txt")

# Set vocab2 to the actual content of vocab.txt
vocab2 = vocab_list.read()

# Set vocab to a list with the content of each line of vocab.txt
vocab = vocab2.splitlines()

# Set definition_list to the content of definitions.txt
definitions_list = open("definitions.txt")

# Set definitions2 to the actual content of definitions.txt
definitions2 = definitions_list.read()

# Set definitions to a list with the content of each line of definition.txt
definitions = definitions2.splitlines()

# Function to ensure definitions and vocab are the same length
def length_check():
  a = len(definitions)
  b = len(vocab)
  if (a != b):
    print("The definitions and vocab lists appear to not be the same length.")
    print("Please update the lists before you continue.")
  else:
    return True

# Function 
