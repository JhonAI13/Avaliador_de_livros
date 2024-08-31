import pdfplumber
from pprint import pprint
import pandas as pd

def pontuacao():
    """Retorna uma string com todos os caracteres de pontuação."""
    return r"""!"#$%&''()*+,‘-./:;<=>?@[\]^_`{|}~"""

def ler_pdf_sem_cabecalho_rodape(caminho_arquivo, margem_superior=50, margem_inferior=50):
    """
    Lê um PDF linha a linha, ignorando o cabeçalho e o rodapé.

    :param caminho_arquivo: Caminho do arquivo PDF.
    :param margem_superior: Tamanho da margem para ignorar o cabeçalho (em pixels).
    :param margem_inferior: Tamanho da margem para ignorar o rodapé (em pixels).
    """
    texto = []
    with pdfplumber.open(caminho_arquivo) as pdf:
        for pagina in pdf.pages:
            largura, altura = pagina.width, pagina.height
            
            # Define a caixa de corte, ignorando cabeçalho e rodapé
            area_util = (0, margem_superior, largura, altura - margem_inferior)
            
            # Recorta a página para excluir cabeçalho e rodapé
            texto_recortado = pagina.within_bbox(area_util).extract_text()
            
            # Separa o texto recortado em linhas
            linhas = texto_recortado.split('\n')
            texto.append(linhas)
    return texto

def remover_pontuacao(text):
    """Remove pontuações de um texto e retorna uma string sem pontuação.

    Args:
        text (str): O texto a ser processado.

    Returns:
        str: O texto sem pontuação.
    """
    caracteres_sem_pontuacao = []
    for char in text:
        if char not in pontuacao():
            caracteres_sem_pontuacao.append(char)
        elif char in "—":
            caracteres_sem_pontuacao.append(" ")
    
    texto_sem_pontuacao = "".join(caracteres_sem_pontuacao)
    return texto_sem_pontuacao.split()

def listlist_to_list(lista):
    intemeidario = []
    for paginas in lista:
        for linhas in paginas:
            for frases in linhas:
                intemeidario.append(frases)
    return intemeidario

def frequencia_palavras(text_processado):
    """Calcula a frequência de cada palavra em um texto.

    Args:
        text_processado (list): A lista de palavras processadas.

    Returns:
        dict: Um dicionário com a frequência de cada palavra.
    """
    freq_palavras = {}
    for palavras in text_processado:
        if palavras not in freq_palavras:
            freq_palavras[palavras] = 1
        else:
            freq_palavras[palavras] += 1
    return freq_palavras

def sorted(dicionario):
    # Converter o dicionário em um DataFrame
    df = pd.DataFrame(list(dicionario.items()), columns=['Palavras', 'token'])
    # Ordenar o DataFrame pelos valores
    df_ordenado = df.sort_values(by='token', ascending=False)
    
    return df_ordenado

def __main__(caminho_pdf):
    lista_paginas = ler_pdf_sem_cabecalho_rodape(caminho_pdf)
    lista_de_linhas = listlist_to_list(lista_paginas)

    lista_paginas_sem_pontuação = remover_pontuacao(lista_de_linhas)
    palavras_tokenizadas = frequencia_palavras(lista_paginas_sem_pontuação)

    lista_ordenada = sorted(palavras_tokenizadas)
    lista_ordenada.to_excel(r'C:\Users\jonat\Documents\GitHub\Avaliador_de_livros\palavras.xlsx', index=False) 
    pprint(lista_ordenada)

caminho_pdf = r'C:\Users\jonat\Documents\GitHub\Avaliador_de_livros\Programa\Textos\Alice’sAdventuresinWonderland.pdf'
__main__(caminho_pdf)
