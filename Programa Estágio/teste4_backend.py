# Recomendações:
# - Não alterar os trechos de código que estejam entre os comentários # NÃO ALTERAR #
# - Desenvolver o código entre os trechos de comentário # DESENVOLVIMENTO - TESTE #
# - É recomendado realizar a verificação/teste/execução do código várias vezes, para garantir o funcionamento
# - TODOS OS PROCESSOS SÃO DE ACESSO PÚBLICO E TIVERAM AUTORIZAÇÃO DE SUAS PARTES
# '------------------------------------------------------------------------------------------------------'

teste = ''' AUTOMAÇÃO SELENIUM - Consulta Pública ESAJ-SP (DIFÍCIL - BACKEND)
TESTE: Desenvolver uma automação selenium para realizar consultas públicas no portal ESAJ-SP
Cada consulta deve montar um dicionário final

Passo a passo da automação:
1. abrir o site
2. clicar no botão rádio Outros
3. Digitar o nº do processo listado abaixo na caixa input
4. Clicar no botão Consultar
5. Verificar se o processo foi ou não encontrado (há mensagem de erro)
6. Caso tenha sido encontrado, coletar as seguintes informações: (para localizar basta pesquisar por esse texto no site)
    - numero_processo
    - classe
    - assunto
    - foro
    - vara
    - Reqte 
    - Reqdo
7. Organizar os dados acima em um dicionário e printá-lo
'''

# # CÓDIGO ESTÁTICO - NÃO ALTERAR #
URL_PORTAL = 'https://esaj.tjsp.jus.br/cpopg/open.do'
LISTA_PROCESSOS = [
    '0000622-07.2022.8.26.0003',
    '1035157-25.2021.8.26.0602',
    '1093123-72.2021.8.26.0529',
    '1011882-72.2021.8.26.0529',
    '0806733-22.2016.8.15.0251',
    '1005551-62.2021.8.26.0048',
    '1000891-61.2021.8.26.0424'
]
# # CÓDIGO ESTÁTICO - NÃO ALTERAR #

# '---------------------------------------------------DESENVOLVIMENTO - TESTE 7---------------------------------------------------'
from selenium import webdriver
from selenium.webdriver.common.by import By

def consultar(processo):
    browser = webdriver.Chrome()
    browser.get(URL_PORTAL)
    browser.find_element(By.ID, 'radioNumeroAntigo').click()
    browser.find_element(By.ID, 'nuProcessoAntigoFormatado').send_keys(processo)
    browser.find_element(By.ID, 'botaoConsultarProcessos').click()
    try:
        if browser.find_element(By.ID, 'mensagemRetorno').is_displayed():
            return ("Erro ao tentar buscar o processo")
    except Exception:
        numeroProcesso = browser.find_element(By.ID, 'numeroProcesso').text
        classe = browser.find_element(By.ID, 'classeProcesso').text
        assunto = browser.find_element(By.ID, 'assuntoProcesso').text
        foro = browser.find_element(By.ID, 'foroProcesso').text
        vara = browser.find_element(By.ID, 'varaProcesso').text
        reqte = browser.find_element(By.XPATH, '//*[@id="tablePartesPrincipais"]/tbody/tr[1]/td[2]').text
        reqdo = browser.find_element(By.XPATH, '//*[@id="tablePartesPrincipais"]/tbody/tr[2]/td[2]').text

        dadosProcesso = {
            "numeroProcesso": numeroProcesso,
            "classe": classe,
            "assunto": assunto,
            "foro": foro,
            "vara": vara,
            "reqte": reqte,
            "reqdo": reqdo

        }
        return dadosProcesso
        
for processo in LISTA_PROCESSOS:
    print(consultar(processo)) 
# '---------------------------------------------------DESENVOLVIMENTO - TESTE 7---------------------------------------------------'
