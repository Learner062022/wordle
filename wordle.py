def get_random_word():
    """Chooses a word at random"""
    target_words = []
    import random
    open_target_words = open("target_words.txt")
    for word in open_target_words:
        target_words.append(word.strip())
    open_target_words.close()
    target_word = random.choice(target_words)
    return target_word


answer = get_random_word()
print(answer)


def get_dict_words():
    """lists dictionary words"""
    dict_words = []
    open_all_words_file = open("all_words.txt")
    for line in open_all_words_file:
        dict_words.append(line.strip())
    open_all_words_file.close()
    return dict_words


def validate_guess(answer):
    """Verifies that the guess is the correct length and the guess is legible"""
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
    """Joins the letters that are not in the guess and the positions of the guesses letters after their
    positions are checked
    """
    position_letters = [0, 0, 0, 0, 0]
    letters_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    validated_guess = validate_guess(answer)
    rev_validation = validated_guess[::-1]
    counter = 0 
    while counter != 5:
        for letter in validated_guess:
            if letter not in answer:
                if letter not in incorrect_letters:
                    incorrect_letters.append(letter)
                    incorrect_letters.sort()
            if letter not in answer:
                position_letters[counter] = "0"
                letters_checked[counter] = "1"
            if letter == answer[counter]:
                position_letters[counter] = "1"
                letters_checked[counter] = "1"
            if letter != answer[counter]:
                if validated_guess.count(letter) == answer.count(letter):
                    position_letters[counter] = "2"
                    letters_checked[counter] = "1"
                if validated_guess.count(letter) != answer.count(letter):
                    position_letters[counter] = "0"
                    letters_checked[counter] = "1"
                    if letter in answer:
                        position_letters[validated_guess.index(letter)] = "2"
                        letters_checked[validated_guess.index(letter)] = "1"
                        position_letters[rev_validation.find(letter)] = "0"
                        letters_checked[rev_validation.find(letter)] = "1"
            counter += 1
        if counter == 5:
            position_letters = " ".join(position_letters)
            incorrect_letters = " ".join(incorrect_letters)
            return position_letters, incorrect_letters


var1, var2 = validate_letters(answer)
             
        
def colour_letters(answer):
    validated_letters = validate_letters(answer)
    """Colours the incorrect letters and the guesses letters"""
    pass


def format_display(answer):
    coloured_letters = colour_letters(answer)
    pass
            

def gameplay(answer):
    """Executes the game"""
    formatted_display = format_display(answer)
    pass
