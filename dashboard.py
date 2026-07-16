import streamlit as st
import altair as alt
from gerar_relatorio import buscar_tarefas, gerar_relatorio_tecnico, gerar_relatorio_executivo
from curva_s import calcular_curva_s

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

st.divider()
st.subheader("📈 Curva S — Planejado x Realizado")

if st.button("Gerar Curva S"):
    with st.spinner("Calculando progresso do projeto..."):
        tarefas_curva = buscar_tarefas()
        df_curva = calcular_curva_s(tarefas_curva)

    if df_curva.empty:
        st.info("Ainda não há dados suficientes para gerar a Curva S.")
    else:
        grafico = alt.Chart(df_curva).mark_line(point=True).encode(
            x=alt.X("data:T", title="Data"),
            y=alt.Y("percentual:Q", title="% Concluído (acumulado)"),
            color=alt.Color("tipo:N", title="Série"),
        ).properties(height=400)

        st.altair_chart(grafico, use_container_width=True)