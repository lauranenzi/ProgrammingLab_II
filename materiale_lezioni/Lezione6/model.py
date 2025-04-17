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
    
    def evaluate(self,data):
        
        lunghezza = int(len(data)*70/100)
        fit_data = data[:lunghezza]
        test_data = data[lunghezza:]

        try:
            self.fit(fit_data)
        except Exception as e:
            if isinstance(e,NotImplementedError):
                pass
            else:
                raise Exception('Il metodo fit è implementato ma' +
        'ha sollevato una eccezione {}'.format(e)) 

        errors = []
        for i in range(len(test_data)-self.window):
            valore_predetto = self.predict(test_data[i:i+self.window])
            errors.append(round(abs(valore_predetto-test_data[self.window + i]),10))
        mae_error = sum(errors)/len(errors)
        return mae_error

    def evaluate_rmse(self, data):
        """
        Calcola RMSE tra i valori predetti e quelli reali.
        """
        lunghezza = int(len(data) * 70 / 100)
        fit_data = data[:lunghezza]
        test_data = data[lunghezza:]

        try:
            self.fit(fit_data)
        except Exception as e:
            if isinstance(e, NotImplementedError):
                pass
            else:
                raise Exception('Il metodo fit è implementato ma ha sollevato una eccezione: {}'.format(e)) 

        pred = []
        actual = []

        for i in range(len(test_data) - self.window):
            x_input = test_data[i:i + self.window]
            y_true = test_data[i + self.window]
            y_pred = self.predict(x_input)
            pred.append(y_pred)
            actual.append(y_true)

        mse = sum((pred[i] - actual[i]) ** 2 for i in range(len(pred))) / len(pred)
        rmse = math.sqrt(mse)
        return rmse


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
