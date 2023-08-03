
# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 2 - VERIFICAÇÃO DE ARQUIVOS (FÁCIL)
TESTE: Criar uma FUNÇÃO que lista os arquivos de um diretório e verifica se todos se algum ultrapassa o limite de 3 MB
Se algum arquivo ultrapassar o limite de 3MB retornar False, se todos os arquivos estiverem abaixo do limite retornar True
'''

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 2---------------------------------------------------'
import os

local = r"C:\Users\gabry\Downloads\programa-estagio"

def verificaArquivo(local):
    try:
        for arquivo in os.listdir(local):
            localArquivo = os.path.join(local, arquivo)
            if (os.path.exists(localArquivo)):
                tamanhoArquivo = os.path.getsize(localArquivo) / (1024 * 1024)
                if tamanhoArquivo > 3:
                    print(f'{tamanhoArquivo:.2f}')
                    return False  
            else:
                print('não foi possivel encontrar o arquivo')
        print(tamanhoArquivo)
        return True
    except:
        return("erro")

print(verificaArquivo(local))
# '---------------------------------------------------DESENVOLVIMENTO - TESTE 2---------------------------------------------------'
