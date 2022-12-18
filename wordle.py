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
print(answer)


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

                
def validate_letters(answer):
    """Returns the letters that are not in the guess and verifies the letters positions
    """
    position_letters = [0, 0, 0, 0, 0]
    letters_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    validation = validate_guess(answer)
    rev_validation = validation[::-1]
    while True:
        for letter in validation:
            index_letter = validation.find(letter)
            if letter not in answer or validation.count(letter) != answer.count(letter):
                if letter not in incorrect_letters:
                    incorrect_letters.append(letter)
                    incorrect_letters.sort()
            if letter not in answer:
                position_letters[index_letter] = "0"
                letters_checked[index_letter] = "1"
            if letter in answer:
                if validation.count(letter) == answer.count(letter) or validation.count(letter) != answer.count(letter):
                    if letter == answer[index_letter]:
                        position_letters[index_letter] = "1"
                        letters_checked[index_letter] = "1"
                if validation.count(letter) < answer.count(letter):
                    if validation[index_letter] != answer[index_letter]:
                        position_letters[index_letter] = "2"
                        letters_checked[index_letter] = "1"
                # if validation.count(letter) > answer.count(letter):
                # pass
                # if validation.count(letter) == answer.count(letter) and validation.count(letter) > 1 and answer.count(letter) > 1:
                # pass
        return position_letters, incorrect_letters
             
        
def colour_letters(answer):
    """Colours the incorrect letters and the guesses letters and returns them 
    """
    pass


def format_display(answer):
    coloured_letters = colour_letters(answer)
    pass
            
                       
def gameplay(answer):
    """Executes the functions until attempts are exhausted"""
    display = format_display(answer)
    num_attempts = 0
#     while num_attempts <= 7:
#         print("Attempt number " + str(num_attempts) + ":" + "\n")
#         validation = validate_guess(answer)
#         print(validation)
#         if validation == answer:
#             print("\n" + "Winner!")
#             break
#         for letter in validation:
#             if validation.count(letter) != answer.count(letter):
#                 if letter not in incorrect_letters:
#                     incorrect_letters.append(letter)
#                     incorrect_letters.sort()
#             if validation.count(letter) == answer.count(letter):
#                 if letter != answer[i]:
#                     position_letter[i] = "2"
#                     letter_checked[i] = "1"
#                 if letter == answer[i]:
#                     position_letter[i] = "1"
#                     letter_checked[i] = "1"
#             if incorrect_letters[i] not in validation:
#                 position_letter[i] = "0"
#                 letter_checked[i] = "1"
#             # if incorrect_letters[i] in validation:
#                 # rev_validation = validation[::-1]
#                 # rev_index = rev_validation.find(letter)
#             i += 1
#             if i == 5:
#                 i = 0
#                 num_attempts += 1
#                 formatted_colours = " ".join(position_letter)
#                 formatted_incorrect_letters = " ".join(incorrect_letters)
#                 display = "\n" + formatted_colours + "\n" + formatted_incorrect_letters + "\n"
#                 print(display)
#     else:
#         print("No more available attempts")


#     gameplay(answer)
