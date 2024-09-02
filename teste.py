from spellchecker import SpellChecker

def corrigir_palavra(palavra):
    # Cria um objeto SpellChecker
    spell = SpellChecker()
    
    # Corrige a palavra
    palavra_corrigida = spell.candidates(palavra)
    if palavra_corrigida:
        # Retorna a palavra mais provável (ou a primeira se houver várias)
        return spell.candidates(palavra).pop()
    else:
        return palavra

# Testa a função com uma palavra errada
palavra_errada = 'gigima'
palavra_corrigida = corrigir_palavra(palavra_errada)
print(f'Palavra original: {palavra_errada}')
print(f'Palavra corrigida: {palavra_corrigida}')