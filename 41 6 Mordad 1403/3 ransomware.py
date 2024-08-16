import pyzipper
from random import choices
random_name = ''.join(choices('1234567890', k=4))
secret_password = b'2416'

file_name = 'ramz'
with open(f"{file_name}.txt", 'r', encoding='utf-8') as f:
    data = f.read()
    with pyzipper.AESZipFile(f'{file_name}.zip', 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(secret_password)
        zf.writestr(random_name, data)
        zf.writestr(f"{file_name}.txt", data)
