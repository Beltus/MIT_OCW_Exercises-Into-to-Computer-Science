# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
#letter_guessed = [];

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str1 = secret_word;
    secret_word_set = set(str1); # Eliminates all duplicate letters in the secret word
    secret_word_list = list(secret_word_set); # Convert to list so as to enable iteration thru the different elements as sets doesnt support iteration
    guess = letters_guessed;
    i = 0;
    x= 0;
    for i in range(len(guess)):
        for x in range(len(secret_word_list)):
            if guess[i] == secret_word_list[x]:
                secret_word_list.remove(secret_word_list[x]); #removes correct character guesses from the secret_word list when there is a correct guess by player
                break;
            
    
    if len(secret_word_list)==0:# checks whether all words in the secret word have been guessed correctly
        return True;
       
    else:
        return False;
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str1 = secret_word;
    secret_word_list = list(str1);
    guess = letters_guessed;
    
    collect = ['_ ']*len(secret_word_list); #initializes a list with of length "len(secret_word_list)" with every element being an underscore wıth space.
    #print(len(collect));
    #print("Secret word:", str1);
   # print("Letters_guessed", guess);
    for x in range(len(secret_word_list)):
        for i in range(len(guess)):
            if guess[i] == secret_word_list[x]:
                collect[x] = secret_word_list[x]
                break;
                
    return (''.join(collect));# converts list of characters to string object and returns a string of already guessed characters by the player



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess = letters_guessed;

    alphabet_list = list(string.ascii_lowercase);
    
    for i in range(len(guess)):
        for x in range(len(alphabet_list)):
            if guess[i] == alphabet_list[x]:
                alphabet_list.remove(alphabet_list[x]);
                break;
    
    
    return ''.join(alphabet_list);#returns strings of letters that have not been guessed
        
def get_correct_character(secret_word, char_guessed):
    '''
    secret_word: strıng, the word the user is guessing
    char_guessed: char, the character the user inputted as guess
    returns: True if character is found in the secret_word and False otherwise
    '''
    found = False;
    secret_word_list = list(secret_word);
    char_guess = char_guessed;
    for i in range(len(secret_word)):
        if char_guess == secret_word_list[i]:
            found = True;
    if found:
        return found;
    else:
        return found;

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    initial_guess = 6;
    guess_left = initial_guess;
    letters_guessed = list();
    warnings_left = 3;
    string_vowels = 'aeiou';
    end_test = False;
    correct = False;
    
    while guess_left > 0:
         
         #Check if the user correctly guessed the secret word
         if is_word_guessed(secret_word, letters_guessed):
             end_test = True;
             break;    
         print('You have {} guesses left'.format(guess_left));
         print('Available Letters:', get_available_letters(letters_guessed)); #Displays the available letters remaining to be guessed from.
        #Get users guess letter;  
         guess_letter = input('Please guess a letter: ​');  
         while True:
                
          #Check if user ınput ıs valıd
            if str.isalpha(guess_letter):#Checks if entered input is a character
                guess_letter = str.lower(guess_letter);
                
                #Check if the guess character had been prevıously entered by the user and penalize accordingly   
                if get_correct_character(''.join(letters_guessed), guess_letter):
                     warnings_left = warnings_left -1;
                     if warnings_left < 0:
                          guess_left = guess_left - 1;
                          print('Oops! You have already guessed that letter. You have no warnings left so you loose one guess', get_guessed_word(secret_word, letters_guessed));
                          print("-------------");
                     else:
                         print('Oops! You have already guessed that letter. You have {} warnings left'.format(warnings_left),get_guessed_word(secret_word, letters_guessed) );
                         print(get_guessed_word(secret_word, letters_guessed));
                         print("-------------");
                     letters_guessed.append(guess_letter);#append the guess character to the existed list of user guesses
                    
                     break; 
                     
               #Check if guessed character is found in secret word 
                elif get_correct_character(secret_word, guess_letter):
                    letters_guessed.append(guess_letter);#append the guess character to the existed list of user guesses
                    print('Good Guess:', get_guessed_word(secret_word, letters_guessed));
                    print("-------------");
                    break;
            
                     
                #Check if guess character is a vowel and penalize by reducing 2 guesses.     
                elif get_correct_character(string_vowels, guess_letter):
                   letters_guessed.append(guess_letter);#append the guess character to the existed list of user guesses
                   guess_left = guess_left - 2;
                   print('Oops! That letter is not in my word and it is a Vowel. You loose 2 guess:', get_guessed_word(secret_word, letters_guessed));
                   print("-------------");
                   
                   break;
                
                else:
                  guess_left = guess_left - 1;
                  
                  print('Oops! That letter is not in my word1:', get_guessed_word(secret_word, letters_guessed));
                  print("-------------");
                  letters_guessed.append(guess_letter);#append the guess character to the existed list of user guessesy
                  break;
            
            elif warnings_left <= 0:
                guess_left = guess_left - 1;
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed));
                print("-------------");
                break;
             #Letter is not valid alphabetical character 
            else:
                warnings_left = warnings_left -1;
                print('Oops! That is not a valid letter. You have {} warnings left:'.format(warnings_left), get_guessed_word(secret_word, letters_guessed));
                print("-------------");
                break;
               # print('Please, enter a valid alphabetic character!');
              #  guess_letter = input('Please guess a letter: ​');
                
              #User looses one guess when he or she uses all warnings.
           
                #print('You have {} guesses left'.format(guess_left));  
       
    if end_test:
        print("Congratulations, you won!"); 
    else:
        print("Sorry, you ran out of guesses. So you loose. The word was {} !!".format(secret_word));          
         
             
             
    print('Finished!');
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   
    


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
   
    secret_word = choose_word(wordlist)
    warnings = 3;
    print("Welcome to the game Hangman!.");
    print('I am thinking of a word that is {} letters long'.format(len(secret_word)));
    print('You have {} warnings left'.format(warnings));
    print("-------------");
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
