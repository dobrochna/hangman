from re import finditer, sub


class Word(object):
    def __init__(self, rand_word):
        self.word_str = rand_word[0]
        self.word_category = rand_word[1]
        self.word_length = rand_word[2]
        self.word_spaces = rand_word[3]

    def create_dots_letters(self):
        dots = '_ ' * self.word_length
        if self.word_spaces[0] != 0:
            for value in range(1, len(self.word_spaces)):
                dots = ''.join((dots[:self.word_spaces[value] * 2], ' ',
                                dots[self.word_spaces[value] * 2 + 1:]))
        return dots

    def letter_in_word(self, letter):
        return letter in self.word_str

    def change_letters_dots(self, letter, letters_places):
        founded_letters = finditer(letter, self.word_str)
        for element in founded_letters:
            letter_index = element.span()[1]
            letters_places = ''.join((letters_places[:(letter_index - 1) * 2], letter,
                                      letters_places[letter_index * 2 - 1:]))
        return letters_places

    def check_if_guessed(self, letters_places):
        return sub(' ', '', letters_places) == sub(' ', '', self.word_str)
