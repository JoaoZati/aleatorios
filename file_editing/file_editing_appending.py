# a append a+ read, append write same time

with open('teste.txt', 'a+') as myfile:
    myfile.write('\nOkra')
    myfile.seek(0)
    content = myfile.read()

print(content)