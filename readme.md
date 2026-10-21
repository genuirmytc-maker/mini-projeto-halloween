# Mini-Projeto: Análise de Vendas Halloween - Festa em Cena

## Descrição do Projeto
Este projeto tem como objetivo organizar, limpar e explorar a base de dados fictícia da rede "Festa em Cena", que vende fantasias de Halloween pelos canais Mercado, Loja física e Web. O programa em Python (Pandas) lê o arquivo CSV, trata os problemas de qualidade (textos inconsistentes, valores nulos e datas inválidas) e gera um relatório de contagens por canal e período.

### Significado de uma linha e quatro colunas
- Linha: Cada linha representa um único pedido de um produto, que pode conter várias unidades.
- pedido_id: Código único de identificação do pedido.
- quantidade: Número de unidades compradas daquele produto. Deve ser um inteiro maior que zero.
- preco_unitario: Valor unitário do produto. Não pode ser negativo.
- status_pedido: Situação atual do pedido (ex: Concluído, Cancelado, Devolvido).

## Regras Adotadas
- Textos: Categorias e canais foram padronizados com .strip() e .lower(), e o Regex (re.sub()) foi usado para remover pontuações como "!!!". Categorias vazias viraram "sem categoria".
- Números: Quantidades inválidas (nulas ou <= 0) e preços inválidos (nulos ou negativos) foram marcados com máscaras lógicas sem inventar dados.
- Datas: As datas válidas foram convertidas para o formato brasileiro (DD/MM/AAAA). Textos como "data_invalida" foram tratados com try/except e marcados, permitindo que o código continue rodando.

## Guia de Execução
1. Certifique-se de ter o Python e a biblioteca Pandas instalados (pip install pandas).
2. Coloque o arquivo halloween_vendas.csv na mesma pasta que os scripts.
3. Execute o arquivo principal com o comando: python main.py.
4. O terminal mostrará as contagens e também gerará um arquivo resultados.txt.

## Reflexão Teórica: ML e Qualidade de Dados
A qualidade dos dados é a base de qualquer projeto de Machine Learning. Dados com nulos, ruídos ou formatações inconsistentes (como os vistos nesta base) levam ao fenômeno "garbage in, garbage out", prejudicando a capacidade do modelo de encontrar padrões reais. No entanto, a limpeza, embora essencial, não é garantia de sucesso. Um modelo ainda pode sofrer de overfitting (decorar os dados de treino) ou underfitting (ser simples demais). Por isso, a representatividade da amostra, a escolha correta do algoritmo e a avaliação rigorosa dos resultados são etapas tão importantes quanto a limpeza dos dados.