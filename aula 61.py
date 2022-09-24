# um programa que leia o primeiro termo e a razao de uma pa.
# no final, mostre os 10 primeiros termos dessa progressão.

print(("gerador de pa"))
print('-='*10)
primeiro=int(input('primeiro termo: '))
razao= int(input('razao da pa'))
termo=primeiro
cont=1
while cont <=10:
    print(f'{termo}-->',end='')
    termo+=razao
    cont +=1

