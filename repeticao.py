while True: 
    nomeProduto = input('Insira a descrição do produto: ')
    quantidade = input ('Digite a quantidade: ')
    quantidade = int (quantidade)
    continuar= input ('Deseja inserir mais um cadastro? SIM[S] OU NÃO[N]')
    if continuar == 'N':
        break
print(f'Produto:{nomeProduto}')
print(f'Quantidade:{quantidade}')
    
