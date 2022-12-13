def get_random_word():
    '''Chooses a word at random'''
    lst_target_words = []
    import random
    open_target_words = open('target_words.txt')
    for word in open_target_words:
        lst_target_words.append(word.strip())
    open_target_words.close()
    target_word = random.choice(lst_target_words)
    return target_word


answer = get_random_word()


def get_dict_words():
    '''lists dictionary words'''
    lst_dict_words = []
    open_all_words_file = open('all_words.txt')
    for line in open_all_words_file:
        lst_dict_words.append(line.strip())
    open_all_words_file.close()
    return lst_dict_words


def validate_guess(answer):
    '''Verifies that the guess is the correct length, its characters are letters and the guess is legible'''
    dict_words = get_dict_words()
    prompt_user = input("Enter a 5 lettered word here - ")
    while True:
        size_prompt = len(prompt_user)
        if size_prompt != 5:
            if size_prompt > 5:
                prompt_user = input("The word has more than 5 characters - Enter another word ")
            elif size_prompt < 5:
                prompt_user = input("The word has less than 5 characters - Enter another word ")
        elif size_prompt == 5:
            if prompt_user in dict_words:
                return prompt_user
            elif prompt_user not in dict_words:
                prompt_user = input("The word doesn't exist - Enter another word ")


def gameplay(answer):
    '''Verifies the guesse's letters positions, returns the incorrect letters and the attempt number'''
    i = 0
    position_letter = [0, 0, 0, 0, 0]
    letter_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    num_attempts = 1
    while num_attempts <= 7:
        print("Attempt number " + str(num_attempts) + ":" + "\n")
        validation = validate_guess(answer)
        print(validation)
        if validation == answer:
            print("Winner!")
            break
        for letter in validation:
            if letter in answer and validation.count(letter) != answer.count(letter) or letter not in answer:
                position_letter[i] = "0"
                letter_checked[i] = "1"
                if letter not in incorrect_letters:
                    incorrect_letters.append(letter)
                    incorrect_letters.sort()
                    " ".join(incorrect_letters)
            if letter in answer and letter == answer[i] and letter in incorrect_letters:
                position_letter[i] = "1"
                letter_checked[i] = "1"
#             if letter in answer and validation.count(letter) > answer.count(letter) and letter in incorrect_letters:
#                 position_letter[validation.find(letter)] = "2"
#                 letter_checked[i] = "1"
#                 rev_validation = validation[::-1]
#                 rev_index = rev_validation.find(letter)
#                 letter_checked[rev_index] = "0"
            if letter in answer and validation.count(letter) == answer.count(letter) and letter != answer[i]:
                position_letter[i] = "2"
                letter_checked[i] = "1"
            if letter in answer and validation.count(letter) == answer.count(letter) and letter == answer[i]:
                position_letter[i] = "1"
                letter_checked[i] = "1"
            i += 1
            if i == 5:
                i = 0
                num_attempts += 1
                formatted_colours = " ".join(position_letter)
                formatted_incorrect_letters = " ".join(incorrect_letters_ordered)
                display = "\n" + formatted_colours + "\n" + formatted_incorrect_letters + "\n"
                print(display)
    else:
        print("No more available attempts")

  
gameplay(answer)
