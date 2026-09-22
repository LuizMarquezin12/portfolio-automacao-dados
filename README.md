# 👨‍💻 Luiz Henrique Garcia | Automação, Dados & Melhoria de Processos

![Python](https://img.shields.io/badge/Python-Automação-3776AB?logo=python&logoColor=white)
![RPA](https://img.shields.io/badge/RPA-Processos-5C2D91)
![Power BI](https://img.shields.io/badge/Power%20BI-Indicadores-F2C811?logo=powerbi&logoColor=black)
![Data](https://img.shields.io/badge/Data-pandas-150458?logo=pandas)
![Portfolio](https://img.shields.io/badge/Portfólio-Cases-success)

Portfólio técnico com **cases demonstrativos inspirados em desafios reais de operação**, mostrando como automação, dados e melhoria de processos podem reduzir trabalho manual, acelerar rotinas e aumentar a visibilidade operacional.

> 🔒 **Confidencialidade:** os códigos e exemplos deste repositório foram recriados e sanitizados. Não há credenciais, dados de clientes, endpoints privados, código proprietário ou regras internas sensíveis.

## 📊 Impacto

- Automações com capacidade observada de **300–400 faturas/dia** em determinados fluxos.
- Caso de alta volumetria com aproximadamente **1.150 consultas processadas em 2h10**.
- Redução relevante do tempo operacional por meio de processamento automatizado.
- A automação interna contribuiu para **redução de custo com captura terceirizada**, permitindo descontinuidade de um fornecedor externo desse processo.
- Consolidação de dezenas de milhares de registros para acompanhamento de **capturadas, faltantes e pendências**.
- Padronização de processos de **rateio, validação, demonstrativos e tratamento de dados**.

> Os valores financeiros do ganho não são publicados por confidencialidade.

## 🧭 Jornada dos projetos

### 1. 🤖 Automação de captura de faturas
O desafio inicial era executar consultas repetitivas em diferentes portais de distribuidoras, baixar documentos e controlar o que havia sido ou não capturado.

A solução evoluiu para robôs com filas, validações, retentativas, logs, recuperação de falhas e organização de documentos. Com mudanças nos portais e adoção de mecanismos adicionais de autenticação e proteção de sessão, a arquitetura precisou ser revista para separar etapas de autenticação/autorização das rotinas automatizadas posteriores.

**Resultado:** maior velocidade de processamento, redução do trabalho manual e menor dependência de captura terceirizada.

### 2. ⚡ Rateio — validação e geração
O rateio exigia conferência de UCs, documentos, percentuais, dados cadastrais e regras diferentes por distribuidora.

Foi estruturado um pipeline para normalização, cruzamento com bases de referência, validação de obrigatórios, tratamento de percentuais e geração de arquivos por distribuidora.

**Resultado:** redução de conferências manuais e de retrabalho antes do processamento.

### 3. 📈 BI de Captura
Com diferentes robôs, competências e origens de captura, tornou-se necessário enxergar o processo de ponta a ponta.

Foi criada uma base consolidada para Power BI com acompanhamento por competência e distribuidora, distinguindo registros **capturados, faltantes e pendentes**, incluindo diferentes origens de atendimento.

**Resultado:** visão operacional centralizada e identificação mais rápida dos gaps de captura.

### 4. 📑 Demonstrativos
Demonstrativos com formatos e identificadores diferentes precisavam ser conciliados com a base faturável.

A automação normaliza UCs/contratos, cruza as fontes e incorpora os registros encontrados ao acompanhamento operacional.

### 5. 🧹 Qualidade de Dados e Excel
Diversas rotinas auxiliares foram automatizadas: normalização de colunas, deduplicação, De/Para de UCs, tratamento de CSV/XLSX, validações, geração de arquivos, PDFs, livros, índices e controles operacionais.

## 📂 Cases

| Case | Problema resolvido | Stack |
|---|---|---|
| [Captura de Faturas](projetos/captura-faturas/) | Alto volume, falhas, mudanças de fluxo e acompanhamento | Python, Selenium, Playwright, PyAutoGUI, APIs |
| [Gerador de Rateio](projetos/gerador-rateio/) | Validação e geração por distribuidora | Python, pandas, DuckDB, openpyxl |
| [BI de Captura](projetos/bi-captura/) | Visibilidade de capturadas x faltantes x pendências | Power BI, Power Query, Python, pandas |
| [Demonstrativos](projetos/processamento-demonstrativos/) | Conciliação com base faturável | Python, pandas, Excel |
| [Qualidade de Dados](projetos/automacao-excel/) | Padronização e confiabilidade das bases | Python, pandas, openpyxl |

## 🛠 Stack

`Python` · `pandas` · `Selenium` · `Playwright` · `PyAutoGUI` · `APIs` · `openpyxl` · `DuckDB` · `Power BI` · `Power Query` · `Excel`

## 🎯 Perfil

Atuação orientada a **melhoria de processos, automação, RPA, dados e indicadores**, conectando problemas operacionais a soluções técnicas mensuráveis.

---
**Luiz Henrique Garcia · São Paulo, Brasil**
