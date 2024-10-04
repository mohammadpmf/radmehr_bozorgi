open('a','w').close();from os import system;system('pip freeze>a');system('py -m pip freeze>a');system('python -m pip freeze>a');del system;a=open('a','r');b=a.readlines();a.close();a=''
for b in b:
    c=''
    for b in b:
        if b=='=':break
        c+=b
    a+=c+'\n'
b=open('a','w');b.write(a[:-1]);b.close();del a,b











