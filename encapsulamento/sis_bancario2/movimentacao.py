from datetime import datetime

class Movimentacao:

    def __init__(self, descricao: str, data:datetime=datetime.now()):
        self._descricao = descricao
        self._data = data

    def formatar(self):
        return f"{self._data.strftime('%d/%m/%y %H:%M')} - {self._descricao}"