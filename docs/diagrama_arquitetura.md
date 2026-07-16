# Diagrama de Arquitetura — Copiloto de Gestão de Projetos

Este diagrama representa o fluxo de dados do sistema, desde a origem no Jira até a apresentação final ao usuário.

```mermaid
flowchart TD
    A[Jira Cloud<br/>Projeto CLOUD] -->|API REST + Token| B[gerar_relatorio.py<br/>buscar_tarefas]

    B --> C{Tipo de relatório<br/>solicitado}

    C -->|Técnico| D[gerar_relatorio_tecnico]
    C -->|Executivo| E[gerar_relatorio_executivo]

    B --> F[curva_s.py<br/>calcular_curva_s]

    D --> G[guardrails.py<br/>validar_relatorio]
    E --> G

    G -->|Sem inconsistências| H[dashboard.py<br/>Streamlit]
    G -->|Inconsistências detectadas| H

    F --> H

    H --> I[Usuário final<br/>navegador]

    J[.env / Streamlit Secrets<br/>credenciais protegidas] -.->|autenticação| B

    style A fill:#2684FF,color:#fff
    style H fill:#FF4B4B,color:#fff
    style G fill:#00C851,color:#fff
    style J fill:#666,color:#fff
```

## Componentes

| Componente | Responsabilidade |
|---|---|
| **Jira Cloud** | Fonte de dados: tarefas, status, prazos e datas de conclusão |
| **gerar_relatorio.py** | Busca dados via API REST e gera os relatórios (técnico e executivo) |
| **curva_s.py** | Calcula o progresso acumulado planejado x realizado |
| **guardrails.py** | Valida se o relatório gerado é consistente com os dados de origem, prevenindo inconsistências |
| **dashboard.py** | Interface interativa (Streamlit) que orquestra os módulos e apresenta os resultados |
| **.env / Streamlit Secrets** | Armazenamento seguro de credenciais (token, e-mail, URL), nunca versionado no código |

## Fluxo resumido

1. O usuário escolhe o tipo de relatório desejado no dashboard
2. O sistema autentica-se no Jira usando credenciais protegidas
3. As tarefas do projeto são buscadas via API REST
4. Os dados são processados e transformados em relatório (técnico ou executivo) e/ou Curva S
5. O guardrail valida o relatório gerado contra os dados brutos, antes de exibi-lo
6. O resultado final é exibido ao usuário através do dashboard

---
*Diagrama elaborado como parte do projeto de portfólio "Copiloto de Gestão de Projetos com IA Generativa".*
