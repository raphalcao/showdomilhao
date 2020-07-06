import unittest

from funcao import verifica_resposta, valor_recebido


class Testes(unittest.TestCase):

    def test_verifica_resposta(self):
        resposta_usuario = '1'
        self.assertIsNotNone(verifica_resposta(resposta_usuario), 'A função não espera um retorno None.')
    
    def test_valor_recebido(self):
        self.assertEqual(valor_recebido(1000000),"Parabéns! Você rebeceu R$: 1000000 reais.")



if __name__ == '__main__':
    unittest.main()
