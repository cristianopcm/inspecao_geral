import streamlit as st
import os
import pandas as pd
from funçoes import datahora, checklist, cabeçalho, tecnicos



desenrolador_itens = [' Verificar Contra Ponta', 'Verificar Unidade Hidráulica', 
                      'Verificar Mangueira/Conexões Hidráulicas', 
                      'Verificar Magueiras/Conexões Pneumáticas',
                        'Verificar Cilindro Hidráulico', 'Verificar Funcionamento de Freio']

desenrolador_multiplo = ['Verificar Integridade do Eixos', 'Verificar Cilindros do Freios', 
                         'Verificar mangueiras/Conexões Pneumáticas', 'Verificar Aderência do Freio',
                           'Verifcar Roletes/Roldanas de Desvio']

bobinador_630 = ['Verificar Contra Ponta', 'Lubrificar Contra Ponta', 'Verificar Nível de Óleo Redutor']

def renderizar(maquina, tipo, nome_equip, item, id):
    with st.form(key=f'form{id}'):
        cabeçalho(maquina, tipo)
        check_dados = checklist(nome_equip, item, id)
        st.divider()
        tempo_dados = datahora(id)
        st.divider()
        equipe = tecnicos(id)
        st.divider()
        obs = st.text_area('**Observação**', key=f'{id}_obs')

        submit = st.form_submit_button(f'Salvar {maquina}', key= f'{id}_sub')
    
        if submit:
            dados = {
                'Máquina': maquina,
                'Tipo': tipo,
                'Data de Inicio': tempo_dados['Inicio'],
                'Data de Termino': tempo_dados['Fim'],
                'Equipe': '.'.join([t for t in equipe if t]),
                'Observação': obs
            }
            dados.update(check_dados)

            df = pd.DataFrame([dados])
            if not os.path.isfile('historico.csv'):
                df.to_csv('historico.csv', index= False)
            else:
                df.to_csv('historico.csv', mode= 'a', header= False, index= False)
            
aba1, aba2, aba3 = st.tabs(['BN53', 'BN55', 'BN45'])
with aba1:
    renderizar('BN 53', 'Mecânica', 'DESENROLADOR', desenrolador_multiplo, 'BN53')

with aba2:
    renderizar('BN 55', 'Mecânica', 'BOBINADOR', bobinador_630, 'BN55')

with aba3:
    renderizar('BN 45', 'Mecânica', 'BOBINADOR', bobinador_630, 'BN45')