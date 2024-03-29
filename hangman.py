print("Let's play hangman!")

word = str(input("Player 1, please enter a word:    "))
wordSoFar = ["_"] * len(word)
lives = 5
win = False

print("\n\n\n\n\n\n\n\n\n")
print(r"""
 
    _______                  __   
   /  _____|                | _|_  ___
  |  /       __  _  ___     | \  \/  /
  |  |      |  || |/   \ ___|  \    /
  |  |      |  ||  __  |/ _    ||  |
  |  |_____ |  || |  | | (_)   ||  |   
   \_______||__||_|  |_|\___/\_||__|
                                               
                                               
                                             """)
print("\n\n\n\n\n\n\n\n\n")

while win == False and lives > 0:
	letter = input("Player 2, enter a letter that you think is in the word:    ")

	if letter in word:
		print("Yay! The letter is in the word!")
		for i in range(len(word)):
			if word[i] == letter:
				wordSoFar[i] = letter

	else:
		lives -= 1
		print("Sorry, that letter is not in the word.")

	print("You have guessed this much of the word: ", "".join(wordSoFar))
	print("You have" , lives , "lives left. \n")

	if word == "".join(wordSoFar):
		win = True

if win == True:
	print("Congratulations! You have guessed the word correctly.")

else:
	print("Aw! You didn't guess the word.")
	print("The word was ", word, ".")
	print("Better luck next time!")