import os
directory = r'C:\Users\Mohammad\Desktop\My own students\3 Radmehr Bozorgi\44 19 Mordad 1403'
file_path = os.path.join(directory, 'test')
if not os.path.exists(directory):
    os.makedirs(directory)
open(file_path, 'w')