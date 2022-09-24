# um programa que leia o ano de nascimetno de 7 pessoas. no final mostre quantas pessoas
# nao atingiram a maioridade e quantas já sao maiores.
from datetime import date
atual=date.today().year
tot=0
totmenor=0
for pess in range(1,8):
    nasc=int(input(f'Em que ano a {pess}° pessoa nasceu? '))
    idade= atual-nasc
    if idade>=21:
       tot +=1
    else:
       totmenor+=1
print(f'Ao todos tivemos {totmenor} menores de idade e {tot} pessoas maiores de idade!')
