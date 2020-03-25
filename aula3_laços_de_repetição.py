# Laços de Repetição

# >>> Imprime números 0 até 100

for y in range(101):
    print(y)


# >>> Imprime números até o número informado pelo usuário

num = int(input('\nEntre com um número: '))

for y in range(1, num+1):
    print(y)


# >>> Acerte o número (de 0 a 25)

num = 0

while num != 17:

    print('\n >>> DESAFIO - Acerte o número\n')

    num = int(input('\nEntre com um número: '))  

    if num == 17:
        print("\n\n>>> Acertou, o número é 17!\n\n")
      
    else:
        print('\nErrou, tente novamente...\n')