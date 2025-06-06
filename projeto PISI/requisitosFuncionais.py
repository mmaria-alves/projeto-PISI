import random
import os
ARQUIVO_TXT1 = "shoutbox.txt"
ARQUIVO_TXT2 = "avaliações.txt"
ARQUIVO_TXT3 = "novidades.txt"

# avaliações
def carregar_avaliacoes():
    avaliacoes = []
    if os.path.exists(ARQUIVO_TXT2):
        with open(ARQUIVO_TXT2, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                if len(dados) == 4:
                    album, artista, nota, comentario = dados
                    avaliacoes.append({
                        'album': album,
                        'artista': artista,
                        'nota': float(nota),  
                        'comentario': comentario
                    })
    return avaliacoes
    
def salvar_avaliacoes(avaliacoes):
    with open(ARQUIVO_TXT2, 'w') as arquivo:
        for avaliacao in avaliacoes:
            linha = f"{avaliacao['album']}|{avaliacao['artista']}|{avaliacao['nota']}|{avaliacao['comentario']}\n"
            arquivo.write(linha)

def carregaravaliacoes():
    avaliacoesnew = []
    if os.path.exists(ARQUIVO_TXT3):
        with open(ARQUIVO_TXT3, 'r') as arquivo:
            for linha in arquivo:
                dadosnew = linha.strip().split('|')
                if len(dadosnew) == 4:
                    album, artista, nota, comentario = dadosnew
                    avaliacoesnew.append({
                        'album': album,
                        'artista': artista,
                        'nota': float(nota),  
                        'comentario': comentario
                    })
    return avaliacoesnew
    
def salvaravaliacoes(avaliacoesnew):
    with open(ARQUIVO_TXT3, 'w') as arquivo:
        for avaliacaonew in avaliacoesnew:
            linha = f"{avaliacaonew['album']}|{avaliacaonew['artista']}|{avaliacaonew['nota']}|{avaliacaonew['comentario']}\n"
            arquivo.write(linha)

# shoutbox
def carregar_shouts():
    shouts = []
    if os.path.exists(ARQUIVO_TXT1):
        with open(ARQUIVO_TXT1, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if '|' in linha:
                    partes = linha.split('|')
                    if len(partes) == 2:
                        album, artista = partes
                        shouts.append({'album': album, 'artista': artista})
                    else:
                        print(f"Linha inválida (muitos '|'): {linha}")
                elif linha:
                    print(f"Linha inválida (sem '|'): {linha}")
    return shouts

def salvar_shouts(shouts):
    with open(ARQUIVO_TXT1, 'w') as arquivo:
        for shout in shouts:
            linha = f"{shout['album']}|{shout['artista']}\n"
            arquivo.write(linha)
            
# menu: funcionalidades
def menu_funcionalidades():
    while True:
        print("\n🎵 Sons da terra 🎵")
        print("1. avaliar")
        print("2. o que as pessoas estão ouvindo")
        print("3. shout-box")
        print("4. novidades")
        print("5. sair")

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == '1':
            avaliar_album()
        elif opcao == '2':
            mostrar()
        elif opcao == '3':
            shout_box()
        elif opcao == '4':
            avaliaralbum()
        elif opcao == '5':
            print("Até a próxima!")
            break
        else:
            print("Tente novamente.")

# Lista de álbuns disponíveis
albuns_disponiveis = [
    {"nome": "Mundhana (2022)", "artista": "Mun-há"},
    {"nome": "Megalomania (2024)", "artista": "Uana"},
    {"nome": "Tanto pra dizer (2024)", "artista": "Mirela Hazin"},
    {"nome": "Coisas naturais (2025)", "artista": "Marina Sena"},
    {"nome": "Âmago (2024)", "artista": "Zendo"},
    {"nome": "Gambiarra chic pt.2 (2025)", "artista": "Irmãs de pau"},
    {"nome": "Grimestar (2024)", "artista": "Tremsete"},
    {"nome": "Jogo de Cintura (2024)", "artista": "Bell Puã"},
    {"nome": "Casa Coração (2025)", "artista": "Joyce Alane"},
    {"nome": "Bacuri (2024)", "artista": "Boogarins"},
    {"nome": "Abaixo de zero: Hello Hell (2019)", "artista": "Black alien"},
    {"nome": "KM2 (2025)", "artista": "Ebony"},
    {"nome": "Letrux como Mulher Girafa (2023)", "artista": "Letrux"},
    {"nome": "SIM SIM SIM (2022)", "artista": "Bala Desejo"},
    {"nome": "Me Chama de Gato Que Eu Sou Sua (2023)", "artista": "Ana Frango Elétrico"},
    {"nome": "o fim é um começo (2024)", "artista": "a terra vai se tornar um planeta inabitável"},
    {"nome": "MAU (2023)", "artista": "Jaloo"},
    {"nome": "Antiasfixiante (2024)", "artista": "Kinoa"},
    {"nome": "Quebra Asa, vol.1 (2023)", "artista": "Fernando motta"},
    {"nome": "Muganga (2023)", "artista": "IDLIBRA"}
    
]

def avaliar_album():
    avaliacoes = carregar_avaliacoes()
    while True:
        print("\nÁlbuns:")
        for i, album1 in enumerate(albuns_disponiveis):
            print(f"{i + 1}. {album1['nome']} - {album1['artista']}")
        
        escolha_input = input('Escolha o número do álbum que deseja avaliar (ou digite "sair" para voltar): ')
        if escolha_input.lower() == "sair":
            return
        
        if not escolha_input.isdigit() or not (1 <= int(escolha_input) <= len(albuns_disponiveis)):
            print("Número inválido. Tente novamente.")
            continue

        escolha = int(escolha_input) - 1

        nota_input = input('Dê uma nota de 0 a 5 (ou digite "sair" para voltar): ')
        if nota_input.lower() == "sair":
            return

        try:
            nota = float(nota_input)
            if nota < 0 or nota > 5:
                print("Nota fora do intervalo permitido. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida para nota. Use um número entre 0 e 5.")
            continue

        comentario = input("Deixe um comentário sobre o álbum: ")

        avaliacao = {
            "album": albuns_disponiveis[escolha]["nome"],
            "artista": albuns_disponiveis[escolha]["artista"],
            "nota": nota,
            "comentario": comentario
        }

        avaliacoes.append(avaliacao)
        salvar_avaliacoes(avaliacoes)
        print("Avaliação registrada com sucesso!\n")
        return

def mostrar():
    avaliacoes = carregar_avaliacoes()
    print("\nO que estão ouvindo agora:")

    if not avaliacoes:
        sugestoes = random.sample(albuns_disponiveis, k=min(3, len(albuns_disponiveis)))
        for album in sugestoes:
            print(f"- {album['nome']} by {album['artista']}")
    else:
        escolhas = random.sample(avaliacoes, k=min(3, len(avaliacoes)))
        for item in escolhas:
            print(f"- {item['album']} by {item['artista']} ({item['nota']}/5): \"{item['comentario']}\"")


def shout_box():
    shouts = carregar_shouts()
    print("\nQual álbum você gostaria de avaliar mas não está disponível?")
    sugestao = input("\nNome do álbum que você quer ver na plataforma: ")
    artista = input("\nNome do artista/banda: ")

    shout = {"album": sugestao, "artista": artista}
    shouts.append(shout)
    salvar_shouts(shouts)
    print("Sugestão registrada! Obrigado por contribuir\n")



# novidades:
novidades = [
        {"nome": "Movimento algum (NOVO)", "artista": "Fernando Motta"},
        {"nome": "Imagina (single)", "artista": "Barbarize feat. Oreia"},
        {"nome": "Tropical do Brasil (single)", "artista": "Uana feat. Leoa"},
        {"nome": "Casa Coração (2025)", "artista": "Joyce Alane"},
        {"nome": "Coisas naturais (2025)", "artista": "Marina Sena"},
        {"nome": "Gambiarra chic pt.2 (2025)", "artista": "Irmãs de Pau"},
        {"nome": "Dvd (single)", "artista": "Mirela Hazin"},
        {"nome": "KM2 (2025)", "artista": "Ebony"}
]


def avaliaralbum():
    avaliacoesnew = carregaravaliacoes()
    while True:
        print("\nÁlbuns lançados recentemente:")
        for i, album in enumerate(novidades):
            print(f"{i + 1}. {album['nome']} - {album['artista']}")
        
        escolha_input = input('Escolha o número do álbum que deseja avaliar (ou digite "sair" para voltar): ')
        if escolha_input.lower() == "sair":
            return
        
        if not escolha_input.isdigit() or not (1 <= int(escolha_input) <= len(novidades)):
            print("Número inválido. Tente novamente.")
            continue

        escolha = int(escolha_input) - 1

        nota_input = input('Dê uma nota de 0 a 5 (ou digite "sair" para voltar): ')
        if nota_input.lower() == "sair":
            return

        try:
            nota = float(nota_input)
            if nota < 0 or nota > 5:
                print("Nota fora do intervalo permitido. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida para nota. Use um número entre 0 e 5.")
            continue

        comentario = input("Deixe um comentário sobre o álbum: ")

        avaliacaonew = {
            "album": novidades[escolha]["nome"],
            "artista": novidades[escolha]["artista"],
            "nota": nota,
            "comentario": comentario
        }

        avaliacoesnew.append(avaliacaonew)
        salvaravaliacoes(avaliacoesnew)
        print("Avaliação registrada com sucesso!\n")
        return
    
