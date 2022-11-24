import os

def get_cont(num):
    num = str(num)
    return '0'*(3-len(num)) + num

cont = 0
for entry in os.scandir('.'):
    cont += 1
    if entry.is_file():
        if entry.name != 'rename.py':
            os.rename(entry.name, get_cont(cont)+'.jpg')