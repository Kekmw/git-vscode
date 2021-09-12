import random

ugreet = ['hi', 'hello', 'namaste', 'monde', 'hey', ]
mgreet = ['hello im monde', 'hiiii', 'yes?']
while True:
    ui = input()
    fi = ui
    if fi in ugreet:
        ran = random.randint(0, len(mgreet)-1)
        print(mgreet[ran])
