def get_random_word():
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
answer = "moons"

def get_dict_words():
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
            
def dict_answer(answer):
    letters_count_answer = dict()
    num_letters_answer = 0
    for letter in answer:
        letters_count_answer[letter] = letters_count_answer.get(letter, 0) + 1
    for key in letters_count_answer:
        num_letters_answer += letters_count_answer[key]
    if num_letters_answer == 5:
        return letters_count_answer
        
def dict_guess():
    validated_guess = validate_guess()
    letters_count_guess = dict()
    num_letters_guess = 0
    for letter in validated_guess:
        letters_count_guess[letter] = letters_count_guess.get(letter, 0) + 1
    for key in letters_count_guess:
        num_letters_guess += letters_count_guess[key]
    if num_letters_guess == 5:
        return letters_count_guess, validated_guess
    

def score_guess(answer):
    guesses_letters, guess = dict_guess()
    answers_letters = dict_answer(answer)
    lst_guess = list(guess)
    incorrect_letters = []
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
            if key not in incorrect_letters:
                incorrect_letters.append(key)
                incorrect_letters.sort() 
        if key in incorrect_letters:
            index_element_guess = lst_guess.index(key)
            lst_guess[index_element_guess] = "0"
        return lst_guess, answer
                        
score_guess(answer)