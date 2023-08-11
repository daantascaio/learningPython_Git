# Exemplo de uso dos sets

dataSet = set()

while True:
    letra = input('Digite: ')
    dataSet.add(letra.lower())

    if 'l' in dataSet:
        print('Yeeeah <3')
        break

    print(dataSet)