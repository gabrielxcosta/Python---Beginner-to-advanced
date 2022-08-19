'''
Write a function, word_reverser(), that will take a given string and 
reverse the order of the words. You may assume that the string is a 
sentence that contains only letters and spaces, with all words separated 
by one space.

For example, word_reverser("Codecademy rules") should return "rules 
Codecademy" and word_reverser("May the Fourth be with you") should 
return "you with be Fourth the May". 
'''
def word_reverser(phrase):
    sep_words = phrase.split(' ')
    sep_words.reverse()
    return ' '.join(sep_words)

print(word_reverser('Codecademy rules'))