import os

# Solicita ao usuário fornecer os nomes das pastas e cria as subpastas como um array
imovel = str(input(f'Digite o nome do imóvel: \n'))
comodo = (input(f'Quais comodos o {imovel} possui? (Coloque separando por espaços!) \n'))
ambiente = comodo.split()
quantidade_comodo = len(ambiente)+1

def criar_pastas(imovel, fotos_ambientes):
    # Verifica se o diretório já existe
    if not os.path.exists(imovel):
        os.makedirs(imovel)
        print(f'Diretório {imovel} criado com sucesso.')

        # Cria as duas subpastas padrão
        subpasta1 = os.path.join(imovel, 'Fotos')
        subpasta2 = os.path.join(imovel, 'Video')

        os.makedirs(subpasta1)
        os.makedirs(subpasta2)

        # Cria as pastas dentro de Subpasta1 com base no array fornecido
        for nome in fotos_ambientes:
            pasta_i = os.path.join(subpasta1, nome)
            os.makedirs(pasta_i)
            print(f'Pasta {pasta_i} criada com sucesso.')

        print(f'Subpastas {subpasta1}, {subpasta2} e pastas dentro de Subpasta1 criadas com sucesso.')

    else:
        print(f'O diretório {imovel} já existe.')

# Especifica o diretório desejado
diretorio_destino = r'/home/rafaelcalacio/Documentos/Teste/' + imovel


# Chama a função para criar as pastas, pastas dentro de Subpasta1 e o arquivo .docx
criar_pastas(diretorio_destino, ambiente)
