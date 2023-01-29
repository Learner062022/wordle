def get_random_word():
    """Puts the target words into a dictionary"""
    target_words = dict()
    import random
    open_target_words = open("target_words.txt")
    for word in open_target_words:
        word = word.strip()
        target_words[word] = word
    open_target_words.close()
    lst_target_words = list(target_words.keys())
    target_word = random.choice(lst_target_words)
    return target_word
    
answer = get_random_word()

def get_dict_words():
    """Puts the dictionary words into a dictionary"""
    dict_words = dict()
    open_all_words = open("all_words.txt")
    for word in open_all_words:
        word = word.strip()
        dict_words[word] = word
    open_all_words.close()
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
        if prompt_user == prompt_user.lower():
            if prompt_user in dict_words:
                dict_guesses[prompt_user] = dict_guesses.get(prompt_user, 0) + 1
                return prompt_user
            else:
                prompt_user = input("The word doesn't exist - Enter another word here ")
        else:
            prompt_user = input("The word must be in lowercases - Enter another word here ")
            
def dict_answer_guess():
    """Puts the guess and the answer into seperate dictionaries"""
    letters_count_answer = dict()
    validated_guess = validate_guess()
    letters_count_guess = dict()
    for letter in answer:
        letters_count_answer[letter] = letters_count_answer.get(letter, 0) + 1
    for letter in validated_guess:
        letters_count_guess[letter] = letters_count_guess.get(letter, 0) + 1
    return letters_count_guess, validated_guess, letters_count_answer

def score_guess():
    """Validates the letters' positions within the guess"""
    guesses_letters, guess, answers_letters = dict_answer_guess()
    lst_guess = list(guess)
    incorrect_letters = dict()
    for key in guesses_letters:
        if key in answers_letters:
            for index_letter in range(len(guess)):
                if lst_guess[index_letter] == key:
                    if lst_guess[index_letter] == answer[index_letter]:
                        lst_guess[index_letter] = "1"
                        answers_letters[key] -= 1
                    else:
                        if answers_letters[key] != 0:
                            lst_guess[index_letter] = "2"
                            answers_letters[key] -= 1
                    if answers_letters[key] == 0:
                        if key in lst_guess:
                            index_element = lst_guess.index(key)
                            lst_guess[index_element] = "0"
        else:
            incorrect_letters[key] = incorrect_letters.get(key, 0) + 1
    for key in incorrect_letters:
        if key in lst_guess:
            for element in lst_guess:
                if element == key:
                    index_element = lst_guess.index(key)
                    lst_guess[index_element] = "0"
    return lst_guess, guess, incorrect_letters
                        
def colour_guess():
    """Colours the letters within the guess"""
    num_prediction, estimate, wrong_letters = score_guess()
    lst_estimate = list(estimate)
    from termcolor import colored
    for index_num in range(len(num_prediction)):
        if num_prediction[index_num] == "1":
            lst_estimate[index_num] = colored(estimate[index_num], "green")
        if num_prediction[index_num] == "2":
           lst_estimate[index_num] = colored(estimate[index_num], "yellow")
        if num_prediction[index_num] == "0":
             lst_estimate[index_num] = colored(estimate[index_num], "red")
    lst_wrong_letters = list(wrong_letters.keys())
    lst_wrong_letters.sort()
    for index_letter in range(len(lst_wrong_letters)):
        lst_wrong_letters[index_letter] = colored(lst_wrong_letters[index_letter], "red")
    return "".join(lst_estimate), "".join(lst_wrong_letters)

def gameplay():
    num_attempts = 1
    while num_attempts != 7:
        print("Attempt number " + str(num_attempts) + ":")
        prediction, wrong_letters = colour_guess()
        print(prediction)
        print(wrong_letters)
        num_attempts += 1
        for key in dict_guesses:
            global answer
            if key == answer:
                prompt_user = input("Winner! Enter Y here to play again, N if not? ")
                if prompt_user == "Y":
                    num_attempts = 1
                    answer = get_random_word()
                else:
                    print("The game has finished")
                    break
    else:
        prompt_user = input("No more available attempts! Enter Y here to play again, N if not? ")
        if prompt_user == "Y":
            num_attempts = 1
            answer = get_random_word()
        else:
            print("The game has finished")
