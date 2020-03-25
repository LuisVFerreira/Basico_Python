# Estruturas condicionais

# Sistema de login

print('\n >>> Sistema de Login <<<')
login = (input('\nDigite sua cadastro: '))

if login == 'admin':
    print("\n\nSeja bem vindo, administrador!\n\n")
elif login == 'user':
    print('\n\nSeja bem vindo, usuário!\n\n')
else:
    print('\n\nAcesso negado, verifique seu cadastro!\n\n')