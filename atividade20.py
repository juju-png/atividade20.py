# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM

import random
random_int=random.randint(0, 5)
numero=int(input("numero: "))
if numero == random_int:
    print("parabens voce acertou")
else: 
    print(f"numero errado boco, o certo era {random_int}")