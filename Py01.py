# Cálculadora completa

'''Neste algorítimo irei utilizar estrutura condicionais if/else,
   funções e loop de repetição while para manter o código rodando durante
   sua aplicação, será feita uma cálculadora completa que utiliza soma, subtração,
   divisão, potência, raiz quadrada, e cálculos de expressões multiplas(exemplo, 2 + 2 * 3).
'''

import math

def menu():
   print('[0] - sair')
   print('[1] - Adição')
   print('[2] - subtração')
   print('[3] - multiplicação')
   print('[4] - divisão')
   print('[5] - potência')
   print('[6] - raiz quadrada')
   print('[7] - calcular expressões.(Ex: 2 + 2 * 3)')

''' try/except - é utilizado nesta função para evitar erros de síntaxe, exemplo:
    caso seja digitado (2 + *), ele ao inves de quebrar o código, exibirá a mensagem e retornará para o programa 
   '''

def calcular_expressao():
   expressao=input('digite a expressão:')
   try:
      resultado=eval(expressao)  # eval() - função em python que cálcula várias expressões ao mesmo tempo
      print('resultado',resultado)
   except:
      print('erro: digite de maneira correta') 

while True:
   menu()
   choice=input('digite a função desejada:')
   if choice=='0':
      print('fim aplicação')
      break # break para encerrar o loop
   elif choice=='7':
      calcular_expressao()
      continue # para retornar ao loop após o cálculo
   # condições de cálculos mais simples [adição, subtração, divisão, multiplicação]
   elif choice in ["1","2","3","4","5"]:  # tratar erro das variáveis num1 e num2, pois caso o usuário digite uma str no lugar de um número, irá quebrar
      num1=float(input('digite:'))
      num2=float(input('digite:'))
      if choice=='1':
         print('resultado:',num1+num2)
      elif choice=='2':
         print('resultado:',num1-num2)
      elif choice=='3':
         print('resultado:',num1*num2)
      elif choice=='4':
         if num2 !=0: # caso seja maior que zero, o programa ira fluir
            print('resultado:',num1/num2)
         else:
            print('erro: não é possível dividir por zero') # senão, a divisão não ocorrerá
      elif choice=='5':
         print('resultado:',num1**num2)
   # condição de raiz quadrada
   elif choice =='6':
      a=float(input('digite:'))
      if a >= 0:
         print('resultado:',math.sqrt(a)) # importo função da biblioteca
      else:
         print('erro: o número para calcular a raiz quadrada deve não pode ser negativo') # caso seja um valor negativo, o cálculo não será realizado
   else:
      print('opção inválida')
