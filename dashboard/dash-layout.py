# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__) #cria o aplicativo

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("dados.xlsx")
opcoes = list(df['ID Motorista'].unique()) #variável que disponibiliza a lista de viagens de diferentes tipos, baseada apenas no ID Motorista
opcoes.append("Todos Motoristas") #adiciona a lista a opção "Todos os Motoristas"

fig = px.bar(df, x="ID Motorista", y="Quantidade", color="Tipo", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Logística de frotas'),

    html.Div(children='''
        Visão geral rotas concluidas x motoristas
    '''),

    html.Div(children='', id = "texto"), #div que será modificada a partir do dropdown

    dcc.Dropdown(opcoes, value='Todos Motoristas', id='drop_lista_motoristas'),

    dcc.Graph(
        id='grafico_motoristas_viagens',
        figure=fig
    )
])

@callback( #DECORATOR - Atribui ao def uma funcionalidade
    Output('texto', 'children'), #define quem será modificado através do input
    Input('drop_lista_motoristas', 'value') #define que seleciona o valor ou seja que passa o valor para o que será modificado.
)
def update_output(value):
    return f'Motorista selecionado: {value}'

@callback( #DECORATOR - Atribui ao def uma funcionalidade
    Output('grafico_motoristas_viagens', 'figure'), #define quem será modificado através do input
    Input('drop_lista_motoristas', 'value') #define que seleciona o valor ou seja que passa o valor para o que será modificado.
)
def update_output(value):
    if value == "Todos Motoristas":
      fig = px.bar(df, x="ID Motorista", y="Quantidade", color="Tipo", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Motorista'] == value, :]
        fig = px.bar(tabela_filtrada, x="ID Motorista", y="Quantidade", color="Tipo", barmode="group")
    return fig
 

if __name__ == '__main__': 
    app.run(debug=True)
