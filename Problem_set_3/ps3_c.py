from ps3 import *
import time


#
# Computer chooses a word
#

def is_valid_word_in_hand(word, hand):
    """
    Returns True if word is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)

    """
    flag = True

    hand_copy = hand.copy()

    for letter in word:
        if letter in hand_copy:
            hand_copy[letter] -= 1
        else:
            return False

    for i in hand_copy.values():
        if i < 0:
            flag = False
    return flag


def comp_choose_word(hand, word_list, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.
    This word should be calculated by considering all the words
    in the wordList.
    If no words in the wordList can be made from the hand, return None.
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    score = 0
    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in word_list:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if is_validWord_in_hand(word, hand) == True:

            # Find out how much making that word is worth
            score = get_word_score(word, n)
            # If the score for that word is higher than your best score
            if score > maxScore:
                # Update your best score, and best word accordingly
                maxScore = score
                bestWord = word

    # return the best word you found.
    return bestWord


##print compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
##print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
##print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
##print compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)
##print compChooseWord({'b': 1}, wordList, 1)

#
# Problem #7: Computer plays a hand
#
def comp_play_hand(hand, word_list, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.
    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """

    total = 0
    hand_copy = hand.copy()
    best_word = comp_choose_word(hand_copy, word_list, n)

    while best_word != None:
        # As long as there are still choice for computer:

        # Display the hand
        print('Current Hand: ', display_hand(hand_copy))

        # let computer to choose the best word
        total += get_word_score(best_word, n)
        print('\"', best_word, '\"', 'earned', get_word_score(best_word, n), 'points. Total: ', total, 'points')
        print()
        hand_copy = update_hand(hand_copy, best_word)
        best_word = comp_choose_word(hand_copy, word_list, n)

    if best_word == None:
        if sum(hand_copy.values()) != 0:
            print('Current Hand: ', display_hand(hand_copy))
            print('Total score: ', total, ' points.')
            print()

        else:
            print('Total score: ', total, ' points.')
            print()

            ##compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)


##compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
##compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)

#
# Problem #8: Playing a game
#
def playG_came(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.
    4) After the computer or user has played the hand, repeat from step 1
    wordList: list (string)
    """

    # Solution 1
    hand = {}

    while True:
        getInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print
        if getInput == 'e':
            return None

        elif getInput not in ('n', 'r'):
            print('Invalid command.')

        elif hand == {} and getInput == 'r':
            print('You have not played a hand yet. Please play a new hand first!')

        elif getInput == 'n' or getInput == 'r':  # if input is 'n' then need to get new hand, and store it for repeat later
            if (getInput == 'n'):
                hand = deal_hand(HAND_SIZE)
                hand_copy = hand.copy()
            else:  # if input is 'r', use the hand which saved previously
                hand = hand_copy.copy()

            while True:
                getInputCom = input('Enter u to have yourself play, c to have the computer play: ')
                print

                if getInputCom == 'u':
                    play_hand(hand, word_list, HAND_SIZE)
                    print
                    break

                elif getInputCom == 'c':
                    comp_play_hand(hand, word_list, HAND_SIZE)
                    print
                    break

                else:
                    print('Invalid command.')
                    print

                    # ---------------------------------------------------------------------------------------------------------------------
                    ##Solution 2
    hand = {}

    while True:
        getInput = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print
        if getInput == 'e':
            return None

        elif hand == {} and getInput == 'r':
            print('You have not played a hand yet. Please play a new hand first!')

        elif getInput == 'n' or getInput == 'r':

            while True:
                getInputCom = input('Enter u to have yourself play, c to have the computer play: ')
                print

                if getInputCom == 'u':
                    if getInput == 'n':
                        hand = deal_hand(HAND_SIZE)
                    play_hand(hand, word_list, HAND_SIZE)  # equals to avoid: elif getInput == 'r':
                    print
                    break

                elif getInputCom == 'c':
                    if getInput == 'n':
                        hand = deal_hand(HAND_SIZE)
                    comp_play_hand(hand, word_list, HAND_SIZE)  # equals to avoid: elif getInput == 'r':
                    print
                    break

                else:
                    print('Invalid command.')
                    print
        else:
            print('Invalid command.')

            ## other solutions:
            ## https://raw.githubusercontent.com/jdhuasirui/MITx--CMITx--6.00.1x-Introduction-to-CS-and-Programming-Using-Python/master/Problem%20Set%204_b.py
            # -------------------------------------------------------------------------
            ##Solution 3
    isFirst = True
    n = HAND_SIZE
    while 1:
        choice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if (choice == 'e'):
            break
        elif (choice != 'r' and choice != 'n'):
            print("Invalid command.\n")
        elif (isFirst and choice is 'r'):
            print("You have not played a hand yet. Please play a new hand first!\n")
        else:
            isFirst = False
            while 1:
                choice2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if (choice2 == 'c'):
                    if (choice == 'n'):
                        hand = deal_hand(n)
                    comp_play_hand(hand, word_list, n)
                    break
                elif (choice2 == 'u'):
                    if (choice == 'n'):
                        hand = deal_hand(n)
                    play_hand(hand, word_list, n)
                    break
                else:
                    print("Invalid command.\n")
                    #


# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)