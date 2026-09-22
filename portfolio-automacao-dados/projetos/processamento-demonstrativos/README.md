# 📑 Case — Processamento de Demonstrativos

## 🔴 Problema
Parte dos atendimentos podia existir em demonstrativos com formatos diferentes e não aparecer diretamente na mesma origem das capturas.

## 🟢 Solução
Automação para:
- ler demonstrativos;
- normalizar UCs/contratos;
- cruzar com a base faturável;
- identificar correspondências;
- incorporar o resultado ao acompanhamento do BI.

## 🎯 Resultado
O demonstrativo deixa de ser um arquivo isolado e passa a fazer parte do controle consolidado de atendimento e pendências.

## 🛠 Stack
Python · pandas · openpyxl · Excel
