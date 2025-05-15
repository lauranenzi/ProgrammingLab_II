import dash                      
from dash import dcc, html      
import plotly.express as px     
import pandas as pd            

# Caricamento di un dataset di esempio (Iris)
df = px.data.iris()  # Contiene misure di 3 specie di fiori

# Crea l'applicazione Dash
app = dash.Dash(__name__)  # __name__ serve per sapere se il file è eseguito direttamente

# Layout dell'app: definisce cosa l'utente vede
app.layout = html.Div([
    html.H2("Iris Dataset Scatter Plot"),  # Titolo

    # Menu a tendina per selezionare la specie
    dcc.Dropdown(
        id='species-dropdown',  # ID usato per il callback
        options=[{'label': s, 'value': s} for s in df['species'].unique()],  # Una voce per specie
        value='setosa'  # Valore iniziale
    ),

    # Area dove sarà visualizzato il grafico
    dcc.Graph(id='scatter-plot')
])

# Callback: funzione che aggiorna il grafico quando cambia la selezione
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),  # Output: grafico da aggiornare
    [dash.dependencies.Input('species-dropdown', 'value')]  # Input: specie selezionata
)
def update_figure(species):
    # Filtra il DataFrame per la specie scelta
    filtered_df = df[df['species'] == species]

    # Crea uno scatter plot con i dati filtrati
    return px.scatter(
        filtered_df,
        x="sepal_width",    # Asse X: larghezza sepalo
        y="sepal_length",   # Asse Y: lunghezza sepalo
        color="species"     # Colore diverso per ogni specie (anche se è solo una)
    )

# Avvio del server Dash
if __name__ == '__main__':
    # Avvia il server sulla porta 8050, accessibile da http://127.0.0.1:8050
    app.run_server(debug=True)
