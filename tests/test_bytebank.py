from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 22

        funcionario_test = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_test.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho
