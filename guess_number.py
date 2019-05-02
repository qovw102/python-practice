#random number practice, game of guess number
import random
start = input('Please enter start number')
end = input('Please enter end number')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1
    num = input('Please enter number:')
    num = int(num)
    if num == r:
        print('Good Job!')
        print(count, 'times guess')
        break
    elif num > r:
        print('number is bigger than answer')
    elif num < r:
        print('number is smaller than answer')
    print(count, 'times guess')

