# Matriz de Riscos - Migração de Sistema Legado para Nuvem

Este documento apresenta os principais riscos identificados para o projeto de migração, avaliados por probabilidade e impacto, seguindo boas práticas de gestão de riscos (PMBOK).

## Escala de avaliação

- **Probabilidade:** Baixa / Média / Alta
- **Impacto:** Baixo / Médio / Alto

## Matriz de Riscos

| ID | Risco | Probabilidade | Impacto | Nível de Exposição | Plano de Resposta |
|----|-------|----------------|---------|---------------------|--------------------|
| R1 | Perda de dados durante a migração | Média | Alto | Alto | Backup completo antes do cutover + testes de restauração |
| R2 | Indisponibilidade do sistema durante o corte (cutover) | Alta | Alto | Crítico | Janela de manutenção fora do horário comercial, plano de rollback definido |
| R3 | Resistência da equipe interna à mudança | Média | Médio | Médio | Treinamento e comunicação antecipada com stakeholders |
| R4 | Estouro de orçamento com custos de nuvem | Média | Médio | Médio | Monitoramento semanal de gastos na AWS/Azure, definição de alertas de custo |
| R5 | Incompatibilidade de sistemas legados com a nuvem | Baixa | Alto | Médio | Testes de compatibilidade já na fase de planejamento |

## Nível de Exposição (cálculo qualitativo)

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|---------------------------|-------|-------|------|
| **Alta**                   | Médio | Alto  | Crítico |
| **Média**                  | Baixo | Médio | Alto |
| **Baixa**                  | Baixo | Baixo | Médio |

## Observações

- Riscos classificados como **Crítico** ou **Alto** devem ser revisados semanalmente durante os Sprints correspondentes.
- Esta matriz deve ser atualizada ao longo do projeto conforme novos riscos são identificados ou riscos existentes são mitigados.

---
*Documento elaborado como parte do projeto de portfólio "Copiloto de Gestão de Projetos com IA Generativa", unindo MBA em Gestão de Projetos e Processos em TI e MBA em Ciência de Dados, Machine Learning e IA Avançada.*
