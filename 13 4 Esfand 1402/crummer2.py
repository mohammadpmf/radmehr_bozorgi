a = float(input("Enter a (Zarib x dar moadeleye avval): "))
b = float(input("Enter b (Zarib y dar moadeleye avval): "))
c = float(input("Enter c (Zarib x dar moadeleye dovvom): "))
d = float(input("Enter d (Zarib y dar moadeleye dovvom): "))
e = float(input("Enter e (Hasele jame moadeleye avval): "))
f = float(input("Enter f (Hasele jame moadeleye dovvom): "))

makhraj = a*d-b*c
if makhraj==0:
    if e==f:
        print("Moadele Binahayat javab darad.")
    else:
        print("Moadele javab nadarad.")
    exit()

s1 = e*d-b*f
s2 = a*f-c*e
print(f"x={s1/makhraj}")
print(f"y={s2/makhraj}")