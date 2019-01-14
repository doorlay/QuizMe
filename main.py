# Imports the random module that allows for psuedo-random number generation
import random

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

# Function that generates a random number between one and four, inclusive
def randompush():
  randomnum = random.randint(1,4)
  return randomnum


# Function that asks for multiple choice questions.
def multiplechoice(n):
  # Initial question for the user
  print("Would you like to see vocab or definitions first?")

  # Ask this so we can alternate between asking displaying vocab and definitions.
  choice = input("Type 'vocab' or 'definitions':")

  if choice == "vocab":
    choice_two = "definition of"
    choice_three = vocab2.splitlines()
  elif choice == "definitions":
    choice_two = "vocab term for"
    choice_three = definitions2.splitlines()
  else:
    print("You didn't type either. Please restart.")
    
  print("What is the {} {}?" .format(choice_two, choice_three[n] ))
