# um programa que leia o primeiro termo e a razao de uma pa.
# no final, mostre os 10 primeiros termos dessa progressão.

primeiro=int(input('Primeiro termo: '))
razao= int(input('Razão: '))
decimo=primeiro+(10-1)*razao
for c in range(primeiro,decimo + razao,razao):
    print(c)