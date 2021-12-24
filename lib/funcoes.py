from random import choice
from time import sleep

from .itens import espadas, escudos, armaduras, pocao_de_vida, pocao_de_mana
from .usuario import usuario, clear
from .inimigos import floresta, caverna, selva, Inimigo


def menu_principal():
    """Função para chamar o menu principal"""
    print('Menu principal')
    print('_________________')
    print('| Novo jogo     |')
    print('| Carregar jogo |')
    print('-----------------')
    opcao = input('Digite uma das opções: ').strip(" ").lower()
    clear()

    if opcao == 'novo jogo':
        print('Novo jogo iniciado!')
        menu_opcoes()

    elif opcao == 'carregar jogo':
        try:
            usuario.load()
            menu_opcoes()

        except FileNotFoundError:
            print('Arquivo de save não encontrado.')

    else:
        print('Opção inválida.')

    sleep(2)
    menu_principal()


def menu_opcoes():
    """Função para chamar o menu de opções"""
    metodos_usuario = {
        'status': usuario.status, 
        'equips': usuario.equips, 
        'inventario': usuario.invent,
        'inventário': usuario.invent, 
        'salvar': usuario.save
    }

    print('Menu de opções')
    print('________________________')
    print('|  Viajar   Descansar  |')
    print('|  Status   Equips     |')
    print('|  Salvar   Inventário |')
    print('|  Sair                |')
    print('------------------------')
    opcao = input('Digite uma das opções do menu: ').strip(" ").lower()
    clear()

    if opcao == 'viajar':
        viajar()

    elif opcao == 'descansar':
        usuario.vida_atual, usuario.mana_atual = usuario.vida, usuario.mana
        print('Você monta uma tenda para descansar um pouco...')
        print('Descansando, você recupera sua vida e mana!')

    elif opcao in metodos_usuario:
        metodos_usuario.get(opcao)()

    elif opcao == 'sair':
        print('Programa finalizado.')
        exit()

    else:
        print('Opção inválida')

    sleep(2)
    menu_opcoes()


def viajar():
    """Função para viajar para alguns lugares"""
    # Dicionário de todos lugares com inimigos
    lugares_inimigos = {
        'floresta': floresta, 
        'caverna': caverna, 
        'selva': selva
    }

    print('Locais disponíveis')
    print('________________________')
    print('|  Floresta   Caverna  |')
    print('|  Vila       Selva    |')
    print('------------------------')
    local = input('Digite uma opção, ou sair para voltar ao menu de opções: ').strip(" ").lower()

    if local in lugares_inimigos:
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
    print('Ao entrar na vila, você vê diversas tavernas e lojas')
    print('________________________')
    print('| Apotecário  Ferreiro |')
    print('------------------------')
    local = input('Digite uma das opções, ou sair: ').strip(" ").lower()

    if local == 'apotecario' or local == 'apotecário':
        apotecario()

    elif local == 'ferreiro':
        ferreiro()     

    elif local == 'sair':
        viajar()

    else:
        print('Opção inválida')
        sleep(2)

    clear()
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
    tipos_equipamentos = {
        'espadas': espadas, 
        'escudos': escudos, 
        'armaduras': armaduras
    }

    dinheiro = str(usuario.dinheiro).ljust(4)
    print('Ferreiro')
    print('_____________')
    print('| Espadas   |')
    print('| Escudos   |')
    print('| Armaduras |')
    print('-------------')
    escolha = input('Digite uma das opções, ou sair: ').strip(" ").lower()

    if escolha in tipos_equipamentos:
        equipamentos = tipos_equipamentos.get(escolha)
        print('_____________________________________________')
        for equipamento in equipamentos:
            print(f'| {equipamento[0].ljust(20)} Dano: {equipamento[1]}   Preço: {equipamento[2].ljust(3)} |')
        print('|                                           |')
        print(f'| Dinheiro: {dinheiro}                            |')
        print('---------------------------------------------')
        equip_esc = input(f'Digite o nome de um(a) dos(as) {escolha}: ').strip(" ").lower()
        usuario.compra_equip(equip_esc, equipamentos)

    elif escolha == 'sair':
        vila()

    else:
        print('Opção inválida.')

    sleep(2)
    clear()
    ferreiro()
