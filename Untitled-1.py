"""Provides the game's instructions"""


def game_introductions():
    print("You have 6 attempts to guess a 5 lettered word. Game completion occurs when:"
          "\n" + "- The guess matches the word."
          "\n" + "- All attempts have been exhausted.")
    print("\n" + "Words that are in the English Dictionary must be used.")
    print("\n" + "Attempts' incrementation begins when the guess is legible, but doesn't match the word.")
    print("\n" + "Guesses' letters will be 1, 2 or 0:"
          "\n" + "1 - the letters are in both words and are in the same position."
          "\n" + "2 - the letters are in the other word but isn't in the same position."
          "\n" + "3 - the letters aren't in the other word.")
    print("\n" + "The incorrect letters will be beneath the guess" + "\n")


"""Chooses a word at random"""


def pick_random_word():
    target_words = []
    import random
    open_target_words_file = open('target_words.txt')
    for line in open_target_words_file:
        target_words.append(line.strip())
    open_target_words_file.close()
    answer = random.choice(target_words)
    return answer


random_word = pick_random_word()
print(random_word)
guesses = []


"""lists all dictionary words"""


def lst_dictionary_words():
    dictionary_words = []
    open_all_words_file = open('all_words.txt')
    for line in open_all_words_file:
        dictionary_words.append(line.strip())
    open_all_words_file.close()
    return dictionary_words


"""Verifies that the guess is the correct length, its characters are letters and the guess exists"""


def validate_guess(random_word):
    dictionary_words = lst_dictionary_words()
    prompt_user = input("Enter a 5 lettered word here - ")
    while True:
        size_prompt = len(prompt_user)
        if size_prompt != 5:
            if size_prompt > 5:
                prompt_user = input("The word has more than 5 characters - Enter another word")
            elif size_prompt < 5:
                prompt_user = input("The word has less than 5 characters - Enter another word")
        elif size_prompt == 5:
            if prompt_user in dictionary_words:
                if prompt_user != random_word:
                    guesses.append(prompt_user)
                    return prompt_user
                elif prompt_user == random_word:
                    return "You guessed the word"
            elif prompt_user not in dictionary_words:
                prompt_user = input("The word doesn't exist - Enter another word")


"""Verifies the letters positions and return the incorrect letters"""


def letter_validation(random_word):
    validation = validate_guess(random_word)
    colours = [0, 0, 0, 0, 0]
    letter_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    i = 0
    for letter in validation:
        if letter in random_word:
            if letter == random_word[i]:
                colours[i] = 1
                letter_checked[i] = 1
            elif letter != random_word[i]:
                colours[i] = 2
                letter_checked[i] = 1
        elif letter not in random_word:
            letter_checked[i] = 1
            if letter not in incorrect_letters:
                incorrect_letters.append(letter)
        i += 1
    return colours, letter_checked, incorrect_letters


def gameplay(random_word, guesses):
    
