from random import randint
from time import sleep
computador = randint(0, 5)  # faz o computador pensar

print('-=' * 24)
print('vou passar um numero de 0 a 7 tente adivinhar')
print('-=' * 24)

nu = int(input('em qual numero eu pensei?'))
print('processando...')
sleep(2)
if nu == computador:
    print('parabéns você ganhou')
else:
    print(f'você perdeu eu pensei no número {computador} e não no {nu}')