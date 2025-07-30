# verificando tipo de dado
''' Utilizo métodos que verifica tipo de dados, podendo ser utilizado
    em aplicações mais avançadas para verificar dados específicos dependendo
    da aplicação que o desenvolvedor for desenvolver.
'''
    
def validar_str(var):
    print('\nOpções de verificação:')
    print('[1] - Contém apenas espaços?')
    print('[2] - É um número inteiro? (ex: "123")')
    print('[3] - Contém apenas letras? (ex: "abc")')
    print('[4] - É alfanumérico? (letras e números, ex: "a1b2")')
    print('[5] - Está tudo em maiúsculas? (ex: "ABC")')
    print('[6] - Está tudo em minúsculas? (ex: "abc")')
    print('[7] - Está capitalizada? (ex: "Abc")')

    opcao = input('Escolha uma opção (1-7): ')

    if opcao == '1':
        print(f'✅ Contém apenas espaços? {var.isspace()}')
    elif opcao == '2':
        print(f'✅ É um número inteiro? {var.isdigit()}')  # Só números inteiros
    elif opcao == '3':
        print(f'✅ Contém apenas letras? {var.isalpha()}')  # Só letras (sem espaços)
    elif opcao == '4':
        print(f'✅ É alfanumérico? {var.isalnum()}')  # Letras e números (sem espaços)
    elif opcao == '5':
        print(f'✅ Está tudo em maiúsculas? {var.isupper()}')
    elif opcao == '6':
        print(f'✅ Está tudo em minúsculas? {var.islower()}')
    elif opcao == '7':
        print(f'✅ Está capitalizada? {var.istitle()}')
    else:
        print('❌ Opção inválida!')

# Programa principal
while True:
    print('\n--- VERIFICADOR DE STRINGS ---')
    print('[1] - Testar uma string')
    print('[2] - Sair')
    
    escolha = input('Escolha: ')
    
    if escolha == '1':
        texto = input('Digite um texto: ')
        validar_str(texto)
    elif escolha == '2':
        print('Até logo!')
        break
    else:
        print('Opção inválida!')