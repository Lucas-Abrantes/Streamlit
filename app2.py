from pyexpat import features
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


st.write("""
## Aplicativo simples de previsão para flores!

Este aplicativo prevê o tipo de flores de acordo com o comprimento e largura da 
sépala. Também, o comprimento e a largura da pétala
    !""")

#sidebar cria uma barra de navegação lateral
# a função header cria elemento de cabeçalho
st.sidebar.header('Digite os parâmetros de entrada')


def input_data():
    # slider: permite renderizar um controle deslizante de intervalo passando uma 
    # tupla ou lista de dois elementos como valor.
    #primeiro parâmetro = minimo
    #segundo parâmetro = maximo
    # ultimo parâmetro = padrão
    comprimento_sepala = st.sidebar.slider('Comprimento da Sépala (cm)', 2.0, 8.9, 5.5)
    largura_sepala = st.sidebar.slider('Largura da Sépala (cm)', 1.0, 5.7, 3.8)
    comprimento_petala = st.sidebar.slider('Comprimeto da Pétala (cm)', 1.0, 4.0, 0.2)
    largura_petala = st.sidebar.slider('Lagura da Pétala (cm)', 0.1, 2.5, 0.2)
    # aqui eu criei um dataframa para exibir os dados
    data = {'comprimento_sepala': comprimento_sepala, 
            'largura_sepala': largura_sepala,
            'comprimento_petala': comprimento_petala,
            'largura_petala': largura_petala}
    #index=[0] - retorna os primeiros elementos de cada variável
    features = pd.DataFrame(data, index=[0])
    return features

df = input_data()

#função que cria um subtítulo
st.subheader('Parêmatros de entrada')

#escreve o dataframe
st.write(df)


#carregando o conjunto de dados da íris
iris = datasets.load_iris()

#matriz dos dados
X = iris.data
#array de rótulos (ou seja, respostas) de cada entrada de dados
Y = iris.target


classficador = RandomForestClassifier()
# fit = treinar o nosso modelo
classficador.fit(X, Y)

#função de predição
predicao = classficador.predict(df)

#função de probabilidade
proba_predicao = classficador.predict_proba(df)

st.subheader('Classes correspondentes')
#obtendo nomes de rótulos, ou seja, as três espécies de flores
st.write(iris.target_names)

st.subheader('Predição')
st.write(iris.target_names[predicao])


st.subheader('Prababilidade de predição')
st.write(proba_predicao)

