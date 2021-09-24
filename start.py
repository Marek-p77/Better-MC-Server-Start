import os

print("---------------------------")
print("|                         |")
print("|  Server Controller      |")
print("|  Version 0.1 by Marek_p |")
print("|                         |")
print("---------------------------")

print("[1] Zapnout server.  RAM: 1024MB")
print("[2] Zapnout server.  RAM: 2048MB")
print("[3] Zapnout server.  RAM: 3072MB")
print("[4] Zapnout server.  RAM: 4096MB")
print("[5] Zapnout server.  RAM: 5120MB")
print("[6] Zapnout server.  RAM: 6144MB")
print("[7] Zapnout server.  RAM: 7168MB")
print("[8] Zapnout server.  RAM: 8192MB")
print("[9] Exit")

answer = input("Zvol číslo podle toho co mám dělat: ")

if answer == "1":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx1024M -jar server.jar nogui')

if answer == "2":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx2048M -jar server.jar nogui')

if answer == "3":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx3072M -jar server.jar nogui')

if answer == "4":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx4096M -jar server.jar nogui')

if answer == "5":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx5120M -jar server.jar nogui')

if answer == "6":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx6144M -jar server.jar nogui')

if answer == "7":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx7168M -jar server.jar nogui')

if answer == "8":
    print("Spouštím server")
    os.system('java -Xms128M -Xmx8192M -jar server.jar nogui')

else:
    print("Bye :)")
