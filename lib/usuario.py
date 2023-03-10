import colorama
import os
from random import random, choice
from json import dumps, load
from time import sleep

from .itens import *


def clear():
    """Função para limpar a tela do terminal"""
    print('\n' * 30)


class Personagem:
    """Classe base dos personagens"""

    def __init__(self, vida, ataque, defesa):
        self.__vida = vida
        self.__vida_atual = vida
        self.__ataque = ataque
        self.__defesa = defesa

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

    @property
    def vida_atual(self):
        return self.__vida_atual

    @vida_atual.setter
    def vida_atual(self, nova_vida):
        self.__vida_atual = nova_vida

    @property
    def ataque(self):
        return self.__ataque

    @ataque.setter
    def ataque(self, novo_ataque):
        self.__ataque = novo_ataque

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, nova_defesa):
        self.__defesa = nova_defesa


class Usuario(Personagem):
    """Classe do personagem do usuário"""

    def __init__(self, vida, mana, ataque, defesa, dano_magico):
        super().__init__(vida, ataque, defesa)
        self.__mana = mana
        self.__mana_atual = mana
        self.__dano_magico = dano_magico
        self.__barra_de_xp = 0
        self.__levelup = 10
        self.__level = 1
        self.__dinheiro = 0
        self.__inventario = [['Poção de vida', 0], ['Poção de mana', 0]]
        self.__espada = ['Espada quebrada', 2]
        self.__escudo = ['Escudo enferrujado', 1]
        self.__armadura = ['Armadura enferrujada', 1]

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, nova_mana):
        self.__mana = nova_mana

    @property
    def mana_atual(self):
        return self.__mana_atual

    @mana_atual.setter
    def mana_atual(self, nova_mana):
        self.__mana_atual = nova_mana

    @property
    def dano_magico(self):
        return self.__dano_magico

    @dano_magico.setter
    def dano_magico(self, novo_dano):
        self.__dano_magico = novo_dano

    @property
    def barra_de_xp(self):
        return self.__barra_de_xp

    @barra_de_xp.setter
    def barra_de_xp(self, nova_barra):
        self.__barra_de_xp = nova_barra

    @property
    def levelup(self):
        return self.__levelup

    @levelup.setter
    def levelup(self, novo_levelup):
        self.__levelup = novo_levelup

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, novo_level):
        self.__level = novo_level

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, novo_dinheiro):
        self.__dinheiro = novo_dinheiro

    @property
    def inventario(self):
        return self.__inventario

    @inventario.setter
    def inventario(self, novo_inventario):
        self.__inventario = novo_inventario

    @property
    def espada(self):
        return self.__espada

    @espada.setter
    def espada(self, nova_espada):
        self.__espada = nova_espada

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, novo_escudo):
        self.__escudo = novo_escudo

    @property
    def armadura(self):
        return self.__armadura

    @armadura.setter
    def armadura(self, nova_armadura):
        self.__armadura = nova_armadura

    def batalha(self, oponente):
        """Método que começa uma batalha entre o usuário e um inimigo."""
        print(f'Um(a) {oponente.nome.lower()} se aproxima!')
        sleep(1)
        while oponente.vida_atual > 0:
            cond = 0

            # Status do oponente
            vida_oponente = str(oponente.vida_atual).ljust(4)

            print(
                f'______________________________\n| {oponente.nome.ljust(11)} ', end='')
            print(colorama.Fore.RED, f'Vida: {vida_oponente}    ', end='')
            print(colorama.Style.RESET_ALL, end='')
            print(f'|\n------------------------------')

            # Status do jogador
            vida_jogador = str(self.vida_atual).ljust(2)
            mana_jogador = str(self.mana_atual).ljust(2)

            print(
                f'______________________________\n| Você                       |\n|', end='')
            print(colorama.Fore.RED, f'Vida: {vida_jogador}    ', end='')
            print(colorama.Style.RESET_ALL, end='')
            print(colorama.Fore.BLUE, f'Mana: {mana_jogador}      ', end='')
            print(colorama.Style.RESET_ALL, end='')
            print(f'|\n------------------------------')

            # Menu de ações
            print(f'_________________________________________\n|', end='')
            print(colorama.Fore.YELLOW,
                  f' 1 Atacar   2 Mágia   3 Item   4 Fugir ', end='')
            print(colorama.Style.RESET_ALL, end='')
            print(f'|\n-----------------------------------------')

            # Ações do jogador
            escolha = input('Digite uma das ações: ')

            # Ataque físico
            if escolha.lower() in ('atacar', '1'):
                if self.ataque + self.espada[1] > oponente.defesa:
                    print(
                        f'Você causou {self.ataque + self.espada[1] - oponente.defesa} de dano com a espada!')
                    oponente.vida_atual -= self.ataque + \
                        self.espada[1] - oponente.defesa
                else:
                    print('Seu ataque não causou nenhum dano.')
                cond += 1

            # Ataque mágico
            elif escolha.lower() in ('mágia', '2') and self.mana_atual >= 6:
                print(f'Você causou {self.dano_magico} de dano com a mágia!')
                oponente.vida_atual -= self.dano_magico
                self.mana_atual -= 6
                cond += 1

            # Sem mana para ataque mágico
            elif escolha.lower() in ('mágia', '2') and self.mana_atual < 6:
                print('Mana insuficiente!')
                sleep(2)

            # Item
            elif escolha.lower() in ('item', '3'):
                self.invent()
                opcao = input('Digite um dos itens disponíveis: ')
                if opcao.lower() in pocao_de_vida[0] and self.inventario[0][1] > 0:
                    if self.vida_atual < self.vida - 6:
                        self.vida_atual += 6
                        print('Você recuperou 6 de vida.')
                    else:
                        self.vida_atual = self.vida
                        print('Você recuperou toda sua vida!')
                    self.inventario[0][1] -= 1
                    cond += 1
                elif opcao.lower() in pocao_de_vida[0] and self.inventario[0][1] == 0:
                    print('Você não tem nenhuma poção de vida.')

                elif opcao.lower() in pocao_de_mana[0] and self.inventario[1][1] > 0:
                    if self.mana_atual < self.mana - 5:
                        self.mana_atual += 5
                        print('Você recuperou 5 de mana.')
                    else:
                        self.mana_atual = self.mana
                        print('Você recuperou toda sua mana!')
                    self.inventario[1][1] -= 1
                    cond += 1
                elif opcao.lower() in pocao_de_mana[0] and self.inventario[1][1] == 0:
                    print('Você não tem nenhuma poção de mana.')

                else:
                    print('Opção inválida')

                sleep(2)

            # Fugir
            elif escolha.lower() in ('fugir', '4'):
                if random() > 0.5:
                    print('Você conseguiu fugir!')
                    sleep(2)
                    break
                else:
                    print('O inimigo bloqueou a sua fuga.')
                    cond += 1

            else:
                print('Opção inválida')
                sleep(2)

            # Verificando se o oponente morreu
            if oponente.vida_atual <= 0:
                break

            # Dano do oponente
            if cond != 0 and oponente.ataque > self.escudo[1] + self.armadura[1] + self.defesa:
                print(f'O(a) {oponente.nome.lower()} causou '
                      f'{oponente.ataque - (self.escudo[1] + self.armadura[1] + self.defesa)} de dano.')
                self.vida_atual -= oponente.ataque - \
                    (self.escudo[1] + self.armadura[1] + self.defesa)
                sleep(2)
                clear()

            elif cond != 0:
                print(
                    f'O ataque do(a) {oponente.nome.lower()} não causou nenhum dano.')
                sleep(2)
                clear()

            # Verificando se o jogador morreu
            if self.vida_atual <= 0:
                clear()
                print('GAME OVER!')
                exit()
            clear()

        if oponente.vida_atual <= 0:
            print(f'O(a) {oponente.nome.lower()} morreu!')
            print(f'{oponente.pontos_xp} pontos de xp adquiridos!')
            print(f'{oponente.dinheiro} moedas adquiridas! ')
            self.barra_de_xp += oponente.pontos_xp
            self.dinheiro += oponente.dinheiro
            sleep(2)
            clear()

    def save(self):
        """Método utilizado para salvar o jogo"""
        if not os.path.exists('lib/saveGame'):
            os.mkdir('lib/saveGame')

        with open('lib/saveGame/save.json', 'w') as save:
            save.write(dumps(self.__dict__, indent=2, separators=(',', ': ')))
            print('Jogo salvo com sucesso!')

    def load(self):
        """Método utilizado para carregar o jogo"""
        with open('lib/saveGame/save.json') as save:
            jogo = list(load(save).values())
            self.vida, self.vida_atual, self.ataque, self.defesa, self.mana, self.mana_atual = jogo[
                :6]
            self.dano_magico, self.barra_de_xp, self.levelup, self.level, self.dinheiro = jogo[
                6:11]
            self.inventario, self.espada, self.escudo, self.armadura = jogo[11:15]
        print('Jogo carregado com sucesso!')

    def compra_equip(self, nome_equipamento, tipo_equipamento):
        """Método para efetuar a compra de um equipamento"""
        for equipamento in tipo_equipamento:
            if nome_equipamento == equipamento[0].lower() and self.dinheiro >= int(
                    equipamento[2]):
                print(f'Você comprou e equipou o(a) {nome_equipamento}.')
                self.dinheiro -= int(equipamento[2])

                if nome_equipamento.split()[0] == 'espada':
                    self.espada = equipamento

                elif nome_equipamento.split()[0] == 'escudo':
                    self.escudo = equipamento

                else:
                    self.armadura = equipamento
                return

            elif nome_equipamento == equipamento[0].lower() and self.dinheiro < int(equipamento[2]):
                print(
                    f'Você não tem dinheiro o suficiente para comprar o(a) {nome_equipamento}.')
                sleep(2)
                return
        print(f'Equipamento inválido.')

    def compra_item(self, nome_item, tipo_item):
        """Método para efetuar a compra de um consumível"""
        if nome_item.lower() in tipo_item[0] and self.dinheiro >= int(tipo_item[1]):
            print(f'Você comprou um(a) {nome_item.lower()}.')
            self.dinheiro -= int(tipo_item[1])

            if nome_item in pocao_de_vida[0]:
                self.inventario[0][1] += 1

            elif nome_item in pocao_de_mana[0]:
                self.inventario[1][1] += 1
            return

        elif nome_item.lower() in tipo_item[0] and self.dinheiro < int(tipo_item[1]):
            print(
                f'Você não tem dinheiro o suficiente para comprar o(a) {nome_item.lower()}.')
            return
        print(f'Item inválido.')

    def invent(self):
        """Método para exibir o inventário do usuário"""
        poc_vida = str(self.inventario[0][1]).ljust(2)
        poc_mana = str(self.inventario[1][1]).ljust(2)
        quant_dinheiro = str(self.dinheiro).ljust(3)

        print(colorama.Fore.LIGHTYELLOW_EX)
        print('___________________________________')
        print('|Inventário                        |')
        print('|                                  |')
        print(f'| 1 Poção de vida   Quantidade: {poc_vida} |')
        print(f'| 2 Poção de mana   Quantidade: {poc_mana} |')
        print('|                                  |')
        print(f'|Dinheiro: {quant_dinheiro}                     |')
        print('------------------------------------')
        print(colorama.Style.RESET_ALL, end='')

    def equips(self):
        """Método para ver os equipamentos do usuário"""
        # Recebendo os dados do equipamento do usuário
        espada, dano_espada = self.espada[0], self.espada[1]
        escudo, def_escudo = self.escudo[0], self.escudo[1]
        armadura, def_armadura = self.armadura[0], self.armadura[1]

        # Extendendo o tamanho da string dos equipamentos
        espada = espada.ljust(24)
        escudo = escudo.ljust(24)
        armadura = armadura.ljust(24)

        # Mostrando os dados dos equipamentos
        print(colorama.Fore.LIGHTYELLOW_EX)
        print('_______________________________________________')
        print('|Equipamento                                  |')
        print('|                                             |')
        print(f'|Espada: {espada}   Dano: {dano_espada}   |')
        print(f'|Escudo: {escudo}   Defesa: {def_escudo} |')
        print(f'|Armadura: {armadura} Defesa: {def_armadura} |')
        print('-----------------------------------------------')
        print(colorama.Style.RESET_ALL, end='')

    def status(self):
        """Método para ver os status do usuário"""
        # Ajuste do tamanho dos dados da tabela
        # Ataque e defesa
        stat_ataque = str(self.ataque).ljust(2)
        stat_defesa = str(self.defesa).ljust(2)

        # Dano mágico
        stat_dano_magico = str(self.dano_magico).ljust(2)

        # Barra de xp e levelup
        stat_barra_xp = (str(self.barra_de_xp) + ' XP').ljust(8)
        stat_levelup = (str(self.levelup) + ' XP').ljust(8)

        # Tabela de status
        print(colorama.Fore.LIGHTYELLOW_EX)
        print(f'_________________________')
        print(f'|Status                 |')
        print(f'|                       |')
        print(f'|Level: {self.level}               |')
        print(f'|Vida: {self.vida}    Mana: {self.mana}   |')
        print(f'|Ataque: {stat_ataque}  Defesa: {stat_defesa} |')
        print(f'|Dano mágico: {stat_dano_magico}        |')
        print(f'|Xp atual: {stat_barra_xp}     |')
        print(f'|Próximo nível: {stat_levelup}|')
        print(f'-------------------------')
        print(colorama.Style.RESET_ALL, end='')

    def lvlup(self):
        """Método chamado ao usuário subir de nível"""
        # Level
        self.level += 1
        stat_level = str(self.level).ljust(2)

        # Vida
        self.vida += choice(range(1, 4))
        self.vida_atual = self.vida
        stat_vida = str(self.vida).ljust(3)

        # Mana
        self.mana += choice(range(1, 4))
        self.mana_atual = self.mana
        stat_mana = str(self.mana).ljust(3)

        # Ataque e defesa
        self.ataque += choice(range(3))
        self.defesa += choice(range(2))
        stat_ataque = str(self.ataque).ljust(2)
        stat_defesa = str(self.defesa).ljust(2)

        # Dano mágico
        self.dano_magico += choice(range(1, 3))
        stat_dano_magico = str(self.dano_magico).ljust(2)

        # Barra de xp e levelup
        self.barra_de_xp = 0
        self.levelup += choice(range(4, 8))
        stat_levelup = (str(self.levelup) + ' XP').ljust(6)

        # Mostrandos os dados
        print(colorama.Fore.LIGHTYELLOW_EX)
        print('________________________')
        print('|Level Up!             |')
        print(f'|Level: {stat_level}             |')
        print(f'|Vida: {stat_vida}             |')
        print(f'|Mana: {stat_mana}             |')
        print(f'|Ataque: {stat_ataque}            |')
        print(f'|Defesa: {stat_defesa}            |')
        print(f'|Dano mágico: {stat_dano_magico}       |')
        print(f'|Próximo nível: {stat_levelup} |')
        print('------------------------')
        print(colorama.Style.RESET_ALL, end='')
        sleep(3)


# Personagem do jogador
usuario = Usuario(20, 10, 2, 0, 7)
