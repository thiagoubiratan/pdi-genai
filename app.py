import streamlit as st

texto = st.text_input("Digite algo")
if st.button("Enviar"):
    st.write(f"Você digitou: {texto}")