#random number practice, game of guess number
import random
r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = input('Please enter number:')
    num = int(num)
    if num == r:
        print('Good Job!')
        break
    elif num > r:
        print('number is bigger than answer')
    elif num < r:
        print('number is smaller than answer')
    print(count, 'times guess')

