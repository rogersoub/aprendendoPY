escrita = 'AUMENTO DE 15% NO SALÁRIO'
print('{:=^100}'.format(escrita))

sal = float(input('Digite seu salário atual em R$: '))
plus = sal*1.15
print('Com um aumento de 15%, seu novo salário é: R$ {:.2f}'.format(plus))