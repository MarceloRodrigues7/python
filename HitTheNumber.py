import random

print('Try to hit the hidden number between 1 to 100')
number = random.randrange(1, 101)
print('Starting...')

def check():
    res = input('What is the hidden number?')
    if int(res) == number:
        print('You got the number right: {}. Congratulations!'.format(number))
    elif int(res) < number:
        print('The hidden number is greater than: {}. Try again'.format(res))
        check()
    elif int(res) > number:
        print("The hidden number is less than: {}. Try again".format(res))
        check()
    else:
        print('Validate that you are entering a number!')
        check()

check()
