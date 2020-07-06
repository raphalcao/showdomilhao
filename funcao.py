def verifica_resposta(resposta_usuario):
    resposta = ('1', '2', '3', '4')
    for i in resposta:
        if i == resposta_usuario:
            return i


def valor_recebido(total_ganho):
    if total_ganho < 7:
        total_ganho *= 1000 / 2
    elif total_ganho < 15:
        total_ganho *= 10000 / 2
    else:
        total_ganho = 1000000
    return (f"Parabéns! Você rebeceu R$: {total_ganho} reais.")
