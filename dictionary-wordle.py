def random_word():
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
    
answer = random_word()

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
            print('Enter a word')
            
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
    guesses_letters, guess, answers_letters = dict_answer_guess()
    lst_guess = list(guess)
    incorrect_letters = dict()
    for key in guesses_letters:
        if key in answers_letters:
            for index_letter in range(len(guess)):
                if lst_guess[index_letter] == key:
                    if lst_guess[index_letter] == answer[index_letter]:
                        lst_guess[index_letter] = '1'
                        answers_letters[key] -= 1
                    else:
                        if answers_letters[key] != 0:
                            lst_guess[index_letter] = '2'
                            answers_letters[key] -= 1
                    if answers_letters[key] == 0:
                        if key in lst_guess:
                            index_element = lst_guess.index(key)
                            lst_guess[index_element] = '0'
        else:
            incorrect_letters[key] = incorrect_letters.get(key, 0) + 1
    for key in incorrect_letters:
        if key in lst_guess:
            for element in lst_guess:
                if element == key:
                    index_element = lst_guess.index(key)
                    lst_guess[index_element] = '0'
    return lst_guess, guess, incorrect_letters
                        
def colour_guess():
    num_prediction, estimate, wrong_letters = score_guess()
    lst_estimate = list(estimate)
    from termcolor import colored
    for index_num in range(len(num_prediction)):
        if num_prediction[index_num] == '1':
            lst_estimate[index_num] = colored(estimate[index_num], 'green')
        if num_prediction[index_num] == '2':
           lst_estimate[index_num] = colored(estimate[index_num], 'yellow')
        if num_prediction[index_num] == '0':
             lst_estimate[index_num] = colored(estimate[index_num], 'red')
    lst_wrong_letters = list(wrong_letters.keys())
    lst_wrong_letters.sort()
    for index_letter in range(len(lst_wrong_letters)):
        lst_wrong_letters[index_letter] = colored(lst_wrong_letters[index_letter], 'red')
    return "".join(lst_estimate), "".join(lst_wrong_letters)

def gameplay():
    attempt_number = 0
    global answer
    while True:
        if attempt_number < 6:
            attempt_number += 1
            if answer in guesses:
                prompt = input('Winner! Enter Y here to play again, N if not ')
                if prompt == 'Y':
                    answer = random_word()
                    attempt_number = 0
                else:
                    print('The game has finished')
                    break
            else:
                print('Attempt number ' + str(attempt_number) + ':')
                prediction, wrong_letters = colour_guess()
                print(prediction)
                print(wrong_letters)
        if attempt_number == 6:
            print('Answer was ' + answer)
            prompt = input('No more available attempts! Enter Y here to play again, N if not ')
            if prompt == 'Y':
                answer = random_word()
                attempt_number = 1
            else:
                print('The game has finished')
                break
