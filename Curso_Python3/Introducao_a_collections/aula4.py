# Objetos próprios
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>  Código {} saldo {}  <<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
# print(conta_do_gui)
conta_do_gui.deposita(500)
# print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
# print(conta_da_dani)


def deposita_para_todos(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todos(contas)
print(contas[0], contas[1])
