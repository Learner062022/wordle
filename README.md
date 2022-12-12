# 5 lettered words that are in the English dictionary are accepted, and their letters are substituted with integers until the number of attempts equates to 6, or the attempt is identical to the one that must be guessed. 
# Attempts’ iteration increments the other word’s indexer by 1 and the attempts’ letters are compared against the word’s using the indexer value.
# If the iteration is in the word, the element of the list that records the positions of the attempt’s letters are replaced with the correct integer at the index value.
# Iterations are appended to a different list if the letter is not in the answer.
# Attempt’s incrementation of 1 begins when the word is accepted. 
# The list that records the positions of the attempt’s letters, in addition to the one that contains the letters that are not in the word are concatenated and are printed when the indexer’s value is 5.
