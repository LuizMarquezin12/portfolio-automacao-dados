# Arquitetura conceitual — Captura

```text
Base de entrada
      │
      ▼
Fila de consultas
      │
      ├──► Autenticação / autorização
      │
      ▼
Processamento pós-login
      │
      ├──► Validação da referência
      ├──► Obtenção do documento
      └──► Registro do resultado
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
    Capturada Pendente  Erro
        │                 │
        │          Retentativa / recuperação
        │                 │
        └────────┬────────┘
                 ▼
        Base consolidada
                 │
                 ▼
             Power BI
```

## Camada de resiliência

Falhas de rede podem acionar uma rotina controlada de recuperação de conectividade antes da retomada da fila. A implementação real não é publicada neste portfólio.

O desenho prioriza **rastreabilidade, idempotência, recuperação de falhas e separação de responsabilidades**.
