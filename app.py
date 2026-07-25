import streamlit as st  # importa a biblioteca Streamlit, apelidada de "st"

st.title("Calculadora")  # exibe um título grande no topo da página

# number_input cria um campo numérico na tela, value=0.0 define o valor inicial
numero1 = st.number_input("Primeiro número", value=0.0)
numero2 = st.number_input("Segundo número", value=0.0)

# selectbox cria um dropdown com as opções listadas
operacao = st.selectbox("Operação", ["Soma", "Subtração", "Multiplicação", "Divisão"])

if st.button("Calcular"):  # executa o bloco abaixo somente quando o botão for clicado
    
    if operacao == "Soma":  # verifica qual operação foi selecionada
        resultado = numero1 + numero2
    elif operacao == "Subtração":
        resultado = numero1 - numero2
    elif operacao == "Multiplicação":
        resultado = numero1 * numero2
    elif operacao == "Divisão":
        if numero2 == 0:  # evita divisão por zero
            st.error("Divisão por zero não é permitida")  # exibe mensagem de erro em vermelho
        else:
            resultado = numero1 / numero2

    st.write(f"Resultado: {resultado}")  # exibe o resultado na tela