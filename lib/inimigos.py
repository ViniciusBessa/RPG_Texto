from .usuario import Personagem


class Inimigo(Personagem):
    """Classe dos inimigos"""
    def __init__(self, nome, vida, ataque, defesa, pontos_xp, dinheiro):
        super().__init__(vida, ataque, defesa)
        self.__nome = nome
        self.__pontos_xp = pontos_xp
        self.__dinheiro = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos_xp(self):
        return self.__pontos_xp

    @property
    def dinheiro(self):
        return self.__dinheiro


# Inimigos
# Floresta
gnomo = ('Gnomo', 8, 4, 0, 2, 2)
elfo = ('Elfo', 14, 5, 1, 6, 5)
floresta = (gnomo, elfo)

# Caverna
kobold = ('Kobold', 16, 6, 1, 3, 3)
basilisco = ('Basilisco', 30, 12, 12, 12, 11)
caverna = (basilisco, kobold)

# Selva
goblin = ('Goblin', 10, 5, 3, 5, 5)
troll = ('Troll', 14, 8, 6, 7, 8)
selva = (goblin, troll)
