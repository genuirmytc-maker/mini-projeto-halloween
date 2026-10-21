import pandas as pd
import re
from datetime import datetime

def padronizar_categorias(df):
    def limpar_texto(texto):
        if pd.isna(texto):
            return "sem categoria"
        texto_limpo = texto.strip().lower()
        texto_limpo = re.sub(r'[^a-z\s]', '', texto_limpo)
        texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
        if texto_limpo == "":
            return "sem categoria"
        return texto_limpo
    df['categoria_limpa'] = df['categoria'].apply(limpar_texto)
    return df

def padronizar_canais(df):
    canais_alterados = 0
    canais_vazios = 0
    def limpar_canal(canal):
        nonlocal canais_alterados, canais_vazios
        if pd.isna(canal) or str(canal).strip() == "":
            canais_vazios += 1
            return "Sem canal"
        canal_original = canal
        canal_limpo = str(canal).strip().lower()
        if "mercado" in canal_limpo:
            canal_final = "Mercado"
        elif "loja" in canal_limpo: 
            canal_final = "Loja física"
        elif "web" in canal_limpo:
            canal_final = "Web"
        else:
            canal_final = "Outros"
        if canal_original != canal_final:
            canais_alterados += 1
        return canal_final
    print("\n--- PADRONIZAÇÃO DE CANAIS (Sprint 2) ---")
    df['canal_venda_limpo'] = df['canal_venda'].apply(limpar_canal)
    print(f"Canais vazios encontrados: {canais_vazios}")
    print(f"Canais não vazios que precisaram de correção: {canais_alterados}")
    return df

def validar_datas(df):
    datas_formatadas = []
    for data_str in df['data_venda']:
        try:
            data_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
            datas_formatadas.append(data_obj.strftime("%d/%m/%Y"))
        except (ValueError, TypeError):
            datas_formatadas.append("Data Inválida")
    df['data_venda_br'] = datas_formatadas
    return df

def validar_numeros(df):
    vazias = df['categoria'].isna().sum()
    print(f"\nCategorias vazias preenchidas (Sprint 3): {vazias}")
    df['quantidade_num'] = pd.to_numeric(df['quantidade'], errors='coerce')
    df['preco_num'] = pd.to_numeric(df['preco_unitario'], errors='coerce')
    erro_quantidade = (df['quantidade_num'].isna()) | (df['quantidade_num'] <= 0)
    erro_preco = (df['preco_num'].isna()) | (df['preco_num'] < 0)
    print(f"Problemas na quantidade: {erro_quantidade.sum()}")
    print(f"Problemas no preço: {erro_preco.sum()}")
    total_afetados = (erro_quantidade | erro_preco).sum()
    print(f"Total de pedidos afetados por problemas numéricos: {total_afetados}")
    return df

def analisar_entregas(df):
    sem_data = df['data_entrega'].isna()
    cancelados = df['status_pedido'].str.lower() == 'cancelado'
    sem_data_cancelados = (sem_data & cancelados).sum()
    sem_data_outros = (sem_data & ~cancelados).sum()
    print(f"\nPedidos sem data de entrega e Cancelados (Sprint 4): {sem_data_cancelados}")
    print(f"Pedidos sem data de entrega com OUTROS status (Hipótese Falsa): {sem_data_outros}")
    if sem_data_outros > 0:
        print("Até 3 exemplos de pedidos sem data de entrega com outros status:")
        exemplos = df[sem_data & ~cancelados][['pedido_id', 'status_pedido']].head(3)
        print(exemplos)

def relatorio_final(df):
    print("\n--- RELATÓRIO FINAL (Sprint 5) ---")
    total_cancelados = (df['status_pedido'].str.lower() == 'cancelado').sum()
    print(f"Total de pedidos cancelados na base: {total_cancelados}")
    print("\nPedidos por canal (incluindo todos os status):")
    print(df['canal_venda_limpo'].value_counts())
    print("\nPedidos por Ano-Mês (apenas datas válidas):")
    df['ano_mes'] = pd.to_datetime(df['data_venda'], errors='coerce').dt.strftime('%Y-%m')
    print(df['ano_mes'].value_counts().sort_index())