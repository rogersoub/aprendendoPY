escrita = 'CALCULA ÁREA E LITROS DE TINTA'
print('{:=^160}'.format(escrita))

l = float(input('Digite os núemros de Metros da Largura da parede: '))
a = float(input('Digite os números de Metros da Altura da parede: '))
area = l*a
lTinta = area/2
print('A parede tem uma área de {:.2f}m², precisará de {:.2f}L de tinta'.format(area,lTinta))