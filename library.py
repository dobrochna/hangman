"""Word library for hangman game"""

from random import randint


class WordLibrary(object):

    def __init__(self):
        """Init the library"""
        self.library = [['alligator', 'animal', 9, (0, )], ['arctic fox', 'animal', 10, (1, 6)],
                        ['bumblebee', 'animal', 9, (0, )], ['blue ring octopus', 'animal', 17, (2, 4, 9)],
                        ['cockroach', 'animal', 9, (0, )], ['cookiecutter shark', 'animal', 18, (1, 12)],
                        ['desert tortoise', 'animal', 15, (1, 6)], ['eastern bluebird', 'animal', 16, (1, 7)],
                        ['falling star', 'astronomy', 12, (1, 7)], ['gravitational constant', 'astronomy', 22, (1, 13)],
                        ['hubble telescope', 'astronomy', 16, (1, 6)], ['interstellar dust', 'astronomy', 17, (1, 12)],
                        ['journalist', 'jobs', 10, (0, )], ['karate teacher', 'jobs', 14, (1, 6)]]

    def get_word(self):
        """Get the word from the library and than delete it - no repetition"""
        word_number = randint(0, len(self.library)-1)
        word = self.library[word_number]
        del self.library[word_number]
        return word
