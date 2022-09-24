# ler 6 numeros inteiros e mostre a soma apenas daquelas que forem pares. se o valor digitado for
#impar desconsidere
soma=0
for c in range(1,7):
    n=int(input(f'Digite o {c} valor: '))
    if n % 2==0:
        soma =soma + n
print(f'A soma dos números pares é {soma}')

