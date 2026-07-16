import pandas as pd
from datetime import date, datetime


def calcular_curva_s(tarefas):
    """Calcula os dados da Curva S: progresso planejado x realizado, acumulado ao longo do tempo."""
    total = len(tarefas)

    # Monta lista de (data_prazo) para todas as tarefas que têm prazo definido
    prazos = []
    for t in tarefas:
        prazo = t["fields"].get("duedate")
        if prazo:
            prazos.append(date.fromisoformat(prazo))

    # Monta lista de (data_conclusao) só das tarefas já concluídas
    conclusoes = []
    for t in tarefas:
        if t["fields"]["status"]["name"] == "Feito":
            resolucao = t["fields"].get("resolutiondate")
            if resolucao:
                # O Jira retorna data e hora juntas, pegamos só a data
                data_conclusao = datetime.fromisoformat(resolucao).date()
                conclusoes.append(data_conclusao)

    prazos.sort()
    conclusoes.sort()

    # Constrói a série acumulada planejada (% do total, acumulado por data de prazo)
    planejado = []
    for i, d in enumerate(prazos, start=1):
        planejado.append({"data": d, "percentual": round(i / total * 100, 1), "tipo": "Planejado"})

    # Constrói a série acumulada realizada (% do total, acumulado por data de conclusão real)
    realizado = []
    for i, d in enumerate(conclusoes, start=1):
        realizado.append({"data": d, "percentual": round(i / total * 100, 1), "tipo": "Realizado"})

    df = pd.DataFrame(planejado + realizado)
    return df