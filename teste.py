import pandas as pd
import nltk
from nltk.corpus import stopwords

def remove_stopwords_df(df, coluna_palavras):
    """
    Remove stopwords de um DataFrame de palavras e cria um novo DataFrame 
    com as palavras não stopwords e seus tokens.

    Args:
        df (pd.DataFrame): DataFrame contendo as palavras e seus tokens.
        coluna_palavras (str): Nome da coluna que contém as palavras.

    Returns:
        pd.DataFrame: Um novo DataFrame com as palavras não stopwords e 
                       seus tokens.
    """

    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))

    # Filtra as stopwords do DataFrame
    df_sem_stopwords = df[~df[coluna_palavras].isin(stop_words)]

    return df_sem_stopwords

# Dados de exemplo (ajuste conforme necessário)
dados = {'Palavras': ['the', 'and', 'to', 'a', 'she', 'joys', 'rememberingher', 'childlife', 'happy', 'aftertime'],
        'token': [1319, 696, 638, 537, 442, 1, 1, 1, 1, 1]}
df = pd.DataFrame(dados)

# Remove as stopwords
df_limpo = remove_stopwords_df(df, 'Palavras')

# Exibe o DataFrame resultante
print(df_limpo)