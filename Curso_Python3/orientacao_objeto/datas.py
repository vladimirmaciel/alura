class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"Data formatada: {self.dia}/{self.mes}/{self.ano}")
