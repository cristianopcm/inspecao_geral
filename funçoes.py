import streamlit as st
import pandas as pd
from datetime import date

hoje = str(date.today())

def cabeçalho(maquina, tipo_manutencao):
    st.subheader(f"**{maquina}** - {tipo_manutencao} SMC: {maquina}{hoje.replace('-','')}")
    st.divider()


def checklist(titulo, itens, prefixo):
    st.markdown(f'**{titulo}**')
    resposta = {}
    cols = st.columns(2)
    for idx, item in enumerate(itens):
        col_set = cols[0] if idx %2 == 0 else cols[1]
        resposta[item] = col_set.checkbox(item, key=f'{prefixo}_{titulo}_{idx}')
    return resposta

def datahora(prefixo):
    st.markdown('**Data/Hora**')
    col1, col2 = st.columns(2)
    with col1:
        dt1 = col1.date_input('Data de Inicio', key= f'{prefixo}_dt1')
        dt2 = col1.date_input('Data Término', key= f'{prefixo}_dt2')
    with col2:
        tp1 = col2.time_input('Hora de Inicio', key= f'{prefixo}_tp1')
        tp2 = col2.time_input('Hora de Termino', key= f'{prefixo}_tp2')
    return {'Inicio': f"{dt1} {tp1}", 'Fim': f"{dt2} {tp2}" }

def tecnicos(prefixo):
    st.markdown('**Equipe Técnica**')
    col1, col2, col3 = st.columns(3)
    t1 = col1.text_input('Técnico 1', key= f'{prefixo}_tec1')
    t2 = col2.text_input('Técnico 2', key= f'{prefixo}_tec2')
    t3 = col3.text_input('Técnico 3', key= f'{prefixo}_tec3')


