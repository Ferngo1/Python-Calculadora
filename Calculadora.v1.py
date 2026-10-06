import os

def soma (num1, num2):
    return num1 + num2

def subtrai (num1, num2):
    return num1 - num2

def multi (num1, num2):
    return num1 * num2

def divi (num1, num2):
    return num1 / num2

opcao = 1

while(opcao):
    opcao = int(input("=======================================\n"
                      "=            CALCULADORA              =\n" 
                      "=======================================\n"
                      "= 1 - SOMA                            =\n"
                      "= 2 - SUBTRAÇÃO                       =\n"
                      "= 3 - MULTIPLICAÇÃO                   =\n"
                      "= 4 - DIVISÃO                         =\n"
                      "=======================================\n"
                      "= Escolha a operação: "))

    if opcao >= 1 and opcao <= 4:

        os.system("cls")
        num1 = int(input('Digite um Número: '))
        num2 = int(input('Digite um Número: '))

        if opcao == 1:
            print('\nOperação Selecionada: Soma')
            print('\nResultado da Soma:', soma(num1, num2))

        elif opcao == 2:
            print('\nOperação Selecionada: Subtração')
            print('\nResultado da Subtração:', subtrai(num1, num2))

        elif opcao == 3:
            print('\nOperação Selecionada: Multiplicação')
            print('\nResultado da Multiplicação:', multi(num1, num2))
            
        elif opcao == 4:
            print('\nOperação Selecionada: Divisão')
            print('\nResultado da Divisão:', divi(num1, num2))

        else:
            print('Opção Inválida!')

        novaOpcao = int(input('\n======================================\n'
                              '= Deseja Realizar uma Nova Operação? =\n'
                              '= 1 - Sim                            =\n' \
                              '= 2 - Não                            =\n' \
                              '======================================\n' \
                              '= Digite a Opção Desejada: '))
        
        os.system("cls")

        if novaOpcao == 2:
            print('= Programa Encerrado, Até mais! =')
            break
    else:
        print('Insira um valor entre as opções!')