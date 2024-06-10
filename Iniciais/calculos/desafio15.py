escrita = 'DESCONTO DE 5%'
print('{:=^70}'.format(escrita))

val = float(input('Digite o preço em R$: '))
desc = val*0.95
print('com desconto de 5%, o valor agora é: R$ {:.2f}'.format(desc))