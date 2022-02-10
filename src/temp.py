
DATA = 'data/'

TOTAL_LETTERS = 0
LETTERS_COUNT = {}
LETTER_PROBABILITY = {}


def main():
    file = open(DATA + 'allowed_words.txt', 'r')
    get_letter_count(file)
    get_letter_probability(LETTERS_COUNT)

    print(LETTER_PROBABILITY)


def get_letter_count(file):
    for line in file:
        for letter in line:
            if (letter == '\n'):
                continue
            global TOTAL_LETTERS
            TOTAL_LETTERS += 1
            LETTERS_COUNT[letter] = LETTERS_COUNT.get(letter, 0) + 1


def get_letter_probability(letters):
    for key in letters:
        LETTER_PROBABILITY[key] = LETTERS_COUNT.get(key) / TOTAL_LETTERS


if __name__ == '__main__':
    main()
