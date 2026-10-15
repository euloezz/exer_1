# Primeiro Exercício
import streamlit as st

# Configuração da página e título principal com ícone amigável
st.set_page_config(page_title="Calculadora Simples", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora Interativa")
st.write("Bem-vindo ao seu app de **Vibe Coding**! Faça cálculos rápidos de forma simples e elegante.")

st.markdown("---")

# Dois campos de entrada numérica (st.number_input) com valores padrão 0.0
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.4f")

# Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("")

# Botão de ação "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    
    # Lógica de cálculo com tratamento de divisão por zero
    if operacao == "Soma (+)":
        resultado = num1 + num2
        st.success(f"O resultado de {num1} + {num2} é:")
        st.metric(label="Resultado", value=f"{resultado:.4f}")
        
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        st.success(f"O resultado de {num1} - {num2} é:")
        st.metric(label="Resultado", value=f"{resultado:.4f}")
        
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        st.success(f"O resultado de {num1} * {num2} é:")
        st.metric(label="Resultado", value=f"{resultado:.4f}")
        
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("⚠️ Opa! Divisão por zero não é permitida na matemática convencional. Tente outro valor para o segundo número.")
        else:
            resultado = num1 / num2
            st.success(f"O resultado de {num1} / {num2} é:")
            st.metric(label="Resultado", value=f"{resultado:.4f}")

# Rodapé simples
st.markdown("---")
st.caption("💡 Dica: Altere os números acima e clique em Calcular novamente para ver a mágica do Streamlit acontecer em tempo real.")
