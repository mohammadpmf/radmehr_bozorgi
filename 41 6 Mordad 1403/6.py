from time import sleep
# f = open('5.txt', 'r')
# for i in range(1000):
#     print(f.readline())
#     sleep(2)
#     5/0
# f.close()

with open('5.txt', 'r') as f:
    for i in range(1000):
        print(f.readline())
        sleep(2)
        5/0