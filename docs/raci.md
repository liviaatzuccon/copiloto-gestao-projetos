# Matriz RACI - Migração de Sistema Legado para Nuvem

A matriz RACI define os papéis e responsabilidades em cada fase do projeto:

- **R (Responsável):** quem executa a atividade
- **A (Aprovador):** quem aprova o resultado e responde por ele
- **C (Consultado):** quem é consultado antes de decisões/execução
- **I (Informado):** quem é apenas informado sobre o andamento

## Papéis considerados

- **PM** — Gerente de Projeto (Livia)
- **Infra** — Responsável de Infraestrutura/Cloud
- **Dev** — Desenvolvedor Backend
- **QA** — Responsável de Qualidade/Testes
- **Sponsor** — Patrocinador do projeto (liderança da empresa)

## Matriz RACI por fase

| Fase | PM | Infra | Dev | QA | Sponsor |
|------|----|----|----|----|---------|
| Planejamento e Levantamento | R/A | C | C | I | A |
| Preparação do Ambiente Cloud | A | R | C | I | I |
| Migração de Dados | A | R | R | C | I |
| Testes e Homologação | A | C | C | R | I |
| Go-live e Estabilização | R/A | R | C | R | C |

## Observações

- O **PM** mantém papel de Aprovador em todas as fases, garantindo alinhamento com escopo, prazo e orçamento.
- O **Sponsor** é mantido informado durante a execução técnica, mas é consultado ativamente na fase crítica de Go-live.
- Em fases técnicas (Preparação de Ambiente, Migração de Dados), a responsabilidade de execução é transferida para as áreas técnicas (Infra/Dev), com o PM em papel de acompanhamento e aprovação.

---
*Documento elaborado como parte do projeto de portfólio "Copiloto de Gestão de Projetos com IA Generativa", unindo MBA em Gestão de Projetos e Processos em TI e MBA em Ciência de Dados, Machine Learning e IA Avançada.*
