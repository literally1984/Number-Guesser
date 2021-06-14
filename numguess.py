userslow = int(input('Enter your minimum number: '))
usershigh = int(input('Enter your maximum number: '))
print('Please think of a number between ' + str(userslow) + ' and ' + str(usershigh))
maxim = usershigh
incrdcrby = 0.00000000000001
low = userslow
high = maxim
num_guesses = 0
high +=1
newhighscoreornot = False
highscores = open("highscores.txt", "a")
highscores.close()
#highscores = open("highscores.txt", "w")
while True:
    guess = (high + low) // 2
    print('Is your secret number ' + str(guess) + '?')
    num_guesses +=1
    print('')
    x = str(input("Enter 'h' to indicate the guess is too high. \nEnter 'l' to indicate the guess is too low. \nEnter 'c' to indicate the guess is correct. "))
    if x == 'h':
      high = guess
    elif x == 'l':
      low = guess
    elif x == 'c':
      break
    else:
      print('Sorry, I did not understand your input.')
#highscores.close()
highscores = open("highscores.txt", "r") 
highscorecont = highscores.read()
highscoreint = 0
if len(highscorecont) > 0:
    highscoreint = int(highscorecont)
if num_guesses > highscoreint:
   highscores.close()
   highscores = open("highscores.txt", "w")
   highscores.write(str(num_guesses))
   newhighscoreornot = True
highscores.close()
highscores = open("highscores.txt", "r")
print('')
print('Game over. Your secret number was: ' + str(guess) + '.')
print('Your number was guessed in ' + str(num_guesses)  + ' guesses.')
if newhighscoreornot == True:
    print('Your new high score for the most amount of guesses is ' + str(num_guesses) + '.')
    print('Congratulations on setting a new high score!')
else:
    print('Your high score for the most amount of guesses is ' + highscores.read() + '.')
highscores.close()
