from pathlib import Path
from pprint import pprint
from os import walk

t = Path()
caminho_projeto = Path() / 'Programa' / 'Textos'
pprint(t.absolute())
for caminho, subpasta, arquivo in walk(caminho_projeto):
    a = arquivo

caminho = caminho_projeto / str(a[0])
print(caminho)