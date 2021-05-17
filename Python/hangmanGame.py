import sys 
import os

topics = {
    'animals': ['gorilla', 'rhino', 'penguin'],
    'plants': ['cactus', 'ixia', 'rosemary']
}

currentTopic = None 
os.system('clear')

while True:
    topic = input(f'What topic would you like? \nEnter a=animals, b=plants ')
    print(f'You selected topic: {topic}')
    
    if topic == 'a':
        choices = topics['animals']
        currentTopic = 'Animal'
        break
    elif topic == 'b':
        choices = topics['plants']
        currentTopic = 'Plant'
        break
    else:
        print(f'You did not select a or b. You selected {topic}. Try again.')

os.system('clear')
print(f"Let's play hangman!")
    
for choice in choices:
    playerGuessedList = []
    totalLetters = len(choice)
    guessingList = []
    for x in range(0, totalLetters):
        guessingList.append('_')
            
    hangman = 'hangman'
    hangmanList = ['_', '_', '_', '_', '_', '_', '_']
    hangmanCurrentIndex = 0
    print(f'choice = {choice}')
    while True:
        os.system('clear')
        print(f'The topic is: {currentTopic}')
        print(f'\n\tGuess the word: {" ".join(guessingList)}')
        print(f'\n\tHangman wrong guesses: {" ".join(hangmanList)}')
        print(f'\n\tLetters guessed: {playerGuessedList}')
        
        guessCharacter = input(f'\nGuess a letter or the word: ')
        
        if guessCharacter in choice:
            # index = choice.index(guessCharacter)
            indexes = []
            for index, char in enumerate(choice):
                if guessCharacter == char:
                    indexes.append(index)
                    
            for index in indexes:
                guessingList[index] = guessCharacter
        
        if guessCharacter not in choice:
            hangmanList[hangmanCurrentIndex] = hangman[hangmanCurrentIndex]
            hangmanCurrentIndex += 1
            playerGuessedList.append(guessCharacter)
        
        if hangman == ''.join(hangmanList): 
            os.system('clear')
            print(f'\nHangman wrong guesses: {" ".join(hangmanList)}')
            print(f'\nThe word is: {choice}')
            playAgain = input('\nYou lose! Taylor wins! YAY! Do you want to play again? Y or N: ')
            if playAgain in ['Y', 'y']:
                break
            else:
                sys.exit('\nOk sore loser! Bye!\n')
            
            
        if choice == ''.join(guessingList):
            os.system('clear')
            print(f'\n\tGuess the word: {" ".join(guessingList)}')
            playAgain = input('\nYou win! No fair! Do you want to play again? Y or N: ')
            if playAgain in ['Y', 'y']:
                break
            else:
                sys.exit('\nOk! Bye!\n')
        
        

    

    