# Herança e Polimorfismo

# from _typeshed import Self


from abc import ABCMeta, abstractclassmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractclassmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


print(Conta(88))
