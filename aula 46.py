"""

n=int(input('Digite um número: '))
for c in range(0, n+1):          #contar de 0 até o numero digitado
    print(c)
print("FIM")
"""
from time import sleep         #biblioteca de esperar
for cont in range(10,-1,-1):    #contar de 10 a 0 em decrescente
    print(cont)
    sleep(1)              #1 segundo
print('Bum! Bum! pooow!')