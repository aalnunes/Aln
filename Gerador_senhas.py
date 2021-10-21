from random import choice
import string
from zxcvbn import zxcvbn


def apenas_letras_min(a):
    senha = ''
    valores = string.ascii_lowercase
    for i in range(a):
        senha += choice(valores)
    print(senha)
    resultado = zxcvbn(senha)
    forca_senha =(resultado['score'])
    if forca_senha == 0:
        print('Nivel da senha {} : Muito Fraca.'.format(forca_senha))
    if forca_senha == 1:
        print('Nivel da senha {} : Fraca.'.format(forca_senha))
    if forca_senha == 2:
        print('Nivel da senha {} : Aceitavel.'.format(forca_senha))
    if forca_senha == 3:
        print('Nivel da senha {} : Forte.'.format(forca_senha))
    if forca_senha == 4:
        print('Nivel da senha {} : Muito Forte.'.format(forca_senha))
    suposicoes = (resultado['guesses'])
    print('Quantidade de suposições da senha {}'.format(suposicoes))
    time_hack = (resultado['crack_times_display']['online_no_throttling_10_per_second'])
    print('Tempo estimado para quebrar a senha {}.'.format(time_hack))


def apenas_letras_max(a):
    senha = ''
    valores = string.ascii_uppercase
    for i in range(a):
        senha += choice(valores)
    print(senha)
    resultado = zxcvbn(senha)
    forca_senha = (resultado['score'])
    if forca_senha == 0:
        print('Nivel da senha {} : Muito Fraca.'.format(forca_senha))
    if forca_senha == 1:
        print('Nivel da senha {} : Fraca.'.format(forca_senha))
    if forca_senha == 2:
        print('Nivel da senha {} : Aceitavel.'.format(forca_senha))
    if forca_senha == 3:
        print('Nivel da senha {} : Forte.'.format(forca_senha))
    if forca_senha == 4:
        print('Nivel da senha {} : Muito Forte.'.format(forca_senha))
    suposicoes = (resultado['guesses'])
    print('Quantidade de suposições da senha {}'.format(suposicoes))
    time_hack = (resultado['crack_times_display']['online_no_throttling_10_per_second'])
    print('Tempo estimado para quebrar a senha {}.'.format(time_hack))


def apenas_letras(a):
    senha = ''
    valores = string.ascii_letters
    for i in range(a):
        senha += choice(valores)
    print(senha)
    resultado = zxcvbn(senha)
    forca_senha = (resultado['score'])
    if forca_senha == 0:
        print('Nivel da senha {} : Muito Fraca.'.format(forca_senha))
    if forca_senha == 1:
        print('Nivel da senha {} : Fraca.'.format(forca_senha))
    if forca_senha == 2:
        print('Nivel da senha {} : Aceitavel.'.format(forca_senha))
    if forca_senha == 3:
        print('Nivel da senha {} : Forte.'.format(forca_senha))
    if forca_senha == 4:
        print('Nivel da senha {} : Muito Forte.'.format(forca_senha))
    suposicoes = (resultado['guesses'])
    print('Quantidade de suposições da senha {}'.format(suposicoes))
    time_hack = (resultado['crack_times_display']['online_no_throttling_10_per_second'])
    print('Tempo estimado para quebrar a senha {}.'.format(time_hack))


def apenas_letras_numeros(a):
    senha = ''
    valores = string.ascii_letters + string.digits
    for i in range(a):
        senha += choice(valores)
    print(senha)
    resultado = zxcvbn(senha)
    forca_senha = (resultado['score'])
    if forca_senha == 0:
        print('Nivel da senha {} : Muito Fraca.'.format(forca_senha))
    if forca_senha == 1:
        print('Nivel da senha {} : Fraca.'.format(forca_senha))
    if forca_senha == 2:
        print('Nivel da senha {} : Aceitavel.'.format(forca_senha))
    if forca_senha == 3:
        print('Nivel da senha {} : Forte.'.format(forca_senha))
    if forca_senha == 4:
        print('Nivel da senha {} : Muito Forte.'.format(forca_senha))
    suposicoes = (resultado['guesses'])
    print('Quantidade de suposições da senha {}'.format(suposicoes))
    time_hack = (resultado['crack_times_display']['online_no_throttling_10_per_second'])
    print('Tempo estimado para quebrar a senha {}.'.format(time_hack))


def letras_numeros_simbolos(a):
    senha = ''
    valores = string.ascii_letters + string.digits + string.punctuation
    for i in range(a):
        senha += choice(valores)
    print(senha)
    resultado = zxcvbn(senha)
    forca_senha = (resultado['score'])
    if forca_senha == 0:
        print('Nivel da senha {} : Muito Fraca.'.format(forca_senha))
    if forca_senha == 1:
        print('Nivel da senha {} : Fraca.'.format(forca_senha))
    if forca_senha == 2:
        print('Nivel da senha {} : Aceitavel.'.format(forca_senha))
    if forca_senha == 3:
        print('Nivel da senha {} : Forte.'.format(forca_senha))
    if forca_senha == 4:
        print('Nivel da senha {} : Muito Forte.'.format(forca_senha))
    suposicoes = (resultado['guesses'])
    print('Quantidade de suposições da senha {}'.format(suposicoes))
    time_hack = (resultado['crack_times_display']['online_no_throttling_10_per_second'])
    print('Tempo estimado para quebrar a senha {}.'.format(time_hack))


tamanho = int(input('Informe o tamanho da senha:  '))

opcao = print('Digite [0] = Apenas Letras Minusculas:\n''Digite [1] = Apenas Letras Maiusculas:\n''Digite [2] = Apenas Letras Maisculas e Minusculas:\n''Digite [3] = incluir Numeros:\n''Digite [4] = Incluir Caracteres especiais:')

menu = int(input('Conforme menu acima informe a opção para gerar a senha: '))



if menu == 0:
    apenas_letras_min(tamanho)

if menu == 1:
    apenas_letras_max(tamanho)

if menu == 2:
    apenas_letras(tamanho)

if menu == 3:
    apenas_letras_numeros(tamanho)

if menu == 4:
    letras_numeros_simbolos(tamanho)


