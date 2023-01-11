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


def validate_guess():
    """Verifies guesses' length and legibility"""
    dict_words = get_dict_words()
    prompt_user = input("Enter a 5 lettered word in lowercases here ")
    size_guess = len(prompt_user)
    if size_guess != 5:
        if size_guess > 5:
            prompt_user = input("The word has more than 5 characters - Enter another word here ")
        else:
            prompt_user = input("The word has less than 5 characters - Enter another word here ")
    else:
        if prompt_user in dict_words:
            return prompt_user
        else:
            prompt_user = input("The word doesn't exist - Enter another word here ")
    
                
def validate_guesses_letters_positions(answer):
    validated_guess = validate_guess()
    incorrect_letters = []
    lst_guess = list(validated_guess)
    for index_letter in range(len(validated_guess)):
        if validated_guess[index_letter] not in answer:
            lst_guess[index_letter] = "0"
            if validated_guess[index_letter] not in incorrect_letters:
                incorrect_letters.append(validated_guess[index_letter])
        if validated_guess[index_letter] == answer[index_letter]:
            lst_guess[index_letter] = "1"
        if validated_guess[index_letter] in answer:
            if validated_guess[index_letter] != answer[index_letter]:
                 if validated_guess.count(validated_guess[index_letter]) == answer.count(answer[index_letter]):
                     lst_guess[index_letter] = "2"
                 else:
                     lst_guess[index_letter] = "0"
        if index_letter == 4:
            return lst_guess, validated_guess, incorrect_letters
            
      
def colour_guesses_letters(answer):
    positions_letters, prediction, incorrect_letters = validate_guesses_letters_positions(answer)
    lst_prediction = list(prediction)
    from termcolor import colored
    for index_positions_letters in range(len(positions_letters)):
        if positions_letters[index_positions_letters] == "1":
            lst_prediction[index_positions_letters] = colored(prediction[index_positions_letters], "green")
        if positions_letters[index_positions_letters] == "2":
            lst_prediction[index_positions_letters] = colored(prediction[index_positions_letters], "yellow")
        if positions_letters[index_positions_letters] == "0":
            lst_prediction[index_positions_letters] = colored(prediction[index_positions_letters], "red")
        if index_positions_letters == 4:
            for index_letter in range(len(incorrect_letters)):
                incorrect_letters[index_letter] = colored(incorrect_letters[index_letter], "red")
                if index_letter == len(incorrect_letters) - 1:
                    return "".join(lst_prediction), "".join(incorrect_letters)
            
            
def gameplay(answer):
    num_attempts = 1
    while True:
        if num_attempts != 7:
            print("Attempt number " + str(num_attempts) + ":")
            predictions, wrong_letters = colour_guesses_letters(answer)
            print(predictions)
            print(wrong_letters)
            num_attempts += 1
            if predictions == answer:
                prompt_user = input("Winner! Enter Y here to play again, N if not?")
                if prompt_user == "N":
                    break
                else:
                   num_attempts = 1 
        else:
            prompt_user = input("No more available attempts! Enter Y here to play again, N if not? ")
            if prompt_user == "N":
                break
            else:
                num_attempts = 1
