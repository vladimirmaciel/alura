class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):  # sempre que formos comparar valores temos que implementar este metodo
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>> Código {} Saldo {} <<<]".format(self._codigo, self._saldo)


contaA = ContaSalario(21)
contaB = ContaSalario(21)
contaA.deposita(100)
contaB.deposita(100)
print(contaA == contaB)
