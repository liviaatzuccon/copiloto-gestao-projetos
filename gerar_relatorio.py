import os
from datetime import date
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def obter_config(chave):
    """Busca a configuração no .env local, ou nos Secrets do Streamlit Cloud."""
    valor = os.getenv(chave)
    if valor:
        return valor
    try:
        return st.secrets[chave]
    except Exception:
        return None


JIRA_URL = obter_config("JIRA_URL")
JIRA_EMAIL = obter_config("JIRA_EMAIL")
JIRA_API_TOKEN = obter_config("JIRA_API_TOKEN")


def buscar_tarefas():
    """Busca todas as tarefas do projeto CLOUD no Jira."""
    url = f"{JIRA_URL}/rest/api/3/search/jql"
    params = {
        "jql": "project = CLOUD AND issuetype != Epic ORDER BY key ASC",
        "maxResults": 50,
        "fields": "summary,status,parent,duedate,resolutiondate"
    }
    response = requests.get(
        url,
        auth=(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
        params=params
    )
    response.raise_for_status()
    return response.json()["issues"]


def gerar_relatorio_tecnico(tarefas):
    """Simula o que uma IA generativa produziria: um relatório técnico detalhado."""
    hoje = date.today()

    total = len(tarefas)
    feitas = [t for t in tarefas if t["fields"]["status"]["name"] == "Feito"]
    em_andamento = [t for t in tarefas if t["fields"]["status"]["name"] in ("Fazendo", "Em análise")]
    a_fazer = [t for t in tarefas if t["fields"]["status"]["name"] == "A fazer"]

    atrasadas = []
    for t in tarefas:
        prazo = t["fields"].get("duedate")
        status = t["fields"]["status"]["name"]
        if prazo and status != "Feito":
            data_prazo = date.fromisoformat(prazo)
            if data_prazo < hoje:
                atrasadas.append(t)

    percentual_concluido = round(len(feitas) / total * 100, 1) if total else 0

    linhas = []
    linhas.append("=" * 60)
    linhas.append("RELATÓRIO TÉCNICO DE STATUS DO PROJETO")
    linhas.append("Migração de Sistema Legado para Nuvem")
    linhas.append(f"Data do relatório: {hoje.strftime('%d/%m/%Y')}")
    linhas.append("=" * 60)
    linhas.append("")
    linhas.append("1. RESUMO GERAL")
    linhas.append(f"   Total de tarefas: {total}")
    linhas.append(f"   Concluídas: {len(feitas)} ({percentual_concluido}%)")
    linhas.append(f"   Em andamento: {len(em_andamento)}")
    linhas.append(f"   A fazer: {len(a_fazer)}")
    linhas.append(f"   Atrasadas: {len(atrasadas)}")
    linhas.append("")

    linhas.append("2. TAREFAS ATRASADAS (ATENÇÃO)")
    if atrasadas:
        for t in atrasadas:
            chave = t["key"]
            titulo = t["fields"]["summary"]
            prazo = t["fields"]["duedate"]
            linhas.append(f"   - [{chave}] {titulo} (prazo era {prazo})")
    else:
        linhas.append("   Nenhuma tarefa atrasada no momento.")
    linhas.append("")

    linhas.append("3. DETALHAMENTO POR TAREFA")
    for t in tarefas:
        chave = t["key"]
        titulo = t["fields"]["summary"]
        status = t["fields"]["status"]["name"]
        prazo = t["fields"].get("duedate", "sem prazo definido")
        linhas.append(f"   [{chave}] {titulo}")
        linhas.append(f"        Status: {status} | Prazo: {prazo}")
    linhas.append("")

    linhas.append("4. RECOMENDAÇÕES")
    if atrasadas:
        linhas.append(f"   - Priorizar as {len(atrasadas)} tarefa(s) atrasada(s) listada(s) acima.")
    if percentual_concluido < 50:
        linhas.append("   - Projeto abaixo de 50% de conclusão; recomenda-se revisão de cronograma.")
    if not atrasadas and percentual_concluido >= 50:
        linhas.append("   - Projeto dentro do esperado, sem pontos críticos de atenção.")

    linhas.append("=" * 60)

    return "\n".join(linhas)


def gerar_relatorio_executivo(tarefas):
    """Simula o que uma IA generativa produziria: um relatório executivo, curto e direto."""
    hoje = date.today()

    total = len(tarefas)
    feitas = [t for t in tarefas if t["fields"]["status"]["name"] == "Feito"]
    percentual_concluido = round(len(feitas) / total * 100, 1) if total else 0

    atrasadas = []
    for t in tarefas:
        prazo = t["fields"].get("duedate")
        status = t["fields"]["status"]["name"]
        if prazo and status != "Feito":
            data_prazo = date.fromisoformat(prazo)
            if data_prazo < hoje:
                atrasadas.append(t)

    if atrasadas:
        situacao = "ATENÇÃO NECESSÁRIA"
    elif percentual_concluido >= 70:
        situacao = "NO CAMINHO CERTO"
    else:
        situacao = "EM ANDAMENTO"

    linhas = []
    linhas.append("RELATÓRIO EXECUTIVO — Migração de Sistema Legado para Nuvem")
    linhas.append(f"Data: {hoje.strftime('%d/%m/%Y')}")
    linhas.append("")
    linhas.append(f"Situação geral: {situacao}")
    linhas.append(f"Progresso: {percentual_concluido}% concluído ({len(feitas)} de {total} tarefas)")
    linhas.append("")

    if atrasadas:
        linhas.append(f"Ponto de atenção: {len(atrasadas)} tarefa(s) com prazo vencido, requer decisão da liderança.")
    else:
        linhas.append("Não há tarefas atrasadas no momento.")

    linhas.append("")
    linhas.append("Próximo marco: acompanhar a fase em andamento e manter o ritmo atual de entregas.")

    return "\n".join(linhas)


if __name__ == "__main__":
    tarefas = buscar_tarefas()

    print(gerar_relatorio_tecnico(tarefas))
    print("\n\n")
    print(gerar_relatorio_executivo(tarefas))