escrita = 'Converto em Centimetro e metros'
print('{:=^120}'.format(escrita))
num = float(input('Digite o valor em métros: '))
mm = num/1000
cm = num/100
print('{}m valem {}cm >>> E valem {}mm'.format(num,cm,mm))