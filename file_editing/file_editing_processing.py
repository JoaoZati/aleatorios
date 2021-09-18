"""
Define a function that gets a caracter and a filepath and returns the count of this caracter
"""


def caracter_to_filepath(caracter: str, filepath: str):
    if len(caracter) != 1:
        print('caracter must have 1 item')
        return

    letter = str(caracter)
    with open(filepath) as file:
        content = file.read()

    return len([i for i in content if i == letter])

def caracter_otimizado(caracter: str, filepath: str):
    file = open(filepath)
    content = file.read()
    return content.count(caracter)

if __name__ == '__main__':
    caracter = input('Digite uma letra: ')
    filepath = input('Digite um caminho: ')

    print(caracter_otimizado(caracter, filepath))
    print(caracter_to_filepath(caracter, filepath))

