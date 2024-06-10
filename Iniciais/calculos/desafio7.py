n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um Segundo numero: '))

s = n1+n2 #soma
su = n1-n2 #Subtracao
m = n1*n2 #multiplicacao
d = n1 / n2 #divisao
di = n1//n2 #divisao inteira
p = n1**n2 #potenciacao
print('A soma foi {} e a subtração foi {} \n a multiplicação foi {} '.format(s, su, m), end=' >>JUNTOU>> ')#o ,end=11 junta as linhas
print('A divisão foi {:.2f} \n a potência deu {} e a divisão inteira deus {}' .format(d,p,di)) #\n pula as linhas
#{:.2f} coloca duas casas depois da vírgula

