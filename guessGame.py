import random
number = random.randint(1, 100)
guessNumber = input("Guess a number between 1-100: ")
if guessNumber != "q":
	guessNumber = int(guessNumber)
numberList = []
output = "You're guesses were: "


while guessNumber != number and guessNumber != 0:
	if guessNumber < number:
		numberList.append(guessNumber)
		guessNumber = str(input("Too low. Guess again or 'q' to quit: "))
		if guessNumber == "q":
			print("Too bad, better luck next time.")
			guessNumber = 0
		else:
			guessNumber = int(guessNumber)
	if guessNumber > number:
		numberList.append(guessNumber)
		guessNumber = str(input("Too high, guess again or 'q' to quit: "))
		if guessNumber == "q":
			print("Too bad, better luck next time.")
			guessNumber = 0
		else:
			guessNumber = int(guessNumber)


if guessNumber == number:
	numberList.append(guessNumber)
	numberList.sort()
	list = []
	index = 0
	while index < len(numberList):
		if numberList[index] == guessNumber:
			list.append("*" + str(numberList[index]) + "*")
		else:
			list.append(str(numberList[index]))
		index += 1	
	print("That's it! Congratulations!")
	print(output)
	print(list)