'''for c in range (1,10):
    print(c)
print('Fim')

c=1
while c < 10:
    print(c)
    c=c+1
print("Fimm")

n=1
while n !=0:
    n=int(input('Digite um valor: ')) #enquanto o numero for diferente de 0 , digite um valor
print('Fim')


r='S'
while r=='S':
    n=int(input('Digite um valor: '))
    r= str(input('Quer comtinuar? [S/N] ')).upper()
print('FIM')

n= 1
par=impar=0
while n !=0:
    n= int(input('Digite um valor:'))
    if n!=0:
        if n % 2==0:
            par +=1
        else:
            impar +=1
print(f'Você digitou {par} números pares e {impar} números impares!')
'''
sexo=str(input('Informe seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MmfF':
    sexo=str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')


