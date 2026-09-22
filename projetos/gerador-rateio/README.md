# ⚡ Case — Automação e Validação de Rateio

## 🔴 Cenário anterior
A preparação de listas de rateio exigia conferências de dados cadastrais, UCs, documentos, percentuais e informações específicas de cada distribuidora.

## 🟡 Problemas
- layouts e campos diferentes;
- risco de dados incompletos;
- necessidade de De/Para de UCs;
- validação de documentos e percentuais;
- conferências repetitivas antes da geração dos arquivos;
- retrabalho quando inconsistências eram descobertas tarde.

## 🟢 Solução
Pipeline em Python para:
1. ler a máscara de rateio;
2. normalizar colunas e identificadores;
3. enriquecer dados por bases de referência;
4. validar campos obrigatórios conforme o contexto;
5. tratar formatos e percentuais;
6. separar o processamento por distribuidora;
7. gerar os arquivos finais e relatórios de pendências.

## 📊 Resultado
O processo passou a concentrar validação e geração em um fluxo automatizado, reduzindo conferências manuais e antecipando inconsistências.

## 🛠 Stack
Python · pandas · DuckDB · openpyxl · Tkinter
