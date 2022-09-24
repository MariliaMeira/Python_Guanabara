print(("gerador de pa"))
print('-='*10)
primeiro=int(input('primeiro termo: '))
razao= int(input('razao da pa'))
termo=primeiro
cont=1
total=0
mais=10
while mais!=0:
    total=total+mais
    while cont <=total:
        print(f'{termo}-->',end='')
        termo+=razao
        cont +=1
    print('PAUSA')
    mais=int(input('Quantos termos voce quer mostrar a mais? '))
print(f'progressao finalizada com {total} termos mostrados!')