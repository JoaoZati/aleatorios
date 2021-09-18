with open('teste.txt') as myfile:
    content = myfile.read()

print(content)

with open('teste_write.txt', 'w') as myfile:
    myfile.write("Tomato")

with open('teste_write.txt', 'w') as myfile:
    myfile.write("Lemon\nTomato")
    myfile.write('\nGarlic')

