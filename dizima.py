peso = input('Por favor, insira seu peso:') 
peso = float(peso)
altura = input('Por favor, insira sua altura para calcular seu IMC:')
altura= float (altura)
resultado = peso/altura

print(f'Seu IMC é:{resultado:.2f} ')