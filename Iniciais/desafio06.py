#teste 1
nome = input("Qual é o seu nome? ")
print('Olá {}'.format(nome*20)) #Inprimindo o nome 20 vezes

#teste 2
print('Olá {:20}!'.format(nome)) #Imprime o nome depois dá 20 espaços

#teste 3
print('Olá {:^20}!'.format(nome)) #Inprimindo o nome em 20 espaços, no centro

#teste 4
print('Olá {:<20}!'.format(nome)) #Inprimindo o nome a esquerda e 20 espaços

#teste 5
print('Olá {:>20}!'.format(nome)) #Inprimindo o nome a direitaroger e 20 espaços

#teste 5
print('Olá {:=^20}!'.format(nome)) #Coloca o nome no meio e preenche os 20 espaços com =====