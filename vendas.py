produto = 'Computador'
preco = 203.98


quantidade = input('Digite quantas unidades deseja comprar:')
quantidade = int(quantidade)



resultado = quantidade*preco
nomeCliente = input ('Digite seu nome completo:')
doctoCliente = input('Digite seu documento de identificação:')

print('PRODUTO:', produto)
print('Preço unitário: R$',preco)
print('Quantidade desejada:', quantidade)
print(f'Total a pagar: R$, {resultado:.2f}')
print('Cliente (Emissão NF):', nomeCliente)
print('Documento de identificação',doctoCliente)
