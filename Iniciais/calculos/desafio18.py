escrita = 'ALUGUAL DE CARROÇA'
print('{:=^80}'.format(escrita))

km = float(input('Digite a quantidade de km foram rodados: '))
day = float(input('Digite a quantidade de dias que o carro foi alugado: '))
t = (km*0.15) + (day*60)
print('Devido as circunstâncias, o valor total foi: R${} '.format(t))