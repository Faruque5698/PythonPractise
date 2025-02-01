import random
import hangman_words
import hangman_arts

lives = 6
stages = hangman_arts.stages

print(hangman_arts.logo)

randomWord = random.choice(hangman_words.word_lists)

placeHolder = ""

# print("This is the letter: ")

for words in randomWord:
    placeHolder += '_ '
print(placeHolder)

game_over = False
correct_letters = []

while not game_over:
    guess_word = input('\nGuess a letter: ').lower()
    display = ""

    for words in randomWord:
        if guess_word == words:
            display += words
            correct_letters.append(words)
        elif words in correct_letters:
            display += words
        else:
            display += "_ "

    print(display)

    if guess_word not in randomWord:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose')

    if "_ " not in display:
        game_over = True
        print("You won")
    print(stages[lives])