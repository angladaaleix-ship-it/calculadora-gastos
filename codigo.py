import streamlit as st


#UI
st.title("Calculadora de gastos 💸")
st.text('Pon tu salario aqui para calcular el reparto')
DINERO=st.number_input('Dime cuanto dinero has ganado este mes')
st.metric("Dinero total", f"{DINERO:.2f}€")
#ACCION
if st.button('Calcular reparto 💰'):
    if DINERO == 0:
        st.warning("Introduce un ingreso válido ⚠️")
    else:
        AHORROS = DINERO * 0.20
        COMIDA = DINERO * 0.70
        SNACKS = DINERO * 0.10
#RESPUESTA
        st.divider()
        st.subheader('📊 Reparto de gastos')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ahorros 💰", f"{AHORROS:.2f}€")
        with col2:
            st.metric("Comida 🍔", f"{COMIDA:.2f}€")
        with col3:
            st.metric("Snacks 🍿", f"{SNACKS:.2f}€")
        mensaje = f"Has ganado {DINERO:.2f} euros este mes. Deberías ahorrar {AHORROS:.2f}, gastar {COMIDA:.2f} en comida y {SNACKS:.2f} en snacks."
      



