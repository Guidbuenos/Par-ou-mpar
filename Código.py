from random import randint

print('--------PAR OU IMPAR--------')
v = 0
while True:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {computador}. Total de {total}')
    print('Deu par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!!')
            break

    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')
