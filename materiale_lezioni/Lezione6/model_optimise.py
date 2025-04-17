import math

class Model():
    def __init__(self, window=3): 
        self.window = window
    
    
    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    
    def _get_predictions_and_targets(self, data):
        """
        Suddivide i dati, effettua le predizioni e restituisce le liste predetti e reali.
        """
        lunghezza = int(len(data) * 70 / 100)
        fit_data = data[:lunghezza]
        test_data = data[lunghezza:]

        try:
            self.fit(fit_data)
        except Exception as e:
            if not isinstance(e, NotImplementedError):
                raise Exception('Il metodo fit è implementato ma ha sollevato un\'eccezione: {}'.format(e))

        pred = []
        actual = []

        for i in range(len(test_data) - self.window):
            x_input = test_data[i:i + self.window]
            y_true = test_data[i + self.window]
            y_pred = self.predict(x_input)
            pred.append(y_pred)
            actual.append(y_true)

        return pred, actual

    def evaluate(self, data):
        """
        Calcola MAE.
        """
        pred, actual = self._get_predictions_and_targets(data)
        errors = [abs(p - a) for p, a in zip(pred, actual)]
        return sum(errors) / len(errors)

    def evaluate_rmse(self, data):
        """
        Calcola RMSE.
        """
        pred, actual = self._get_predictions_and_targets(data)
        mse = sum((p - a) ** 2 for p, a in zip(pred, actual)) / len(pred)
        return math.sqrt(mse)


class TrendModel(Model):
        
    def validate_data(self,data):     
        if not isinstance(data, list):
                raise TypeError("I dati devono essere di tipo lista, non {}".format(type(data).__name__))
        if len(data) != self.window:
            raise ValueError('Passati {} mesi ma il modello richiede di averne {}'.format(len(data), self.window))       
        for item in data:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("Tutti gli elementi della lista devono essere numeri (int o float) invece questo è {}.".format(item))
    
    def compute_avg_variation(self, data):
        prev_value = None
        variazioni = []
        for item in data:
            if prev_value is not None:
                variazioni.append(item - prev_value)
            prev_value = item
        if len(variazioni)> 0:
            avg_variation = sum(variazioni)/len(variazioni)
        else:
            avg_variation = 0
        return avg_variation
   
    def predict(self, data): 
        self.validate_data(data)
        prediction = data[-1] + self.compute_avg_variation(data)
        return prediction


class FitTrendModel(TrendModel):

    def fit(self, data):
        self.historical_avg_variation = self.compute_avg_variation(data)

    def predict(self, data):
        self.validate_data(data)
        try:
            self.historical_avg_variation 
        except AttributeError:
            raise Exception('Il modello non è fittato!')
        
        prediction = data[-1] + (self.historical_avg_variation + self.compute_avg_variation(data))/2
        return prediction
