import pyzipper
file_name = 'ramz'
numbers='0123456789'
for i1 in numbers:
    for i2 in numbers:
        for i3 in numbers:
            for i4 in numbers:
                guess = i1+i2+i3+i4
                guess = bytes(guess.encode(encoding='utf-8'))
                with pyzipper.AESZipFile(f'{file_name}.zip') as zf:
                    zf.setpassword(guess)
                    try:
                        my_secrets = zf.read(f'{file_name}.txt')
                        string_of_my_secrets = my_secrets.decode(encoding='utf-8')
                        with open('result', 'w', encoding='utf-8') as r:
                            r.write(string_of_my_secrets)
                        print(f"The password is {guess}")
                        exit()
                    except RuntimeError:
                        print(guess)
                        pass