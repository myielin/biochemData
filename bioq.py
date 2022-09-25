from sklearn.linear_model import LinearRegression as reg
from sklearn.metrics import r2_score
import streamlit as st
import plotly.express as px
import pandas as pd

##### dados
conc = pd.DataFrame({'v':[0, 1500*0.1, 1500*0.25, 1500*0.375, 1500*0.75, 1500]})
bsa = pd.DataFrame({
    'água destilada (uL)': [2000, 1800, 1500, 1250, 500, 0],
    'BSA [1500 ug/mL](uL)': [0, 200, 500, 750, 1500, 2000],
    'concentração ug/mL': [
                        f"1500*0 = 2000*C2    | C2 = {1500*0}",
                        f"1500*200 = 2000*C2    | C2 = {1500*0.1}",
                        f"1500*500 = 2000*C2  | C2 = {1500*0.25}",
                        f"1500*750 = 2000*C2  | C2 = {1500*0.375}",
                        f"1500*1500 = 2000*C2 | C2 = {1500*0.75}",
                        f"1500*750 = 2000*C2  | C2 = {1500*1}"]
    }, index=["0", "1", "2", "3", "4", "5"])

bf = pd.DataFrame({
    'Padrão diluído (uL)': ["60"],
    'Reagente de Bradford (mL)': ["3.0"],
    'Absorbância (595 nm)': [0, 0.098, 0.286, 0.474, 0.910]
}, index = ["0'", "1'", "2'", "3'", "4'"])

y = pd.DataFrame(bf['Absorbância (595 nm)'])
absb = reg()
absb.fit(conc[:-1], y)
coef = float(str(absb.coef_)[2:-2])
intr = float(str(absb.intercept_)[1:-1])
calc = [i*coef + intr for i in conc['v'][:-1]]

##### markdowns
titlo = """<h1> Bioquímica experimental - grupo 5 </h1>
<h3> Quantificação de proteínas por espectrofotometria </h3>
"""
txt = """ <h4> Análise </h4>
        <p> A relação entere concentração e absorbância segue um comportamente linear com formula: </p> """

##### view
st.markdown(titlo, unsafe_allow_html=True)
st.table(bsa)
st.line_chart(conc)

st.table(bf)
st.write("o último dado foi desconsiderado por apresentar erro.")
st.write("É possível ver que a concentração do reagente de Bradford é constante: 3.0 mL")
st.line_chart(bf['Absorbância (595 nm)'])

st.markdown(txt, unsafe_allow_html=True)
st.write(f"f(x) = {coef}x + {intr}")
st.write(f"e R² igual a {r2_score(y, calc)}")

st.table(pd.DataFrame({'concentração': [0, 1500*0.1, 1500*0.25, 1500*0.375, 1500*0.75], 'Absorbância': [0, 0.098, 0.286, 0.474, 0.910]}))
fig = px.line(x=conc['v'][:-1], y=bf['Absorbância (595 nm)'])
st.plotly_chart(fig, use_container_width=True)
