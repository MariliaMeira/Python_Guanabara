# um número inteiro e dizer se ele é ou não é primo
n=int(input('Digite um número: '))
tot=0
for c in range(1,n +1):
    if n % c == 0:
        print('\033[33m',end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(c,end=' ')
print(f'\n\033[m O numero {n} foi dividido {tot} vezes!')
if tot==2:
    print('E por isso ele é um número primo!')
else:
    print('E por isso ele náo é um número primo! ')