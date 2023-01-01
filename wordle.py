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
    positions_letters = [0, 0, 0, 0, 0]
    guesses_incorrect_letters = []
    guesses_positions_letters = []
    validated_guesses = validate_guesses()
    index = 0
    incorrect_letters = []
    while len(guesses_positions_letters) != 6:
        for guess in validated_guesses:
            while index != 5:
                for letter in guess:
                    if letter not in answer and letter not in incorrect_letters:
                        incorrect_letters.append(letter)
                        incorrect_letters.sort()
                        positions_letters[index] = "0"
                    if letter == answer[index]:
                        positions_letters[index] = "1"
                    if letter != answer[index]:
                        if guess.count(letter) == answer.count(letter):
                            positions_letters[index] = "2"
                        if guess.count(letter) != answer.count(letter):
                            positions_letters[index] = "0"
                            if letter in answer:
                                rev_validation = guess[::-1]
                                positions_letters[guess.find(letter)] = "2"
                                positions_letters[rev_validation.find(letter)] = "0"
                    index += 1
            else:
                guesses_positions_letters.append(positions_letters)
                guesses_incorrect_letters.append(incorrect_letters)
                index = 0
                incorrect_letters.clear()
    else:
        return guesses_positions_letters, guesses_incorrect_letters, validated_guesses


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

            

