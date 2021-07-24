import colorama
from random import choice
from time import sleep

from .itens import *
from .usuario import usuario, clear
from .inimigos import floresta, caverna, selva, Inimigo


def menu_principal():
    """Função para chamar o menu principal"""
    print('Menu principal')
    print('_________________')
    print('| Novo jogo     |')
    print('| Carregar jogo |')
    print('-----------------')
    jogo = input('Digite uma das opções: ')

    if jogo.strip(" ").lower() == 'novo jogo':
        clear()
        print('Novo jogo iniciado!')

    elif jogo.strip(" ").lower() == 'carregar jogo':
        try:
            clear()
            usuario.save('carregar')
            print('Jogo carregado com sucesso!')

        except FileNotFoundError:
            print('Arquivo de save não encontrado.')
            sleep(2)
            clear()
            menu_principal()
    else:
        print('Opção inválida.')
        sleep(2)
        clear()
        menu_principal()


def menu_opcoes():
    """Função para chamar o menu de opções"""
    print('Menu de opções')
    print('________________________')
    print('|  Viajar   Descansar  |')
    print('|  Status   Equips     |')
    print('|  Salvar   Inventário |')
    print('|  Sair                |')
    print('------------------------')
    opcao = input('Digite uma das opções do menu: ')
    clear()

    if opcao.strip(" ").lower() == 'viajar':
        viajar(opcao)
        clear()
        menu_opcoes()

    elif opcao.strip(" ").lower() == 'descansar':
        usuario.vida_atual = usuario.vida
        usuario.mana_atual = usuario.mana
        print('Você monta uma tenda para descansar um pouco...')
        print('Descansando, você recupera vida e mana!')
        sleep(2)
        clear()
        menu_opcoes()

    elif opcao.strip(" ").lower() == 'status':
        usuario.status()
        sleep(2)
        clear()
        menu_opcoes()

    elif opcao.strip(" ").lower() == 'equips':
        usuario.equips()
        sleep(2)
        clear()
        menu_opcoes()

    elif opcao.strip(" ").lower() == 'salvar':
        clear()
        usuario.save('salvar')
        menu_opcoes()

    elif opcao.strip(" ").lower() in ['inventario', 'inventário']:
        usuario.invent()
        sleep(2)
        clear()
        menu_opcoes()

    elif opcao.strip(" ").lower() == 'sair':
        print('Programa finalizado.')
        exit()

    else:
        print('Opção inválida')
        sleep(2)
        clear()
        menu_opcoes()


def viajar(opcao):
    """Função para viajar"""
    if opcao.strip(" ").lower() == 'viajar':
        while True:
            print('Locais disponíveis')
            print('________________________')
            print('|  Floresta   Caverna  |')
            print('|  Vila       Selva    |')
            print('------------------------')
            local = input('Digite um dos locais, ou sair para voltar ao menu de opções: ')

            if local.strip(" ").lower() == 'floresta':
                inimigo = Inimigo(*choice(floresta))
                usuario.batalha(inimigo)

            elif local.strip(" ").lower() == 'caverna':
                inimigo = Inimigo(*choice(caverna))
                usuario.batalha(inimigo)

            elif local.strip(" ").lower() == 'vila':
                while True:
                    clear()
                    print('Ao entrar na vila, você vê diversas tavernas e lojas')
                    print('________________________')
                    print('| Apotecário  Ferreiro |')
                    print('------------------------')
                    local = input('Digite uma das opções, ou sair: ')
                    clear()

                    if local.strip(" ").lower() == 'apotecario' or local.strip(" ").lower() == 'apotecário':
                        clear()
                        while True:
                            dinheiro = str(usuario.dinheiro).ljust(4)
                            print('Apotecário')
                            print('____________________________')
                            print('| Poção de vida  Preço: 10 |')
                            print('| Poção de mana  Preço: 10 |')
                            print('|                          |')
                            print(f'| Dinheiro: {dinheiro}           |')
                            print('----------------------------')
                            escolha = input('Digite o nome de uma das poções, ou sair: ')

                            if escolha.strip(" ").lower() in pocao_de_vida[0]:
                                usuario.compra_item(escolha, pocao_de_vida)

                            elif escolha.strip(" ").lower() in pocao_de_mana[0]:
                                usuario.compra_item(escolha, pocao_de_mana)

                            elif escolha.strip(" ").lower() == 'sair':
                                break

                            else:
                                print('Opção inválida.')
                            sleep(2)
                            clear()

                    elif local.strip(" ").lower() == 'ferreiro':
                        while True:
                            dinheiro = str(usuario.dinheiro).ljust(4)
                            print('Ferreiro')
                            print('_____________')
                            print('| Espadas   |')
                            print('| Escudos   |')
                            print('| Armaduras |')
                            print('-------------')
                            escolha = input('Digite uma das opções, ou sair: ')

                            if escolha.strip(" ").lower() == 'espadas':
                                print('_____________________________________________')
                                for espada in espadas:
                                    print(f'| {espada[0]} Dano: {espada[1]}   Preço: {espada[2]} |')
                                print('|                                           |')
                                print(f'| Dinheiro: {dinheiro}                            |')
                                print('---------------------------------------------')
                                espada_esc = input('Digite o nome de uma das espadas, ou sair: ').strip(" ")
                                if espada_esc != 'sair':
                                    usuario.compra_equip(espada_esc, espadas)

                            elif escolha.strip(" ").lower() == 'escudos':
                                print('_____________________________________________')
                                for escudo in escudos:
                                    print(f'| {escudo[0]}Dano: {escudo[1]}    Preço: {escudo[2]} |')
                                print('|                                           |')
                                print(f'| Dinheiro: {dinheiro}                            |')
                                print('---------------------------------------------')
                                escudo_esc = input('Digite o nome de um dos escudos, ou sair: ').strip(" ")
                                if escudo_esc != 'sair':
                                    usuario.compra_equip(escudo_esc, escudos)

                            elif escolha.strip(" ").lower() == 'armaduras':
                                print('_____________________________________________')
                                for armadura in armaduras:
                                    print(f'| {armadura[0]}Dano: {armadura[1]}    Preço: {armadura[2]} |')
                                print('|                                           |')
                                print(f'| Dinheiro: {dinheiro}                            |')
                                print('---------------------------------------------')
                                armadura_esc = input('Digite o nome de uma das armaduras, ou sair: ')
                                if armadura_esc != 'sair':
                                    usuario.compra_equip(armadura_esc, armaduras)

                            elif escolha.strip(" ").lower() == 'sair':
                                break

                            else:
                                print('Opção inválida.')
                            sleep(2)
                            clear()

                    elif local.strip(" ").lower() in ['sair', 'sair da vila']:
                        break

                    else:
                        print('Opção inválida')

            elif local.strip(" ").lower() == 'selva':
                inimigo = Inimigo(*choice(selva))
                usuario.batalha(inimigo)

            elif local.strip(" ").lower() == 'sair':
                break

            else:
                print('Local inválido.')
                sleep(2)
                clear()

            # Verificando se o usuário subiu de nível
            if usuario.barra_de_xp >= usuario.levelup:
                # Level
                usuario.level += 1
                stat_level = str(usuario.level).ljust(2)

                # Vida
                usuario.vida += choice(range(1, 4))
                usuario.vida_atual = usuario.vida
                stat_vida = str(usuario.vida).ljust(3)

                # Mana
                usuario.mana += choice(range(1, 4))
                usuario.mana_atual = usuario.mana
                stat_mana = str(usuario.mana).ljust(3)

                # Ataque e defesa
                usuario.ataque += choice(range(3))
                usuario.defesa += choice(range(2))
                stat_ataque = str(usuario.ataque).ljust(2)
                stat_defesa = str(usuario.defesa).ljust(2)

                # Dano mágico
                usuario.dano_magico += choice(range(1, 3))
                stat_dano_magico = str(usuario.dano_magico).ljust(2)

                # Barra de xp e levelup
                usuario.barra_de_xp = 0
                usuario.levelup += choice(range(4, 8))
                stat_levelup = (str(usuario.levelup) + ' XP').ljust(6)

                # Impressão dos dados
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
            clear()
