# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# '------------------------------------------------------------------------------------------------------'

teste = ''' TESTE 1 - TRATAMENTO DE DADOS DINÂMICOS (FÁCIL)
TESTE: Criar uma FUNÇÃO para tratar e converter datas para o formato americano AAAA-MM-DD.
A função deve estar apta a converter qualquer tipo de data exemplificados na lista_datas_outros_formatos
Pode/deve-se utilizar um FOR para realizar o teste da função com os valores contidos na lista_datas_outros_formatos '''


# #CÓDIGO ESTÁTICO - NÃO ALTERAR #
DATAS_PARA_TRATAR = [
    '30/11/2022',
    '01 dez 2022', 
    '25/12/2022', 
    '31 de dezembro de 2022'
]
# #CÓDIGO ESTÁTICO - NÃO ALTERAR #


# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'
def tratarData(data):
    try:
        meses = {
            'jan': '01', 'fev': '02', 'mar': '03', 'abr': '04', 'mai': '05', 'jun': '06',
            'jul': '07', 'ago': '08', 'set': '09', 'out': '10', 'nov': '11', 'dez': '12'
        }

        mesesExtenso = {
            'janeiro': '01', 'fevereiro': '02', 'marco': '03', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06',
            'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
        }

        partesData = data.split()

        if len(partesData) == 1:
            partesData = data.split('/')
            dia, mes, ano = partesData

        elif len(partesData) == 3:
            dia, mes, ano = partesData

            if mes in meses:
                mes = meses[mes.lower()]

            elif mes in mesesExtenso:
                mes = mesesExtenso[mes.lower()]

        elif len(partesData) == 5:
            dia = partesData[0]
            mes = partesData[2]
            ano = partesData[4]   

            if mes in meses:
                mes = meses[mes.lower()]

            elif mes in mesesExtenso:
                mes = mesesExtenso[mes.lower()]

        return  f'{ano}-{mes}-{dia}'
    except:
        return("erro")

for data in DATAS_PARA_TRATAR:
        print(tratarData(data))

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 1---------------------------------------------------'
# EXEMPLO: 30/11/2022 DEVE SE TORNAR 2022-11-30