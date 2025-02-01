import random

word_list = ['aardvark', 'baboon', 'camel']
# word_list_len = len(word_list)
# print(word_list[random.randint(0,word_list_len-1)])
randomWord = random.choice(word_list)
print(randomWord)
guess_word = input('Guess a letter: ').lower()
for words in randomWord:
    if guess_word == words:
        print('Right')
    else:
        print('Wrong')


