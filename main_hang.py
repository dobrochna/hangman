"""Simple console hangman game"""

from library import WordLibrary
from player import Player
from word import Word

'Init game conditions'
game_is_on = True
new_game = True


while game_is_on:

    print('It is a Hangman game, lets start the new one!')
    player_name = input('What is your name? ')

    'Input name and then init a player'
    print('\nHello %s!' % player_name)
    player = Player(player_name)

    'Create library for the game'
    word_library = WordLibrary()

    while new_game:

        'Unpack word informations'
        word = Word(word_library.get_word())

        print('Word category is: %s' % word.word_category)
        print('You can pass wrong letter five times than you are hanged!')
        print('Your chances: ' + '*' * player.chances + '\n')

        'Create places for letters'
        letters_places = word.create_dots_letters()
        print(letters_places)

        'Start guessing letters'
        still_playing = True
        while still_playing:

            'Check if the passed letter is correct'
            incorrect_letter = True
            while incorrect_letter:
                letter = input('Pass letter: ').lower()
                if letter.isalpha() and len(letter) == 1:

                    'Check if letter was passed before'
                    if player.check_letter(letter):
                        print('Ooops you tried that letter before, try the different one!')
                    else:
                        player.add_letter(letter)
                        incorrect_letter = False
                else:
                    print('You can pass only one letter, try one more time!')

            'Check if passed letter is in the word'
            if word.letter_in_word(letter):
                print('Yes! We have that letter!')
                'If letter in the word - change _ for letter'
                letters_places = word.change_letters_dots(letter, letters_places)
                print(letters_places)

                'If all the letters form word were passed'
                if word.check_if_guessed(letters_places):
                    print('Congrats! That was the last missing letter!')
                    print('The word was: %s' % word.word_str)
                    still_playing = False

            else:
                'Wrong letter, decrement chances'
                player.wrong_letter()
                print('Ooops letter %s not in our word!' % letter)

                'Chances ended'
                if player.chances == 0:
                    print('You lose, you dont have more chances...')
                    print('The word was: %s' % word.word_str)
                    still_playing = False

                else:
                    print('Chances left: ' + '*' * player.chances)

        incorrect_decision = True

        'After the game, decision if player wants to play again'
        while incorrect_decision:
            decision = input('Do you want to play again? ')
            if decision == 'n':
                print('Ok, bye!')
                new_game = False
                incorrect_decision = False
            elif decision == 'y':
                print('Ok lets play!')
                player.reset_chances()
                player.clear_letters()
                incorrect_decision = False
            else:
                print("Pass 'y' for yes or 'n' for no!")

    game_is_on = False
