# uma frase diga se é um palindromo (  contrario igual)
frase=str(input('Digite uma frase: ')).strip().upper() #deixar tudo maiusculo e tira os espaços o strip
palavras=frase.split() #dividir as palavras
junto=''.join(palavras) #juntas as palavras
inverso= ''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('Temos um palindromo!')
else:
    print('Não é palindromo!')
