# https://stackoverflow.com/questions/9210525/how-do-i-convert-hex-to-decimal-in-python
s = "6a48f82d8e828ce82b82"
i = int(s, 16)
print(i)
s = "ab"
i = int(s, 16)
print(i)
i = int(s, 12)
print(i)
i = int(s, 36)
print(i)
s = '34'
i = int(s, 5)
print(i)
print(bin(35))
print('-'*100)
print(0x111) # => 264 + 16 + 1 = 273
print(0o111) # =>  64 +  8 + 1 = 73
print(0b111) # =>   4 +  2 + 1 = 7