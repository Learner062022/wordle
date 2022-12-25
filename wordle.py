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
    validated_guess = validate_guess(answer)
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
                        positions_letters[validated_guess.index(letter)] = "2"
                        letters_checked[validated_guess.index(letter)] = "1"
                        positions_letters[rev_validation.find(letter)] = "0"
                        letters_checked[rev_validation.find(letter)] = "1"
            index += 1
        if index == 5:
            return positions_letters, incorrect_letters, validated_guess


def colour_guesses_letters():
    letters_positions, wrong_letters, guess = validate_guesses_letters(answer)
    from termcolor import colored
    index = 0
    separate_guess = list(guess)
    while index != 5:
        wrong_letters[index] = colored(wrong_letters[index], "red")
        if letters_positions[index] == "1":
            separate_guess[index] = colored(separate_guess[index], "green")
        if letters_positions[index] == "2":
            separate_guess[index] = colored(separate_guess[index], "yellow")
        if letters_positions[index] == "0":
            separate_guess[index] = colored(separate_guess[index], "red")
        index += 1
        connected_guess = " ".join(separate_guess)
        connected_letters = " ".join(wrong_letters)
        return connected_guess, connected_letters

            
def gameplay(answer):
    prediction, unaccepted_letters = colour_guesses_letters()
    num_attempts = 1
    while True:
        attempt_num = "Attempt number " + str(num_attempts) + ":"
        if num_attempts != 7:
            if prediction == answer:
                prediction = input("Winner! Enter Y if you would like to play again, N if not: ")
            if prediction != answer:
                print(attempt_num + "\n" + prediction + "\n" + unaccepted_letters + "\n")
                num_attempts += 1
        if num_attempts == 7:
            prediction = input("No more available attempts, enter Y if you would like to play again, N if not: ")
        if prediction == "Y":
            pass
        if prediction == "N":
            break
