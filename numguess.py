print('Please think of a number between 0 and 100!')
maxim = 100
incrdcrby = 0.00000000000001
low = 0
high = maxim
while True:
    guess = (high + low) // 2
    print('Is your secret number ' + str(guess) + '?')
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
print('Game over. Your secret number was: ' + str(guess))
