
def game_intructions():
    '''Provides the game's instructions'''
    print("You have 6 attempts to guess a 5 lettered word. Game completion occurs when:"
          "\n" + "- The guess matches the word."
          "\n" + "- All attempts have been exhausted.")
    print("\n" + "Words that are in the English Dictionary must be used.")
    print("\n" + "Attempts' incrementation begins when the guess is legible, but doesn't match the word.")
    print("\n" + "Guesses' letters will be 1, 2 or 0:"
          "\n" + "1 - the letters are in both words and are in the same position."
          "\n" + "2 - the letters are in the other word but isn't in the same position."
          "\n" + "3 - the letters aren't in the other word.")
    print("\n" + "The guesse's incorrect letters will be beneath the guess." + "\n")


def random_word():
    '''Chooses a word at random'''
    target_words = []
    import random
    open_target_words = open('target_words.txt')
    for line in open_target_words:
        target_words.append(line.strip())
    open_target_words.close()
    target_word = random.choice(target_words)
    return target_word


answer = random_word()


def lst_dict_words():
    '''lists dictionary words'''
    dict_words = []
    open_all_words_file = open('all_words.txt')
    for line in open_all_words_file:
        dict_words.append(line.strip())
    open_all_words_file.close()
    return dict_words


def validate_guess(answer):
    '''Verifies that the guess is the correct length, its characters are letters and the guess is legible'''
    dict_words = lst_dict_words()
    prompt_user = input("Enter a 5 lettered word here - ")
    while True:
        size_prompt = len(prompt_user)
        if size_prompt != 5:
            if size_prompt > 5:
                prompt_user = input("The word has more than 5 characters - Enter another word")
            elif size_prompt < 5:
                prompt_user = input("The word has less than 5 characters - Enter another word")
        elif size_prompt == 5:
            if prompt_user in dict_words:
                return prompt_user
            elif prompt_user not in dict_words:
                prompt_user = input("The word doesn't exist - Enter another word")


def gameplay(answer):
    '''Verifies the guesse's letters positions, return the incorrect letters beneath the guess and the attempt number'''
    i = 0
    colours = [0, 0, 0, 0, 0]
    letter_checked = [0, 0, 0, 0, 0]
    incorrect_letters = []
    num_attempts = 0
    game_intructions()
    while num_attempts <= 6:
        print("Attempt number " + str(num_attempts) + ":" + "\n")
        validation = validate_guess(answer)
        print(validation)
        if validation == answer:
            print("Winner!")
            break
        for letter in validation:
            if letter in answer:
                if letter == answer[i]:
                    colours[i] = "1"
                    letter_checked[i] = "1"
                elif letter != answer[i]:
                    colours[i] = "2"
                    letter_checked[i] = "1"
            elif letter not in answer:
                colours[i] = "0"
                letter_checked[i] = "1"
                if letter not in incorrect_letters:
                    incorrect_letters.append(letter)
            i += 1
            if i == 5:
                i = 0
                num_attempts += 1
                formatted_colours = " ".join(colours)
                formatted_incorrect_letters = " ".join(incorrect_letters)
                display = "\n" + formatted_colours + "\n" + formatted_incorrect_letters + "\n"
                print(display)
    else:
        print("No more available attempts")

  
gameplay(answer)
