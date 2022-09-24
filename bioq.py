import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

vals = pd.DataFrame({
    'água destilada (uL)': [2000, 1800, 1500, 1250, 500, 0],
    'BSA [1500 ug/mL](uL)': [0, 200, 500, 750, 1500, 2000],
    'concentração': [1.500, 0.888, 0.333, 0.6, 3, 1.500]
    }, index=["B", "1", "2", "3", "4", "5"])


titlo = """<h1> Bioquímica experimental - grupo 5 </h1>
            <h3> Quantificação de proteínas por espectrofotometria </h3>
        """

st.markdown(titlo, unsafe_allow_html=True)
st.table(vals)
st.line_chart(vals["concentração"])
st.line_chart(vals["BSA [1500 ug/mL](uL)"])
