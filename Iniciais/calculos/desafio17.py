escrita = 'CONVERSOR DE °C PARA FARE'
print('{:=^80}'.format(escrita))

c = float(input('Digite a temperatura em Celsios: '))
fa = c*1.8+32 #para calcular f é só multiplicar por 1,8 e somar 32
print('{}°C de temperatura em °F é {}'.format(c,fa))