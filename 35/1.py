import hashlib

def hash_password(password: str, salt="mohammad pourmohammadi fallah"):
    new_password = (password+salt).encode()
    hashed_password = hashlib.sha384(new_password)              # 96 raghame hex
    hashed_password = hashed_password.hexdigest()
    return hashed_password
    
print(hash_password('9art9876', '1'))
