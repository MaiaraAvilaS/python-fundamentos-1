nomeCandidato = input('Por favor, insira seu nome:')
idadeCandidato = input('Qual a sua idade?')
idadeCandidato = int(idadeCandidato)
renda = input('Por favor, insira a sua renda mensal bruta: R$')
renda = float(renda)

if renda >= 2000 or idadeCandidato >=65: 
    print('PARABÉNS, SEU CRÉDITO FOI APROVADO')
else:
    print('Infelizmente não aprovamos seu crédito, tente novamente')
    