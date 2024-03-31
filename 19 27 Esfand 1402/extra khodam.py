import os
for (root,dirs,files) in os.walk("C:/Users/Mohammad/Desktop/Zabt Python", topdown=True):
    print (root)
    print (dirs)
    print (files)
    print ('--------------------------------')