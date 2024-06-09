import os

os.rename('a.py', 'b.txt')
os.rename('1', '2')

os.rename('b.txt', 'a.py')
os.rename('2', '1')