def get_random_word():
    target_words = []
    import random
    open_target_words = open("target_words.txt")
    for word in open_target_words:
        target_words.append(word.strip())
    open_target_words.close()
    target_word = random.choice(target_words)
    return target_word


answer = get_random_word()


def get_dict_words():
    """lists dictionary words"""
    dict_words = []
    open_all_words_file = open("all_words.txt")
    for line in open_all_words_file:
        dict_words.append(line.strip())
    open_all_words_file.close()
    return dict_words


def validate_guesses():
    """Verifies guesses' length and legibility"""
    dict_words = get_dict_words()
    guesses = []
    while len(guesses) != 6:
        prompt_user = input("Enter a 5 lettered word here ")
        size_guess = len(prompt_user)
        if size_guess != 5:
            if size_guess > 5:
                prompt_user = input("The word has more than 5 characters - Enter another word here ")
            if size_guess < 5:
                prompt_user = input("The word has less than 5 characters - Enter another word here ")
        if size_guess == 5:
            if prompt_user in dict_words:
                guesses.append(prompt_user)
            if prompt_user not in dict_words:
                prompt_user = input("The word doesn't exist - Enter another word here ")
    else:
        return guesses

                
def validate_guesses_letters_positions(answer):
    guesses_positions_letters = []
    validated_guesses = validate_guesses()
    for index_guess in range(len(validated_guesses)):
        lst_guess = list(validated_guesses[index_guess])
        for index_letter in range(len(lst_guess)):
            if lst_guess[index_letter] not in answer:
                lst_guess[index_letter] = "0"
            if lst_guess[index_letter] == answer[index_letter]:
                lst_guess[index_letter] = "1"
            if lst_guess[index_letter] in answer:
                if lst_guess[index_letter] != answer[index_letter]:
                    if lst_guess.count(lst_guess[index_letter]) == answer.count(answer[index_letter]):
                        lst_guess[index_letter] = "2"
                    #  if lst_guess.count(lst_guess[index_letter]) != answer.count(answer[index_letter]):
                    #  Resolve later
            if index_letter == 4:
                guesses_positions_letters.append(lst_guess)
                if len(guesses_positions_letters) == 6:
                    return guesses_positions_letters, validate_guesses


def colour_guesses_letters():
    letters_positions, wrong_letters, guess = validate_guesses_letters_positions(answer)
    lst_guess = list(guess)
    from termcolor import colored
    index = 0
    while index != 5:
        for num in letters_positions:
            if num == "1":
                lst_guess[index] = colored(guess[index], "green")
            if num == "2":
                lst_guess[index] = colored(guess[index], "yellow")
            if num == "0":
                lst_guess[index] = colored(guess[index], "red")
            if guess[index] in wrong_letters:
                index_wrong_letter = wrong_letters.index(guess[index])
                wrong_letters[index_wrong_letter] = colored(wrong_letters[index_wrong_letter], "red")
            index += 1
            coloured_guess = " ".join(guess)
            coloured_letters = " ".join(wrong_letters)
            return coloured_guess, coloured_letters

            

