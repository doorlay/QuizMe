# Imports the random module that allows for psuedo-random number generation
import random

# Welcome message to be displayed upon initial running of the program
def welcome():
	print("Welcome to the vocabulary practice!")
	name = input("What's your name?")
	print("Welcome, {}! Let's begin." .format(name))
		  

# Set vocab_list to the content of vocab.txt
vocab_list = open("DOCUMENTS/vocab.txt")

# Set vocab2 to the actual content of vocab.txt
vocab2 = vocab_list.read()

# Set vocab to a list with the content of each line of vocab.txt
vocab = vocab2.splitlines()

# Set definition_list to the content of definitions.txt
definitions_list = open("DOCUMENTS/definitions.txt")

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
def random_one_to_four():
  randomnum = random.randint(1,4)
  return randomnum

# Function that generates a random number between entire index of vocab list
def random_length():
  a = len(vocab) - 1
  randomnum = random.randint(0,a)
  return randomnum


# Function that asks the multiple choice questions.
def frquestion(n):
  # Initial question for the user
  print("Would you like to answer with terms or definitions?")

  # Ask this so we can alternate between asking displaying vocab and definitions.
  choice = input("Type 'terms' or 'definitions':")


  if choice == "definitions":
    choice_two = "What is the definition of"
    choice_three = vocab2.splitlines()
    # We assign 0 to a, so we know that the user is answering with definitions
    a = 0
  elif choice == "terms":
    choice_two = "What is the term for"
    choice_three = definitions2.splitlines()
    # We assign 1 to a, so we know that the user is answering with terms
    a = 1
  else:
    choice_two = "You didn't type either."
    choice_three = "Please restart."
  print("{} {}?" .format(choice_two, choice_three[n] ))

  # Return either 0 or 1 so we know if the user is answering terms or definitions
  return a


# Sub-function for checking multiple choice answers
# b = 0 for answering definitions, 1 for answering terms.
# 'answer' is the users answer
# a is the index of the correct answer
def frcheck(b, answer, a):
  if b == 0:

    # .lower() method is used to make sure case sensitivity while answering is not an issue
    if answer.lower() == definitions[a].lower():
      print("Correct!")
      # Returns 1 if the answer is correct
      return 1
    else:
      print("Wrong!")
      # This prints out the correct answer.
      print("The correct answer was {}." .format(definitions[a]))
      # Returns 0 if the answer is wrong
      return 0
  if b == 1:
    if answer.lower() == vocab[a].lower():
      print("Correct!")
      # Returns 1 if the answer is correct
      return 1
    else:
      print("Wrong!")
      # This prints out the correct answer.
      print("The correct answer was {}." .format(vocab[a]))
      # Returns 0 if the answer is wrong
      return 0

# Function that evaluates the answers for multiple choice questions
def fr():
  # a is assigned to a random number in within the index of the list of vocab/definitions
  a = random_length()

  # b is assigned to either 0 or 1, depending on if the user is inputting terms or definitions
  b = frquestion(a)

  # answer is assigned to the users answers
  answer = input("Answer here:")
  # c is assigned to 0 if the answer is wrong
  # c is assigned to 1 if the answer is right
  c = frcheck(b, answer, a)
  return c


def quizstart():
  welcome()
  length_check()
  
def quiz():
  # This function sends the welcome message and ensures that the length of vocab and definitions are equal
  quizstart()

  # c is assigned to the length of the vocab list, multiplied by two. This value is to be passed into the for loop, to determine the amount of questions to be asked.
  c = len(vocab) * 2

  # b is assigned to either 0 or 1, depending on if answering is wrong or right, respectively
  for x in range(1,c):
    fr()


quiz()
