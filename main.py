
import utils # Imports the utils package, containing the word module


user_choice = input("What is the word you would like to check?: ").upper()
user_pattern1 = input("What is the first pattern you would like to check?: ").upper()   # asks the user for their choices
user_pattern2 = input("What is the second pattern you would like to check?: ").upper()
init_word = utils.Word(user_choice)   # calls the class and parses parameters, storing in a variable
init_word.checkForPattern(user_pattern1, user_pattern2)  # calls the checkforpattern function from the word class

