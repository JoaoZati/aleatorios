file_teste = open('teste.txt')
content = file_teste.read()
file_teste.close()
content_list = content.split('\n')

print(file_teste)
print(content)

