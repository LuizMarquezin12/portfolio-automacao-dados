# 📈 Case — BI de Captura e Acompanhamento Operacional

## 🔴 Problema
Com múltiplos robôs, distribuidoras, competências e fontes, saber apenas que um robô havia rodado não era suficiente. Era necessário responder: **quanto da base faturável já foi atendido e o que ainda falta?**

## 🟢 Solução
Foi estruturado um pipeline de consolidação para alimentar um dashboard no Power BI.

O fluxo:
- lê bases faturáveis de diferentes competências;
- normaliza distribuidoras e identificadores;
- cruza capturas e outras fontes de atendimento;
- classifica cada registro;
- preserva histórico;
- gera uma base consolidada para o BI.

## 📊 Indicadores
- Total faturável
- Capturadas / atendidas
- Faltantes
- Pendências
- Taxa de captura
- Evolução por competência
- Visão por distribuidora
- Origem do atendimento

Em uma execução do pipeline, foram processadas **mais de 78 mil linhas faturáveis** distribuídas entre três competências, demonstrando a necessidade de automação também na camada analítica.

## 🎯 Resultado
A operação ganhou uma visão centralizada dos gaps, permitindo priorizar o que ainda precisava de ação em vez de conferir arquivos isoladamente.

## 🛠 Stack
Power BI · Power Query · Python · pandas · Excel

## 🔗 Papel do BI no ecossistema

O dashboard funciona como a camada de observabilidade do processo. Em vez de avaliar cada robô isoladamente, o cruzamento parte da base faturável e verifica quais registros foram efetivamente atendidos.

Isso conecta **automação operacional + qualidade de dados + gestão por indicadores** e permite direcionar esforço para os gaps restantes.
