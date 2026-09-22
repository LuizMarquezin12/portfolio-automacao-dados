# 🤖 Case — Automação de Captura de Faturas

## 🔴 Cenário inicial

A operação exigia consultas repetitivas em diferentes portais, identificação da referência correta, obtenção dos documentos e controle do que já havia sido atendido. Em escala, o processo consumia tempo operacional e dependia também de captura terceirizada.

## 🧭 Evolução técnica

### 1. Automação do fluxo repetitivo
Os primeiros fluxos automatizaram navegação, consulta, identificação da fatura e organização dos documentos.

### 2. Controle operacional
A solução passou a registrar estados como sucesso, pendência e erro, permitindo retomar o processamento sem reiniciar toda a fila.

### 3. Mudanças de portal e autenticação
Com a evolução dos sites, apareceram novos fluxos, mensagens adicionais de autenticação, falhas temporárias e mecanismos de proteção de sessão/anti-bot.

A arquitetura foi adaptada para separar autenticação/autorização das etapas posteriores de processamento.

> Este portfólio não publica métodos para contornar CAPTCHA, anti-bot ou controles de acesso.

### 4. Resiliência de conectividade
Em execuções e testes prolongados, falhas de conectividade também precisavam ser tratadas.

Foi criada uma integração com **Android Debug Bridge (ADB)** para controlar ciclos de reconexão de um dispositivo de rede em ambiente de testes. O fluxo conseguia:

- solicitar a reinicialização controlada da conexão;
- aguardar um intervalo de segurança;
- verificar/restabelecer conectividade;
- somente então continuar a fila;
- preservar o estado do processamento para evitar perda de trabalho.

Essa camada foi criada para **recuperação de conectividade e tolerância a falhas**, não para burlar mecanismos de segurança.

### 5. Captura e tratamento do documento
Quando o sistema disponibilizava o documento de maneira estruturada e o acesso era autorizado, a automação podia processar o conteúdo retornado pela aplicação e salvar o PDF, reduzindo dependência de cliques e tornando o pós-login mais confiável.

### 6. Integração com indicadores
O resultado das capturas deixou de ser apenas uma pasta de PDFs. Os status passaram a alimentar o acompanhamento de **faturável × atendido × faltante × pendente**, conectado ao case de BI deste portfólio.

## 📊 Impacto observado

- fluxos com capacidade de aproximadamente **300–400 faturas/dia**;
- caso de alta volumetria com cerca de **1.150 consultas processadas em 2h10**;
- redução relevante de atividades manuais repetitivas;
- menor tempo de processamento;
- maior rastreabilidade de erros e pendências;
- redução de custo com captura terceirizada;
- a internalização da capacidade de automação contribuiu para a **descontinuidade de um fornecedor externo de captura**.

> O valor financeiro economizado não é divulgado por confidencialidade.

## 🛠 Tecnologias e conceitos

`Python` · `Selenium` · `Playwright` · `PyAutoGUI` · `ADB` · `pandas` · `APIs` · `PDF/Base64` · `Excel` · `RPA` · `logs` · `retry/backoff`

## 🔒 Segurança e confidencialidade

O `demo.py` deste repositório é propositalmente simplificado. Ele não contém URLs privadas, credenciais, dados de clientes, código corporativo, parâmetros reais de autenticação ou técnicas de evasão de controles de acesso.
