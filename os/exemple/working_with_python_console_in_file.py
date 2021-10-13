import os
print(os.getcwd())
os.chdir('os/exemple')

with open('../file.txt', 'r') as file:
    print(file.read())
