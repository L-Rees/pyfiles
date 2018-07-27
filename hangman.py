word = "rainbow"
wordlist = list(word.lower())
chances = 10
winner = False
wordlength = len(word)
altwordlist = []
for x in range(wordlength):
	altwordlist.append("__ ")

def check_winner():
	if "__" not in altwordlist:
		global winner
		winner = True

def check_letter():
	letter = input("What letter?\n").lower()
	numcorrect = 0
	global chances
	for x in range(wordlength):
		if letter == wordlist[x]:
			altwordlist[x] = letter
			numcorrect += 1
	if numcorrect > 0:
		print("There are {} {} in the word. \nGood guessing!".format(numcorrect, letter))
		return altwordlist
	else:
		print("Sorry. There is no {} in the word.".format(letter))
		chances-=1
		

def status():
	visible_list = ("".join(altwordlist))
	print("You have {} lives remaining.\n{}".format(chances, visible_list))

print("\n\nLet's play hangman!\nThe word has {} letters.\n".format(wordlength))

while chances > 0 and winner == False:
	status()
	choice = int(input("Enter 1 if you want to guess the word \nEnter 2 if you want to guess a letter\n "))
	
	if choice == 1:
		wordguess = input("What word is it? Be careful with your spelling.\n")
		wordguess = wordguess.lower()
		if wordguess == word:
			winner = True
		else:
			print("Nope. {} is not the word.".format(wordguess))
			chances-=1
	elif choice == 2:
		check_letter()	
		
	

if chances <= 0:
	print("Sorry. You lose!")
elif winner == True:
	print("Great job! You guessed right!\nThe word was {}!".format(word))

