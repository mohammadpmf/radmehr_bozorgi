import os

for cur_dir, dirs, files in os.walk('C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/22 31 Farvardin 1403'):
    for file in files:
        os.remove(os.path.abspath(f"{cur_dir}/{file}"))
for cur_dir, dirs, files in os.walk('C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/22 31 Farvardin 1403'):
    for dir in dirs:
        try:
            os.rmdir(os.path.abspath(f"{cur_dir}/{dir}"))
        except:
            pass
for cur_dir, dirs, files in os.walk('C:/Users/Mohammad/Desktop/My own students/3 Radmehr Bozorgi/22 31 Farvardin 1403'):
    for dir in dirs:
        try:
            os.rmdir(os.path.abspath(f"{cur_dir}/{dir}"))
        except:
            pass

