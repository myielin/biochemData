import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

##### dados
bsa = pd.DataFrame({
    'água destilada (uL)': [2000, 1800, 1500, 1250, 500, 0],
    'BSA [1500 ug/mL](uL)': [0, 200, 500, 750, 1500, 2000],
    'concentração': [0, 0.888, 0.333, 0.6, 3, 1.500]
    }, index=["0", "1", "2", "3", "4", "5"])

bf = pd.DataFrame({
    'Padrão diluído (uL)': ["60"],
    'Reagente de Bradford (mL)': ["3.0"],
    'Absorbância (595 nm)': [0, 0.098, 0.286, 0.474, 0.910]
}, index = ["0'", "1'", "2'", "3'", "4'"])

##### markdowns
titlo = """<h1> Bioquímica experimental - grupo 5 </h1>
<h3> Quantificação de proteínas por espectrofotometria </h3>
"""

##### view
st.markdown(titlo, unsafe_allow_html=True)
st.table(bsa)
st.line_chart(bsa["concentração"])
st.line_chart(bsa["BSA [1500 ug/mL](uL)"])

st.table(bf)
st.write("é possível ver que a concentraão do reagente de Bradford é constante: 3.0 mL")
st.line_chart(bf['Absorbância (595 nm)'])
