from module import questoes
from funcao import verifica_resposta, valor_recebido
import time


print("..%%%%...%%..%%...%%%%...%%...%%..........%%%%%....%%%%...........%%...%%..%%%%%%..%%......%%..%%...%%%%....%%%%..")
print(".%%......%%..%%..%%..%%..%%...%%..........%%..%%..%%..%%..........%%%.%%%....%%....%%......%%..%%..%%..%%..%%..%%.")
print("..%%%%...%%%%%%..%%..%%..%%.%.%%..........%%..%%..%%..%%..........%%.%.%%....%%....%%......%%%%%%..%%%%%%..%%..%%.")
print(".....%%..%%..%%..%%..%%..%%%%%%%..........%%..%%..%%..%%..........%%...%%....%%....%%......%%..%%..%%..%%..%%..%%.")
print("..%%%%...%%..%%...%%%%....%%.%%...........%%%%%....%%%%...........%%...%%..%%%%%%..%%%%%%..%%..%%..%%..%%...%%%%..")
print("..................................................................................................................")


print()

name = input(str("Por gentileza, informe seu nome: ")).capitalize()

print(f"Bem vindo ao programa do Show do Milhão, {name}")
time.sleep(2)

print("Vamos começar! ")

print("-=" * 40)
time.sleep(5)
respostas_certas = 0

for pergunta_chave, pergunta_valor in questoes.items():
    print(f'{pergunta_chave}: {pergunta_valor["pergunta"]}')
    print()

    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}]: {resposta_valor}')

    resposta_usuario = input(str("Digite sua resposta: "))

    while verifica_resposta(resposta_usuario) is None:
        resposta_usuario = input(str("Digite sua resposta: "))
        verifica_resposta(resposta_usuario)

    if resposta_usuario == pergunta_valor['resposta_certa']:
        print('Certa resposta!')
        print()
        time.sleep(3)
        respostas_certas += 1
    else:
        print()
        print('Você errou!')
        if respostas_certas == 0:
            print("Você ganhou R$: 300,00 reais")
        time.sleep(3)
        if respostas_certas == 1:
            print()
            print(f"Seu total de acertos foi de : {respostas_certas} questão.")
        else:
            print()
            print(f"Seu total de acertos foi de : {respostas_certas} questões.")
        break

time.sleep(3)
print("-=" * 40)

qtde_perguntas = len(questoes)

total_ganho = respostas_certas

print(valor_recebido(total_ganho))