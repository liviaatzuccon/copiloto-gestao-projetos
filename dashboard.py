import streamlit as st
from gerar_relatorio import buscar_tarefas, gerar_relatorio_tecnico, gerar_relatorio_executivo

st.set_page_config(page_title="Copiloto de Gestão de Projetos", page_icon="🤖")

st.title("🤖 Copiloto de Gestão de Projetos")
st.caption("Migração de Sistema Legado para Nuvem — dados em tempo real do Jira")

publico = st.selectbox(
    "Para quem é o relatório?",
    ["Relatório Técnico (equipe)", "Relatório Executivo (sponsor)"]
)

if st.button("Gerar relatório"):
    with st.spinner("Buscando dados do Jira e gerando relatório..."):
        tarefas = buscar_tarefas()

        if publico == "Relatório Técnico (equipe)":
            relatorio = gerar_relatorio_tecnico(tarefas)
        else:
            relatorio = gerar_relatorio_executivo(tarefas)

    st.success("Relatório gerado com sucesso!")
    st.text(relatorio)

    with st.expander("Ver dados brutos do Jira"):
        for t in tarefas:
            st.write(f"**{t['key']}** — {t['fields']['summary']} — Status: {t['fields']['status']['name']}")