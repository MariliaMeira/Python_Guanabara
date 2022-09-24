# mostarr o peso de 5 pessoas. no final, mostre qual foi o maior e o menor peso


maior=0
menor=0
for p in range (1,6):
    peso=float(input(f'Peso da {p}° pessoa: '))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso lido foi de {maior} kg')
print(f'o menor peso lido foi de {menor} kg ')