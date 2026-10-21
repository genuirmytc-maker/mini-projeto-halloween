# Relatório de Análise - Festa em Cena

## 1. Visão Geral e Qualidade dos Dados
A base analisada contém 1.500 registros de pedidos. Durante o processo de validação, identificamos que a qualidade dos dados é um desafio significativo. Foram encontradas 18 categorias vazias que precisaram ser preenchidas com "sem categoria". Além disso, 45 registros de canais de venda apresentavam inconsistências de escrita (espaços, letras maiúsculas/minúsculas) e precisaram ser corrigidos e padronizados para "Mercado", "Loja física" e "Web". 

Na validação numérica, encontramos problemas em 19 pedidos: 7 apresentaram quantidade inválida (nulas ou menores/iguais a zero) e 12 apresentaram preço unitário inválido. É importante notar que 1.500 é o total de pedidos, mas nem todos são vendas concluídas.

## 2. Regra de Negócio: Entregas e Cancelamentos
Investigamos a hipótese de que todos os pedidos sem data de entrega seriam cancelados. A hipótese foi comprovada como falsa. Identificamos 109 pedidos sem data de entrega que estão devidamente cancelados. No entanto, 34 pedidos não possuem data de entrega e apresentam outros status, como "Concluído" (exemplos: pedidos 1170, 990 e 740). Isso indica uma possível falha no registro da data de entrega para pedidos que foram finalizados.

No total, a base possui 109 pedidos cancelados.

## 3. Descobertas por Canal e Período
**Por Canal de Venda:**
A contagem de pedidos registrados (incluindo todos os status) mostra que o canal Web é o mais movimentado, com 666 pedidos, seguido pela Loja física (551) e Mercado (283). 
Interpretação: O e-commerce é o principal ponto de entrada de pedidos. 
Limitação: Esta contagem representa o volume de pedidos registrados, não a receita gerada, pois não filtramos cancelamentos.

**Por Período (Ano-Mês):**
Agrupando os dados com datas válidas, observamos um claro padrão sazonal. O pico de pedidos ocorre no mês de outubro em ambos os anos: 393 pedidos em 2024-10 e 410 em 2025-10. Os meses de agosto e setembro apresentam volumes menores, crescendo gradativamente até o Halloween. 
Interpretação: A demanda é fortemente concentrada nas semanas que antecedem o dia 31 de outubro. 
Limitação: A análise mede apenas o volume transacional, sem considerar o valor monetário das vendas.