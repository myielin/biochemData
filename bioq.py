from sklearn.linear_model import LinearRegression as reg
from sklearn.metrics import r2_score
import streamlit as st
import plotly.express as px
import pandas as pd


##### dados
bsa = pd.DataFrame({
    'água destilada (uL)': [2000, 1800, 1500, 1250, 500, 0],
    'BSA [1500 ug/mL](uL)': [0, 200, 500, 750, 1500, 2000],
    'concentração': [0, 0.1, 0.25, 0.375, 0.75, 1]
    }, index=["0", "1", "2", "3", "4", "5"])

bf = pd.DataFrame({
    'Padrão diluído (uL)': ["60"],
    'Reagente de Bradford (mL)': ["3.0"],
    'Absorbância (595 nm)': [0, 0.098, 0.286, 0.474, 0.910]
}, index = ["0'", "1'", "2'", "3'", "4'"])

x = pd.DataFrame(bsa['concentração'][:-1])
y = pd.DataFrame(bf['Absorbância (595 nm)'])
absb = reg()
absb.fit(x, y)
coef = float(str(absb.coef_)[2:-2])
intr = float(str(absb.intercept_)[1:-1])
calc = [i*coef + intr for i in bsa['concentração'][:-1]]

##### markdowns
titlo = """<h1> Bioquímica experimental - grupo 5 </h1>
<h3> Quantificação de proteínas por espectrofotometria </h3>
"""
txt = """ <h4> Análise </h4>
        <p> A relação entere concentração e absorbância segue um comportamente linear com formula: </p> """

##### view
st.markdown(titlo, unsafe_allow_html=True)
st.table(bsa)
st.line_chart(bsa["concentração"].apply(lambda x: x*100))

st.table(bf)
st.write("o último dado foi desconsiderado por apresentar erro.")
st.write("É possível ver que a concentração do reagente de Bradford é constante: 3.0 mL")
st.line_chart(bf['Absorbância (595 nm)'])

st.markdown(txt, unsafe_allow_html=True)
st.write(f"f(x) = {coef}x + {intr}")
st.write(f"e R² igual a {r2_score(y, calc)}")

fig = px.line(x=bsa['concentração'][:-1], y=bf['Absorbância (595 nm)'])
st.plotly_chart(fig, use_container_width=True)
