with open('bear.txt') as file:
    content = file.read()

with open('first.txt', 'w') as fist:
    fist.write(content[:90])
