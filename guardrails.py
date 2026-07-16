def validar_relatorio(tarefas, relatorio_texto):
    """
    Guardrail: verifica se o relatório gerado é consistente com os dados brutos do Jira.
    Retorna uma lista de problemas encontrados (vazia se tudo estiver correto).
    """
    problemas = []

    if not tarefas:
        problemas.append("Nenhuma tarefa foi retornada pelo Jira — relatório não deve ser gerado.")
        return problemas

    chaves_reais = {t["key"] for t in tarefas}

    # Verifica se todas as chaves de tarefa mencionadas no relatório realmente existem
    import re
    chaves_no_relatorio = set(re.findall(r"CLOUD-\d+", relatorio_texto))
    chaves_inventadas = chaves_no_relatorio - chaves_reais

    if chaves_inventadas:
        problemas.append(
            f"O relatório menciona tarefas que não existem nos dados do Jira: {', '.join(chaves_inventadas)}"
        )

    # Verifica se o total de tarefas mencionado bate com o total real
    total_real = len(tarefas)
    match_total = re.search(r"Total de tarefas:\s*(\d+)", relatorio_texto)
    if match_total:
        total_no_relatorio = int(match_total.group(1))
        if total_no_relatorio != total_real:
            problemas.append(
                f"Total de tarefas divergente: relatório diz {total_no_relatorio}, mas o Jira retornou {total_real}."
            )

    return problemas