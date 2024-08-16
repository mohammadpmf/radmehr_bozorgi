import pyzipper

secret_password = b'lost art of keeping a secret'

with pyzipper.AESZipFile('new_test.zip') as zf:
    zf.setpassword(secret_password)
    my_secrets = zf.read('test.txt')
    string_of_my_secrets = my_secrets.decode()
    print(string_of_my_secrets)
