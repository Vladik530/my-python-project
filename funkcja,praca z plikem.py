def fin(y,q):
    print(y*q)
fin(3,5)
def fin2(f1,i):
    return f1 + i
try:
    print(fin2(fin(), 7))
except TypeError:
    print("Bład w programie")
print()
file = open("teks.txt","w")
if file.writable():
    file.write(input("Wprowadz tekst:")+ "\n")
file.close()
file = open("teks.txt","r")
if file.readable():
    print(file.read())
