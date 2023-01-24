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


dict_guesses = dict()


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
            if prompt_user == prompt_user.lower():
                dict_guesses[prompt_user] = dict_guesses.get(prompt_user, 0) + 1
                return prompt_user
            else:
                prompt_user = input("The word must be in lowercases - Enter another word here ")
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
            if lst_guess[index_letter] != "1":
                if validated_guess.count(lst_guess[index_letter]) == answer.count(lst_guess[index_letter]):
                    lst_guess[index_letter] = "2"
                else:
                    rev_guess = validated_guess[::-1]
                    index_last_duplicate = rev_guess.find(lst_guess[index_letter])
                    lst_guess[index_last_duplicate] = "0"
                    index_init_duplicate = validated_guess.find(lst_guess[index_letter])
                    lst_guess[index_init_duplicate] = "2"
            #  edge case unresolved(answer = moons, guess = nines)
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
    return "".join(lst_prediction), "".join(incorrect_letters)
            
            
def gameplay(answer):
    num_attempts = 1
    while True:
        if num_attempts != 7:
            prediction, wrong_letters = colour_guess()
            print("Attempt number " + str(num_attempts) + ":")
            print(prediction)
            print(wrong_letters)
            num_attempts += 1
            for key in dict_guesses:
                print(key)
                if key == answer:
                    prompt_user = input("Winner! Enter Y here to play again, N if not? ")
        if num_attempts == 7:
            prompt_user = input("No more available attempts! Enter Y here to play again, N if not? ")
        if prompt_user == "N":
            print("The game has finished")
            break
        if prompt_user == "Y":
            num_attempts = 1
            dict_guesses.clear()
        # need get new word
        # need resolve NoneType object
