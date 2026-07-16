from datetime import date, timedelta
from gerar_relatorio import gerar_relatorio_tecnico, gerar_relatorio_executivo
from guardrails import validar_relatorio


def criar_tarefa(chave, status, prazo=None):
    """Função auxiliar para criar uma tarefa fictícia, no mesmo formato que o Jira retorna."""
    return {
        "key": chave,
        "fields": {
            "summary": f"Tarefa {chave}",
            "status": {"name": status},
            "duedate": prazo,
        }
    }


def test_relatorio_tecnico_conta_tarefas_corretamente():
    tarefas = [
        criar_tarefa("CLOUD-1", "Feito"),
        criar_tarefa("CLOUD-2", "Feito"),
        criar_tarefa("CLOUD-3", "Fazendo"),
        criar_tarefa("CLOUD-4", "A fazer"),
    ]
    relatorio = gerar_relatorio_tecnico(tarefas)

    assert "Total de tarefas: 4" in relatorio
    assert "Concluídas: 2 (50.0%)" in relatorio


def test_relatorio_tecnico_detecta_tarefa_atrasada():
    ontem = (date.today() - timedelta(days=1)).isoformat()
    tarefas = [
        criar_tarefa("CLOUD-1", "A fazer", prazo=ontem),
    ]
    relatorio = gerar_relatorio_tecnico(tarefas)

    assert "Atrasadas: 1" in relatorio
    assert "CLOUD-1" in relatorio


def test_relatorio_tecnico_nao_marca_tarefa_feita_como_atrasada():
    ontem = (date.today() - timedelta(days=1)).isoformat()
    tarefas = [
        criar_tarefa("CLOUD-1", "Feito", prazo=ontem),
    ]
    relatorio = gerar_relatorio_tecnico(tarefas)

    assert "Atrasadas: 0" in relatorio


def test_relatorio_executivo_situacao_atencao_quando_atrasado():
    ontem = (date.today() - timedelta(days=1)).isoformat()
    tarefas = [
        criar_tarefa("CLOUD-1", "A fazer", prazo=ontem),
    ]
    relatorio = gerar_relatorio_executivo(tarefas)

    assert "ATENÇÃO NECESSÁRIA" in relatorio


def test_relatorio_executivo_situacao_no_caminho_certo():
    tarefas = [
        criar_tarefa("CLOUD-1", "Feito"),
        criar_tarefa("CLOUD-2", "Feito"),
        criar_tarefa("CLOUD-3", "Feito"),
        criar_tarefa("CLOUD-4", "A fazer"),
    ]
    relatorio = gerar_relatorio_executivo(tarefas)

    assert "NO CAMINHO CERTO" in relatorio


def test_guardrail_aprova_relatorio_consistente():
    tarefas = [criar_tarefa("CLOUD-1", "Feito")]
    relatorio = gerar_relatorio_tecnico(tarefas)

    problemas = validar_relatorio(tarefas, relatorio)
    assert problemas == []


def test_guardrail_detecta_tarefa_inventada():
    tarefas = [criar_tarefa("CLOUD-1", "Feito")]
    relatorio_falso = "Total de tarefas: 1\nA tarefa CLOUD-999 está em risco."

    problemas = validar_relatorio(tarefas, relatorio_falso)
    assert len(problemas) > 0
    assert "CLOUD-999" in problemas[0]


def test_guardrail_detecta_total_divergente():
    tarefas = [criar_tarefa("CLOUD-1", "Feito"), criar_tarefa("CLOUD-2", "Feito")]
    relatorio_falso = "Total de tarefas: 5"

    problemas = validar_relatorio(tarefas, relatorio_falso)
    assert len(problemas) > 0