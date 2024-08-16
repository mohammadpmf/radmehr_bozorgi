from string import ascii_letters, digits, punctuation
import hashlib

def hash_password(password: str, salt="mohammad pourmohammadi fallah"):
    new_password = (password+salt).encode()
    hashed_password = hashlib.sha384(new_password)              # 96 raghame hex
    hashed_password = hashed_password.hexdigest()
    return hashed_password


answers=[]
for i in ascii_letters+digits+punctuation:
    if hash_password(i)==i:
        answers.append(i)
for i in ascii_letters+digits+punctuation:
    for j in ascii_letters+digits+punctuation:
        if hash_password(i+j)==i+j:
            answers.append(i+j)

print(hash_password('lmsX'))