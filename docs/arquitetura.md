# Arquitetura dos cases (visão demonstrativa)

Os diagramas descrevem conceitos de projeto, **não a infraestrutura interna de uma empresa**.

## Rateio

```mermaid
flowchart TD
    A[Arquivos de entrada fictícios] --> B[Normalização e conferência]
    B --> C{Pendências?}
    C -->|Sim| D[Relatório de pendências]
    C -->|Não| E[Template de envio]
    E --> F[Validadores por distribuidora]
    F --> G[Saída conferida e logs]
```

**Decisões:** separar entrada e saída, validar competência e campos obrigatórios, registrar status por etapa e evitar publicar arquivos incompletos.

## Captura

```mermaid
flowchart TD
    A[Fila de consultas autorizadas] --> B[Acesso pelo fluxo permitido]
    B --> C{Documento disponível?}
    C -->|Sim| D[Conferência e armazenamento]
    C -->|Não| E[Registro de pendência]
    D --> F[Indicadores]
    E --> F
```

Os exemplos respeitam autenticação, CAPTCHA e controles de acesso; não documentam evasão dessas proteções.

## BI

Bases de referência e resultados passam por normalização, deduplicação e conciliação antes de gerar indicadores de total, atendido, faltante e pendente.

## Próximos passos técnicos

- Testes automatizados com dados sintéticos.
- Medição de duração por etapa.
- Verificação de integridade dos resultados.
- Pipeline de qualidade com GitHub Actions.

São **melhorias planejadas**, não funcionalidades já comprovadas nos exemplos atuais.
