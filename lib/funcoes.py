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
    clear()

    if jogo.strip(" ").lower() == 'novo jogo':
        print('Novo jogo iniciado!')
        menu_opcoes()

    elif jogo.strip(" ").lower() == 'carregar jogo':
        try:
            usuario.save('carregar')
            print('Jogo carregado com sucesso!')
            menu_opcoes()

        except FileNotFoundError:
            print('Arquivo de save não encontrado.')

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
        viajar()

    elif opcao.strip(" ").lower() == 'descansar':
        usuario.vida_atual = usuario.vida
        usuario.mana_atual = usuario.mana
        print('Você monta uma tenda para descansar um pouco...')
        print('Descansando, você recupera vida e mana!')

    elif opcao.strip(" ").lower() == 'status':
        usuario.status()

    elif opcao.strip(" ").lower() == 'equips':
        usuario.equips()

    elif opcao.strip(" ").lower() == 'salvar':
        usuario.save('salvar')

    elif opcao.strip(" ").lower() in ['inventario', 'inventário']:
        usuario.invent()

    elif opcao.strip(" ").lower() == 'sair':
        print('Programa finalizado.')
        exit()

    else:
        print('Opção inválida') 

    sleep(2)
    clear()
    menu_opcoes()


def viajar():
    """Função para viajar"""

    # Dicionário de todos lugares com inimigos
    lugares_inimigos = {'floresta': floresta, 'caverna': caverna, 'selva': selva}

    print('Locais disponíveis')
    print('________________________')
    print('|  Floresta   Caverna  |')
    print('|  Vila       Selva    |')
    print('------------------------')
    local = input('Digite uma opção, ou sair para voltar ao menu de opções: ').strip(" ").lower()

    if local in lugares_inimigos.keys():
        inimigo = Inimigo(*choice(lugares_inimigos.get(local)))
        usuario.batalha(inimigo)

    elif local == 'vila':
        vila()

    elif local == 'sair':
        menu_opcoes()

    else:
        print('Local inválido.')
        sleep(2)

    # Verificando se o usuário subiu de nível
    if usuario.barra_de_xp >= usuario.levelup:
        usuario.lvlup()
    clear()
    viajar()


def vila():
    clear()
    print('Ao entrar na vila, você vê diversas tavernas e lojas')
    print('________________________')
    print('| Apotecário  Ferreiro |')
    print('------------------------')
    local = input('Digite uma das opções, ou sair: ').strip(" ").lower()
    clear()

    if local == 'apotecario' or local == 'apotecário':
        apotecario()

    elif local == 'ferreiro':
        ferreiro()     

    elif local == 'sair':
        viajar()

    else:
        print('Opção inválida')
        sleep(2)
    vila()


def apotecario():
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
        vila()

    else:
        print('Opção inválida.')
    sleep(2)
    clear()
    apotecario()


def ferreiro():
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
            print(f'| {espada[0].ljust(20)} Dano: {espada[1]}   Preço: {espada[2].ljust(3)} |')
        print('|                                           |')
        print(f'| Dinheiro: {dinheiro}                            |')
        print('---------------------------------------------')
        espada_esc = input('Digite o nome de uma das espadas: ').strip(" ")
        usuario.compra_equip(espada_esc, espadas)

    elif escolha.strip(" ").lower() == 'escudos':
        print('_____________________________________________')
        for escudo in escudos:
            print(f'| {escudo[0].ljust(20)}Dano: {escudo[1]}    Preço: {escudo[2].ljust(3)} |')
        print('|                                           |')
        print(f'| Dinheiro: {dinheiro}                            |')
        print('---------------------------------------------')
        escudo_esc = input('Digite o nome de um dos escudos: ').strip(" ")
        usuario.compra_equip(escudo_esc, escudos)

    elif escolha.strip(" ").lower() == 'armaduras':
        print('_____________________________________________')
        for armadura in armaduras:
            print(f'| {armadura[0].ljust(20)}Dano: {armadura[1]}    Preço: {armadura[2].ljust(3)} |')
        print('|                                           |')
        print(f'| Dinheiro: {dinheiro}                            |')
        print('---------------------------------------------')
        armadura_esc = input('Digite o nome de uma das armaduras: ')
        usuario.compra_equip(armadura_esc, armaduras)

    elif escolha.strip(" ").lower() == 'sair':
        vila()

    else:
        print('Opção inválida.')
    sleep(2)
    clear()
    ferreiro()
