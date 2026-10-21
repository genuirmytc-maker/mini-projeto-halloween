import pandas as pd
from funcoes import padronizar_categorias, padronizar_canais, validar_datas, validar_numeros, analisar_entregas, relatorio_final
import sys

# Isso faz o print aparecer no terminal E salvar em um arquivo
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("resultados.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger()

caminho = "halloween_vendas.csv"
df = pd.read_csv(caminho, sep=",", encoding="utf-8", dtype=str)

print("--- TRATANDO OS DADOS ---")

df = padronizar_categorias(df)
df = padronizar_canais(df)
df = validar_datas(df)
df = validar_numeros(df)

analisar_entregas(df)
relatorio_final(df)