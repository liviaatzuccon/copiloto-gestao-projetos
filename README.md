# Copiloto de Gestão de Projetos com IA Generativa

Sistema que se conecta em tempo real ao Jira e gera automaticamente relatórios de status de projeto adaptados ao público-alvo (equipe técnica ou liderança/sponsor), combinando fundamentos de Gestão de Projetos com Ciência de Dados e IA.

Dashboard ao vivo: [copiloto-gestao-projetos.streamlit.app](https://copiloto-gestao-projetos-6i2of7dmyy99wkelytaduj.streamlit.app/)

---

## Sobre o Projeto

Este projeto foi desenvolvido como trabalho de portfólio, unindo competências dos MBAs em Gestão de Projetos e Processos em TI e Ciência de Dados, Machine Learning e IA Avançada.

A proposta: eliminar o trabalho manual de transformar dados brutos de um projeto (tarefas, prazos, status) em relatórios de status compreensíveis — tarefa que hoje consome horas de um gerente de projetos toda semana. O sistema busca os dados diretamente do Jira via API e gera automaticamente relatórios em linguagem natural, adaptados a diferentes públicos.

**Cenário de base:** Migração de Sistema Legado para a Nuvem — projeto simulado de uma empresa migrando sistemas on-premise para AWS/Azure, com 5 fases (Épicos), 20 tarefas, cronograma de 4 meses e gestão realizada com metodologia Scrum.

---

## Funcionalidades

- **Conexão em tempo real com o Jira** via API REST, buscando tarefas, status e prazos
- **Geração de relatórios adaptados ao público:**
  - Relatório técnico (detalhado, por tarefa, com foco em atrasos e recomendações)
  - Relatório executivo (curto, direto, focado em decisão da liderança)
- **Curva S** — gráfico de progresso planejado x realizado, acumulado ao longo do tempo
- **Guardrails de validação** — checagem automática que garante que os relatórios gerados são consistentes com os dados reais do Jira, sem inconsistências ou dados inventados
- **Preenchimento automatizado de dados** — script que atualiza prazos de múltiplas tarefas no Jira via API, eliminando trabalho manual repetitivo

---

## Estrutura do Projeto

```
copiloto-gestao-projetos/
├── docs/
│   ├── matriz_riscos.md       # Matriz de riscos do projeto (probabilidade x impacto)
│   └── raci.md                 # Matriz RACI de responsabilidades por fase
├── dashboard.py                 # Dashboard interativo (Streamlit)
├── gerar_relatorio.py           # Conexão com Jira e geração dos relatórios
├── curva_s.py                   # Cálculo da Curva S (planejado x realizado)
├── guardrails.py                # Validação de consistência dos relatórios
├── listar_tarefas.py            # Script utilitário de listagem de tarefas
├── preencher_datas.py           # Script de preenchimento automatizado de prazos
├── requirements.txt             # Dependências do projeto
└── .env                         # Credenciais locais (não versionado)
```

---

## Pipeline do Projeto

1. **Planejamento** — estruturação do projeto no Jira (Épicos, tarefas, cronograma), seguindo metodologia Scrum
2. **Gestão de riscos** — elaboração de matriz de riscos e matriz RACI
3. **Integração via API** — conexão segura ao Jira usando token de API e variáveis de ambiente
4. **Processamento** — cálculo de métricas de progresso, detecção de atrasos e cálculo da Curva S
5. **Geração de relatórios** — transformação dos dados brutos em relatórios em linguagem natural, adaptados ao público
6. **Validação** — guardrails conferindo consistência entre relatório gerado e dados de origem
7. **Dashboard** — interface interativa via Streamlit
8. **Deploy** — publicação pública via Streamlit Community Cloud

---

## Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/liviaatzuccon/copiloto-gestao-projetos.git
cd copiloto-gestao-projetos

# Instale as dependências
pip install -r requirements.txt

# Configure as credenciais (crie um arquivo .env na raiz do projeto)
# JIRA_URL=https://seudominio.atlassian.net
# JIRA_EMAIL=seu_email@exemplo.com
# JIRA_API_TOKEN=seu_token_aqui

# Rode o dashboard
streamlit run dashboard.py
```

---

## Principais Aprendizados

- Integração prática entre APIs REST e automação de processos de gestão
- Importância de proteger credenciais sensíveis (uso de `.env` e variáveis de ambiente/secrets), tanto em ambiente local quanto em produção
- Adaptação de uma mesma fonte de dados para diferentes formatos de comunicação, conforme o público-alvo
- Implementação de guardrails como prática de confiabilidade em sistemas que geram texto automaticamente
- Deploy de aplicações Python com dependências gerenciadas via `requirements.txt`
- Aplicação prática de conceitos de gestão de projetos (matriz de riscos, RACI, Curva S) em um produto de software real

---

## Próximos Passos

- Substituir a camada de geração de relatórios (atualmente baseada em regras) pela API da Anthropic (Claude), permitindo textos gerados livremente por IA generativa
- Adicionar testes automatizados
- Adicionar diagrama de arquitetura do sistema

---

## Links

- Dashboard Público: [copiloto-gestao-projetos.streamlit.app](https://copiloto-gestao-projetos-6i2of7dmyy99wkelytaduj.streamlit.app/)
- Código-fonte (este repositório): [github.com/liviaatzuccon/copiloto-gestao-projetos](https://github.com/liviaatzuccon/copiloto-gestao-projetos)

---

Projeto desenvolvido por Livia Atzuccon como parte de portfólio pessoal, unindo MBA em Gestão de Projetos e Processos em TI e MBA em Ciência de Dados, Machine Learning e IA Avançada.
