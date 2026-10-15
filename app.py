import streamlit as st

# Configuração da página e título principal com ícone amigável
st.set_page_config(page_title="Calculadora Simples", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora Interativa")
st.write("Bem-vindo ao seu app de **Vibe Coding**! Faça cálculos rápidos de forma simples e elegante.")

st.markdown("---")

# Dois campos de entrada numérica sem formatação fixa de decimais
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0)
with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0)

# Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("")

# Botão de ação "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    
    # Lógica de cálculo com tratamento de divisão por zero
    erro = False
    
    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        if num2 == 0:
            erro = True
            st.error("⚠️ Opa! Divisão por zero não é permitida na matemática convencional. Tente outro valor para o segundo número.")
        else:
            resultado = num1 / num2
            
    # Se não houver erro, exibe o resultado de forma inteligente
    if not erro:
        # Se o resultado for inteiro (ex: 4.0), removemos o .0 para ficar limpo
        if resultado.is_integer():
            resultado_final = int(resultado)
        else:
            resultado_final = round(resultado, 4)
            
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado", value=resultado_final)

# Rodapé simples
st.markdown("---")
st.caption("💡 Dica: Agora o app se adapta automaticamente, exibindo números inteiros sem decimais desnecessários.")
