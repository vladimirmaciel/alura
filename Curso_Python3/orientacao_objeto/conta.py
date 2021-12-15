class Conta:

    def __init__(self, numero, titular, saldo, limite):  # função construtora
        # self é a referencia que sabe onde encontrar o objeto na memoria
        print("Construindo objeto...")
        # Deixando os atributos privados com o __
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = "001"

    def extrato(self):
        print(f"Saldo  de {self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):  # metodo privado
        valor_disponivel_a_sacar = self.saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def transfere(self, valor, destino):
        # self.origem.saca(valor)
        # encapsulamento de código utilizamos o self
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

     #  Métodos estáticos tem um cheiro de linguagem procedural já que independe de um objeto para ser chamado e não manipula informações/atributos de objetos. Deve ser usado com bastante cautela!
    @staticmethod
    def codigos_bancos():  # metodo estático faz são da classe, não precisa do self(não precisa do objeto)
        #     # Criando dicionário com códigos dos bancos
        return {"BB": '001', "Caixa": '104', "Bradesco": '237'}
