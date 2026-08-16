# Titanic Data Pipeline

Pipeline de limpeza e preparação de dados do dataset Titanic, construído durante estudos para vaga de estágio em Ciência de Dados/IA.

## O que faz
- Carrega o dataset do Titanic
- Trata valores ausentes (idade, embarque, remove coluna deck)
- Converte tipos de dados para formatos otimizados

## Como rodar
\`\`\`python
from src.limpeza import carregar_e_limpar
df = carregar_e_limpar()
\`\`\`