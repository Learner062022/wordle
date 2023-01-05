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
            # if lst_guess[index_letter] in answer:
            #     if lst_guess[index_letter] != answer[index_letter]:
            #          if lst_guess.count(lst_guess[index_letter]) == answer.count(answer[index_letter]):
            #          Resolve later
            #          if lst_guess.count(lst_guess[index_letter]) != answer.count(answer[index_letter]):
            #          Resolve later
            #          Need to append incorrect letters to a list
            if index_letter == 4:
                lst_guess = "".join(lst_guess)
                guesses_positions_letters.append(lst_guess)
                if len(guesses_positions_letters) == 6:
                    return guesses_positions_letters, validated_guesses
                
      
def colour_guesses_letters(answer):
    positions_letters, predictions = validate_guesses_letters_positions(answer)
    coloured_guesses = []
    from termcolor import colored
    for index_positions_letters in range(len(positions_letters)):
        prediction = predictions[index_positions_letters]
        positions = positions_letters[index_positions_letters]
        lst_prediction = list(prediction)
        for index_position in range(len(positions)):
            if positions[index_position] == "1":
                lst_prediction[index_position] = colored(prediction[index_position], "green")
            if positions[index_position] == "2":
                lst_prediction[index_position] = colored(prediction[index_position], "yellow")
            if positions[index_position] == "0":
                lst_prediction[index_position] = colored(prediction[index_position], "red")
        #  Need to colour incorrect letters
        if index_position == 4:
            coloured_guesses.append("".join(lst_prediction))
            if len(coloured_guesses) == 6:
                return coloured_guesses

            

