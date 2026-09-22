# 🤖 Case — Automação de Captura de Faturas

## 🔴 Cenário anterior
A operação dependia de consultas repetitivas em portais de diferentes distribuidoras, download de documentos e controle manual do que já havia sido capturado.

Além do volume, cada portal possuía comportamento próprio e podia mudar ao longo do tempo.

## 🟡 Desafios encontrados
- múltiplas distribuidoras e fluxos diferentes;
- falhas temporárias e necessidade de retentativa;
- alterações de páginas e etapas de autenticação;
- mecanismos adicionais de proteção de sessão/anti-bot;
- necessidade de identificar documentos corretos e organizar referências;
- rastreabilidade do que foi capturado ou ficou pendente.

## 🟢 Solução
Foram desenvolvidas automações/RPA em Python com Selenium, Playwright, PyAutoGUI e integrações via APIs quando apropriado.

A arquitetura passou a incluir filas, validações, logs, retentativas, recuperação de falhas e separação entre autenticação/autorização e processamento automatizado posterior.

> Este portfólio não publica métodos para contornar CAPTCHA, anti-bot ou controles de acesso.

## 📊 Resultados
- fluxos com capacidade observada de **300–400 faturas por dia**;
- um caso de alta volumetria atingiu aproximadamente **1.150 consultas em 2h10**;
- redução relevante do tempo gasto em tarefas repetitivas;
- aumento da capacidade operacional;
- redução de custo com captura terceirizada, contribuindo para a descontinuidade de um fornecedor externo desse processo.

O valor financeiro não é divulgado por confidencialidade.

## 💻 Código
[`demo.py`](demo.py) mostra apenas a arquitetura de fila/status, sem acesso a portais reais.
