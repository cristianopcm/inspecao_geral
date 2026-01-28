import streamlit as st

st.set_page_config(layout='wide')

with open ('style.css') as f:
    st.markdown(f'<style> {f.read()}</style>', unsafe_allow_html= True)

st.title('Titulo 1 ')

st.button('Clique Aqui')

with st.container():
        st.title('Data/Hora de Inspeção',)
        col1, col2 = st.columns(2)
        with col1:
            st.date_input('Data de Início:')
            st.date_input('Data de Término:')
        with col2:
            st.time_input('Hora de Início:', step=300)
            st.time_input('Hora de Término:', step=300)

