import random
print("Welcome to HangMan Game!")
name = input("Name: ")
name_capitalized = name.capitalize()
lives = 15


word_list = ["apple", "banana", "chair", "dream", "elephant", "flower", "guitar", "house", "island", "journey", "kite", "laptop", "mountain", "notebook", "ocean", "pencil", "quiet", "river", "star", "tree", "umbrella", "valley", "water", "xylophone", "yellow", "zebra", "ball", "clock", "desk", "eggfish"]
random_word = random.choice(word_list)


word_lenght = len(random_word)
guessed_word = ["_"] * word_lenght



print(f"Hi {name_capitalized} Are you ready to play? ")
print(f"Your word has {word_lenght} letters. If you can find the word ,you'll win ")
print(guessed_word)


while lives > 0 :
    for i in range(word_lenght): 
        guess = input("Guess a word: ")
        if random_word[i] == guess :
            guessed_word[i] = guess
            print("It's True")
            print(guessed_word)

            
        else:
            print("Wrong guess!")
            lives -= 1 
            print(f"You Have {lives} Lives!")
    if lives == 0:
        print(f"True Word is:  {random_word}")
        print("You Died!")
        break

    if "_" not in guessed_word:
        print("You WON!")      


        
    
    
        
     



