#random number practice, game of guess number
import random
r = random.randint(1,100)

while True:
    num = input('Please enter number:')
    num = int(num)
    if num == r:
        print('Good Job!')
        break
    elif num > r:
        print('num is bigger than answer')
    elif num < r:
        print('num is smaller than answer')

