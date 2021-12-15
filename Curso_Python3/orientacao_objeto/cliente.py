class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # proprieades
    @property
    def nome(self):
        print("chamando @propetry nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando @propetry nome()")
        self.__nome = nome
