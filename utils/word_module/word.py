from itertools import permutations  # imports a module permutations from itertools package, allowing code to manipulate strings

__all__ = ['Word'] # when exporting, export with the name Word

class Word:
    def __init__(self, phrase):
        self.phrase = phrase          # When calling the Word class, a phrase parameter must be parsed when calling the class

    def createList(self):
        return(list(self.phrase))     # Converts the phrase into a list

    def checkForPattern(self, pattern_1, pattern_2):                                        # Two parameters(patterns), must be parsed when calling the method
        string_permutations = list(permutations(self.phrase))                               # Finds all the possible permutations of the phrase initially parsed, first converting it into a list format
        string_permutations = [''.join(permutation) for permutation in string_permutations] # each permutation is joined from its own separate list with each letter being an element, instead creating one list joining every element together to form the 'word' 
        elements = string_permutations  # The string_permutations variable can be accessed through the key word elements
        
        list_of_elements_not_containing_pattern = [element for element in elements if pattern_1 not in element and pattern_2 not in element]   # Using list comprehension, the string can be treated as a list, then checking if the pattern is within the element, if both patterns are not in the phrase, they will be added to a new list. 

        pattern_not_in_word = len(list_of_elements_not_containing_pattern) # The number of permutations is counted with len and then stored in a variable pattern_not_in_word
        print("The list of the words not containing the pattern are: " + str(list_of_elements_not_containing_pattern)) # The list is displayed
        print("The number of combinations of the word '" + self.phrase + "' that don't contain the pattern(s) '" + pattern_1 + "' or '" + pattern_2 + "' is: " + str(pattern_not_in_word)) # The word and patterns chosen are displayed along with the number of permutations not including the 
        