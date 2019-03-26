# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
WILD_CARD = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    first_component = 0; #variable for holding sum of the points for the letters in the word
    second_component = 0; # holds is 7*wordlen - 3*(n-wordlen), where wordlen is the length of the word and n is the hand length when the word was played

    
    word_list = list(word);
    
    for character in word_list:
        
        first_component += SCRABBLE_LETTER_VALUES[str.lower(character)]; # calculates the sum of the individual characters in the word played by the user
        
    second_component = 7 * len(word) - 3 *( n - len(word));# calculates the score component based on the word played 
    
    if second_component < 0:
        return first_component * 1 ; # second_component is substituted to 1 if the equation (7 * len(word) - 3 *( n - len(word)) results in a negative number
    else:
        return first_component * second_component;
        
    
        
        

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    
    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1;
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand
display_hand(deal_hand(7));
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy();#makes a coppy of the hand dictionary
    word_list = list(word.lower()); 
    #new_hand = dict();
    
    for c in word_list:
        for k in list(hand_copy.keys()):
            if c == k:
                hand_copy[k] = hand_copy.get(k,0) - 1;#iterates thru all the values of the hand dictionary and subtracts the value by 1 if the character in the word is found in the hand dict
                                                        #this is to account for letters that occur more than once in the dictionary
            
    for k in list(hand_copy.keys()):
        if hand_copy[k] <= 0:
            hand_copy.pop(k); #removes the elements from the hand_copy dictionary and returns letters that have not been used yet.
                    
    return hand_copy                
                    
    
    

    
    
    # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
    
def possible_word(word, char_position, word_list, hand):
    
        """
        Takes a string containing the "*" character and returns the Real word replace by a vowel if the word is found in the word_list
        
        word: a string containing one occurence of the special character "*".
        char_position: the position of the character "*" in the word string
        word_list: list of lowercase strings
        """
        character_list = list(word.lower());
        new_word_list = list();
        hand_copy = hand.copy();
        
        new_word_list = [join_words(v , char_position, character_list) for v in VOWELS];
        
        if len(list(set(new_word_list) & set(word_list))) > 0:#check if 
            new_list = list(set(new_word_list) & set(word_list)); # returns a list which contains one word as an element e.g new_list = ['honey']
            #new_string = new_list[0]; #converts the list element to string
            #new_string_list = list(new_string); #converts string characters to list
            
            #hand_copy[new_string_list[char_position]] = hand_copy['*']; # swaps  the key "*" with the character at position char_position
            del hand_copy['*']; #deletes the old key from the dictionary
           # dictionary[new_key] = dictionary.pop(old_key)
            
            return (''.join(new_list) , hand_copy);
            
        else:
            return (-1, -1);
''' 
        for v in VOWELS:
            character_list[char_position] = v;
            new_word = ''.join(character_list);
            new_word_list.append(new_word);
        print(list(set(new_word_list) & set(word_list))); 
'''
        
def join_words(v, char_position, word):
    """
    v: vowel character
    char_position:position of "*" in word
    word: a string containing one occurence of the special character "*".
    
    returns : a string where "*" is replaced by the vowel v in the original word
    """
    character_list = list(word)
    character_list[char_position] = v;
    return ''.join(character_list);
    #new_word_list.append(new_word);
    
def is_valid_word(word, hand, word_list):
    
    
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    found = True;
    new_word = word.lower();
    c_index = 0;
    hand_copy = hand.copy();
    for c in word:
        if c == '*':
            c_index = new_word.find('*')
            new_word, hand_copy  = possible_word(word, c_index, word_list, hand_copy);
           
            
    """        
    for w in word_list:
            if w == word:
                continue;
            else:
                found == False;
    """
    if new_word == -1:
        found = False;
       # print('could find it')
    else:
        list_new_word = list(new_word)
        for c in list_new_word:
            for k in list(hand_copy.keys()):
                if c == k:
                    hand_copy[k] = hand_copy.get(k,0) - 1;
                    found = True;
                    break;
                else:
                    found = False;
            if not found:
                break;
        for k in list(hand_copy.keys()):
            if hand_copy[k] < 0: 
               found = False;
               
        for w in word_list:
            if w == new_word:
                found = True;
                break;
            else:
                found = False;   
        
    if found:
        return found;
    else:
        return found;
    
     # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    sum = 0;
    hand_keys_list = list(hand.keys());
    for i in hand_keys_list:
        sum += hand.get(i, 0);
    return sum;
    
    
      # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
         
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function

    total = 0;
    found = True;
    hand_copy = hand.copy();
    n = calculate_handlen(hand_copy)
    word_list1 = word_list;
    
    while found:
        print('Current Hand:');
        display_hand(hand_copy);
        user_input = str(input('Enter word, or "!!" to indicate that you are finished:'));
    
        word = user_input;
        
        if word == '!!':
           # print('Total score: {} points\n'.format(total));
            found = False;
            break;
        
        if is_valid_word(word, hand_copy, word_list1):
            total += get_word_score(word, n);
            print(word + ' earned {} points. Total: {} points\n'.format(get_word_score(word, n), total));
            hand_copy = update_hand(hand_copy, word);
        else:
            print('That is not a valid word. Please choose another word. \n');
        
        
        
        if len(list(hand_copy.keys())) == 0:
            print('Ran out of letters');
            found = False;
        n = calculate_handlen(hand_copy);
        
    if not found:
        print('Total score for this hand: {} points'.format(total));
        print('-----------------------------------------------------');
    
    return total;
           
    
        
   


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#



def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    alphabet = string.ascii_lowercase;#string containing all alphabetical letters
    hand_copy = hand.copy();
    hand_keys_list = list(hand_copy.keys());
    
    if ''.join(set(letter) & set(hand_keys_list)) != letter: # Checks if the letter provided to be replaced is not an element found in the hand.
        return hand_copy;# return hand unchanged.
    
    new_alphabet = alphabet.replace(letter, ""); #remove the letter to be replaced in the hand from the alphabet string list
    
    random_letter = random.choice(new_alphabet); # chooses a random letter from string
    
    hand_copy[random_letter] = hand_copy[letter]; # swaps  the key "letter" with the new randomly selected character
    del hand_copy[letter]; #deletes the old key from the dictionary
    
    return hand_copy;
   
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    hand_num = input('Enter total number of hands:');
    
    hand = deal_hand(HAND_SIZE);
    new_hand = hand.copy()
    final_total = 0;
    print('Current hand:');
    display_hand(new_hand);
    
    found = True;
    
    while found:
        substitute = str(input('Would you like to substitute a letter? "yes or no": '));
        
        if substitute == 'no':
            final_total += play_hand(new_hand, word_list);
            
        else:
            sub_letter = input('Which letter would you like to replace?');
            new_hand = substitute_hand(new_hand, sub_letter)
            final_total += play_hand(new_hand, word_list);
            
        replay = str(input('Would you like to replay the hand? "yes or no": '));
        
        if replay == 'yes':
            new_hand = hand;
            print('Current hand:', display_hand(new_hand));
            #play_hand(new_hand, word_list);
        else:
            new_hand = deal_hand(HAND_SIZE);
            #print('Current hand:', display_hand(new_hand));
            final_total += play_hand(new_hand, word_list);
            found = False;
            
        #print('Current hand:');
        #display_hand(new_hand);
     
    print('End Game');
        
        
    
    
    
    #print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
"""
if __name__ == '__main__':
    word_list = load_words()
    hand =  {'a': 1, 'p': 1, 'r': 1, '*': 1, 'c': 1, 't': 1, 'i': 1 }
    play_hand(hand, word_list)
    
"""



















