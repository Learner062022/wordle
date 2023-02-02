def get_random_word():
    target_words = dict()
    import random
    open_target_words = open("target_words.txt")
    for word in open_target_words:
        word = word.strip()
        target_words[word] = word
    open_target_words.close()
    target_words_keys = list(target_words.keys())
    target_word = random.choice(target_words_keys)
    return target_word
    
answer = get_random_word()

def get_all_words():
    all_words = dict()
    open_all_words = open('all_words.txt')
    for word in open_all_words:
        word = word.strip()
        all_words[word] = word
    open_all_words.close()
    return all_words

guesses = dict()

def validate_guess():
    all_words = get_all_words()
    while True:
        prompt = input('Enter a 5 lettered word in lowercases here ')    
        if prompt != '':
            if len(prompt) != 5:
                print('5 letters')
            else:
                if prompt.isalpha() == False:
                    print('Alphabetical characters')
                else:
                    if prompt.lower() == False:
                        print('Lowercase letters')
                    else:
                        if prompt in all_words:
                            guesses[prompt] = guesses.get(prompt, 0) + 1
                            return prompt
                        else:
                            print('Not existing')
        else:
            print('Enter word')
            
def dict_answer_guess():
    letters_count_answer = dict()
    validated_guess = validate_guess()
    letters_count_guess = dict()
    for letter in answer:
        letters_count_answer[letter] = letters_count_answer.get(letter, 0) + 1
    for letter in validated_guess:
        letters_count_guess[letter] = letters_count_guess.get(letter, 0) + 1
    return letters_count_guess, validated_guess, letters_count_answer

def score_guess():
    letters_guess, guess, letters_answer = dict_answer_guess()
    guess_listed = list(guess)
    incorrect_letters = dict()
    for key in letters_guess:
        if key in letters_answer:
            for index_letter in range(len(guess)):
                if guess_listed[index_letter] == key:
                    if guess_listed[index_letter] == answer[index_letter]:
                        guess_listed[index_letter] = '1'
                        letters_answer[key] -= 1
                    else:
                        if letters_answer[key] != 0:
                            guess_listed[index_letter] = '2'
                            letters_answer[key] -= 1
                    if letters_answer[key] == 0:
                        if key in guess_listed:
                            index_element = guess_listed.index(key)
                            guess_listed[index_element] = '0'
        else:
            incorrect_letters[key] = incorrect_letters.get(key, 0) + 1
    for key in incorrect_letters:
        if key in guess_listed:
            for element in guess_listed:
                if element == key:
                    index_element = guess_listed.index(key)
                    guess_listed[index_element] = '0'
    return guess_listed, guess, incorrect_letters
                        
def colour_guess():
    listed_guess, estimate, wrong_letters = score_guess()
    estimate_listed = list(estimate)
    from termcolor import colored
    for index_number in range(len(listed_guess)):
        if listed_guess[index_number] == '1':
            estimate_listed[index_number] = colored(estimate[index_number], 'green')
        if listed_guess[index_number] == '2':
           estimate_listed[index_number] = colored(estimate[index_number], 'yellow')
        if listed_guess[index_number] == '0':
            estimate_listed[index_number] = colored(estimate[index_number], 'red')
    wrong_letters_listed = list(wrong_letters.keys())
    wrong_letters_listed.sort()
    for index_letter in range(len(wrong_letters_listed)):
        wrong_letters_listed[index_letter] = colored(wrong_letters_listed[index_letter], 'red')
    return "".join(estimate_listed), "".join(wrong_letters_listed)

def gameplay():
    attempt_number = 0
    global answer
    while True:
        if attempt_number < 6:
            attempt_number += 1
            if answer in guesses:
                prompt = input('Winner! Enter Y here to play again, N if not ')
                if prompt == 'Y':
                    answer = get_random_word()
                    attempt_number = 0
                else:
                    print('The game has finished')
                    break
            else:
                print('Attempt number ' + str(attempt_number) + ':')
                prediction, wrong_letters = colour_guess()
                print(prediction)
                print(wrong_letters)
        else:
            print('Answer was ' + answer)
            prompt = input('No more available attempts! Enter Y here to play again, N if not ')
            if prompt == 'Y':
                answer = get_random_word()
                attempt_number = 1
            else:
                print('The game has finished')
                break
