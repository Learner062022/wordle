def get_random_word():
    """Chooses a random word"""
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


def validate_guess():
    """Verifies guesses' length and legibility"""
    dict_words = get_dict_words()
    prompt_user = input("Enter a 5 lettered word ")
    while True:
        size_guess = len(prompt_user)
        if size_guess != 5:
            if size_guess > 5:
                prompt_user = input("The word has more than 5 characters - Enter another word ")
            if size_guess < 5:
                prompt_user = input("The word has less than 5 characters - Enter another word ")
        if size_guess == 5:
            if prompt_user in dict_words:
                return prompt_user
            if prompt_user not in dict_words:
                prompt_user = input("The word doesn't exist - Enter another word ")

                
def validate_guesses_letters(answer):
    positions_letters = [0, 0, 0, 0, 0]
    letters_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    validated_guess = validate_guess()
    lst_guess = list(validated_guess)
    rev_validation = validated_guess[::-1]
    index = 0
    while index != 5:
        for letter in validated_guess:
            if letter not in answer and letter not in incorrect_letters:
                incorrect_letters.append(letter)
                incorrect_letters.sort()
                positions_letters[index] = "0"
                letters_checked[index] = "1"
            if letter == answer[index]:
                positions_letters[index] = "1"
                letters_checked[index] = "1"
            if letter != answer[index]:
                if validated_guess.count(letter) == answer.count(letter):
                    positions_letters[index] = "2"
                    letters_checked[index] = "1"
                if validated_guess.count(letter) != answer.count(letter):
                    positions_letters[index] = "0"
                    letters_checked[index] = "1"
                    if letter in answer:
                        positions_letters[validated_guess.find(letter)] = "2"
                        letters_checked[validated_guess.find(letter)] = "1"
                        positions_letters[rev_validation.find(letter)] = "0"
                        letters_checked[rev_validation.find(letter)] = "1"
            index += 1
        return positions_letters, incorrect_letters, lst_guess


def colour_guesses_letters(answer):
    letters_positions, wrong_letters, guess = validate_guesses_letters(answer)  # why lists are appearing here
    from termcolor import colored
    index = 0
    while True:
        if index != 5:
            for num in range(len(letters_positions)):
                if num == "1":
                    guess[letters_positions.index(num)] = colored(letters_positions[num], "green")
                if num == "2":
                    guess[letters_positions.index(num)] = colored(letters_positions[num], "yellow")
                if num == "0":
                    guess[letters_positions.index(num)] = colored(letters_positions[num], "red")
                index += 1
        if index == 5:
            index = 0
            for letter in wrong_letters:
                wrong_letters[index] = colored(letter, "red")
                index += 1
        if index == len(wrong_letters):
            coloured_guess = " ".join(guess)
            coloured_letters = " ".join(wrong_letters)
            return coloured_guess, coloured_letters

            

