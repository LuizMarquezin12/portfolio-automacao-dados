# Gerador e Validador de Listas de Rateio

## Problema
Processos de rateio podem envolver planilhas extensas, diferentes layouts, bases auxiliares e validações manuais.

## Solução
Pipeline em Python para selecionar uma máscara Excel, normalizar campos, enriquecer registros com bases de referência, validar informações obrigatórias e gerar arquivos separados por distribuidora.

## Fluxo
1. Leitura da máscara e das abas necessárias.
2. Normalização de nomes e identificadores.
3. Cruzamento com bases de referência.
4. Validação de campos obrigatórios.
5. Tratamento de formatos e percentuais.
6. Separação por distribuidora.
7. Geração dos arquivos finais e registro de pendências.

## Tecnologias
Python · pandas · DuckDB · openpyxl · Tkinter

## Observação
Esta é uma descrição sanitizada. Integrações, dados e regras internas não são publicados.
