from model import TrendModel, FitTrendModel
from importa_dati import NumericalCSVFile
import matplotlib.pyplot as plt

# --- CARICAMENTO DATI ---

# Creo un'istanza della classe NumericalCSVFile con il nome del file 'shampoo_sales.csv'
shampoofile = NumericalCSVFile('../dati/shampoo_sales.csv')

# Ottengo i dati dal file (lista di tuple [data, valore])
lista_dati = shampoofile.get_data()

# Separazione delle date e dei valori in due liste distinte
dates = [item[0] for item in lista_dati]
values = [item[1] for item in lista_dati]


# --- PREPARAZIONE DATI ---

# Dati usati per addestrare il modello FitTrendModel (fino alla 24° osservazione)
fit_values = values[:24]

# Dati di test (dal 25° elemento in poi)
test_values = values[24:]

# Dati da cui iniziare a prevedere per TrendModel (ultimi 3 del fit + test)
data = values[21:]

window = 2  # Finestra mobile per il modello

# --- MODELLO TREND SEMPLICE (senza fit) ---

trend_model = TrendModel(window=2)
pred_data = [values[23]]  # primo punto noto da cui parte la previsione

# Ciclo di previsione per TrendModel
for i, item in enumerate(data[:]):
    if i >= window:
        prediction = trend_model.predict(data[i-window:i])
        print(data[i-window:i])  # (debug) stampa finestra usata per predire
        pred_data.append(prediction)

# --- MODELLO FITTREND (con fit) ---

fit_trend_model = FitTrendModel(window=2)
fit_pred_data = []

# Prime due osservazioni reali passate al modello per iniziare a predire
predicted_values = data[:window]

# Fase di "fit" con i dati storici
fit_trend_model.fit(fit_values)

# Previsioni passo-passo su test_values
for i in range(len(test_values) - window):
    prediction = fit_trend_model.predict(predicted_values)
    fit_pred_data.append(prediction)
    del predicted_values[0]  # rimuove il più vecchio
    predicted_values.append(test_values[i + window])  # aggiunge il nuovo valore reale

# --- VALUTAZIONE MAE (già fornito da Model.evaluate) ---

mae_trend = trend_model.evaluate(values)
mae_fit_trend = fit_trend_model.evaluate(values)


# --- VALUTAZIONE RMSE (funzione personalizzata) ---

def evaluate_rmse(model, data):
    # Suddivide in fit e test set (70%-30%)
    lunghezza = int(len(data) * 70 / 100)
    fit_data = data[:lunghezza]
    test_data = data[lunghezza:]

    # Fit del modello (se implementato)
    try:
        model.fit(fit_data)
    except:
        pass  # Se non implementato (TrendModel), ignora

    pred = []
    actual = []

    # Predizioni e raccolta valori reali
    for i in range(len(test_data) - model.window):
        x_input = test_data[i:i + model.window]
        y_true = test_data[i + model.window]
        y_pred = model.predict(x_input)
        pred.append(y_pred)
        actual.append(y_true)

    # Calcolo RMSE
    squared_errors = [(pred[i] - actual[i]) ** 2 for i in range(len(pred))]
    rmse = (sum(squared_errors) / len(squared_errors)) ** 0.5
    return rmse

# Calcolo RMSE per entrambi i modelli
rmse_trend = evaluate_rmse(trend_model, values)
rmse_fit = evaluate_rmse(fit_trend_model, values)

# Stampa risultati
print(f"TrendModel → MAE: {mae_trend:.2f}, RMSE: {rmse_trend:.2f}")
print(f"FitTrendModel → MAE: {mae_fit_trend:.2f}, RMSE: {rmse_fit:.2f}")


# --- PLOT DEI RISULTATI ---

x = list(range(len(values)))  # asse x per tutti i dati reali
x_pred = list(range(23, 23 + len(pred_data)))  # asse x per previsioni TrendModel
x_fit = list(range(26, 26 + len(fit_pred_data)))  # asse x per previsioni FitTrendModel

plt.figure(figsize=(12, 6))
plt.plot(x, values, marker='o', linestyle='-', label='Vendite di shampoo')
plt.plot(x[24:], test_values, color='lightblue', marker='o', linestyle='-', label='Dati di test')
plt.plot(x_pred, pred_data, color='red', marker='o', linestyle='-', label='Previsioni senza fit (TrendModel)')
plt.plot(x_fit, fit_pred_data, color='orange', marker='o', linestyle='-', label='Previsioni con fit (FitTrendModel)')
plt.title('Vendite di Shampoo nel tempo')
plt.xlabel('Date')
plt.ylabel('Vendite')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
