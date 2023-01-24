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
    open_all_words_file = open("all_words.txt")
    for word in open_all_words_file:
        word = word.strip()
        dict_words[word] = word
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
            if prompt_user == prompt_user.lower():
                return prompt_user
            else:
                prompt_user = input("The word must be in lowercases - Enter another word here ")
        else:
            prompt_user = input("The word doesn't exist - Enter another word here ")
            
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
                    if answer[index_letter] == key:
                        lst_guess[index_letter] = "1"
                    else:
                        if answers_letters[key] == guesses_letters[key]:
                            index_element = lst_guess.index(key)
                            lst_guess[index_element] = "2"
                        else:
                            if lst_guess[index_letter] == key:
                                lst_guess[index_letter] = "0"
    # edge case moons, nines
        else:
            incorrect_letters[key] = incorrect_letters.get(key, 0) + 1
        if key in incorrect_letters:
            index_element_guess = lst_guess.index(key)
            lst_guess[index_element_guess] = "0"
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
