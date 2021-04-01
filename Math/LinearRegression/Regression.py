from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

class Regression:

    def __init__(self, file, x_axis, y_axis, *args, **kwargs):
        separator = kwargs.get('separator')
        if not separator:
            separator = ','
            
        self.data = pd.read_csv(file, sep=separator)
        self.x_axis = x_axis
        self.y_axis = y_axis
        
        try:
            X = self.fixDecimal(self.data[x_axis].values)
        except:
            raise Exception("Ocorreu um erro, talvez tenha utilizado o separador errado\nSeparador utilizado: '%s'\n Regression(arquivo, eixo x, eixo y, <separator=',|;'>)" % separator)
        m = len(X)
        self.X = X.reshape((m,1))
        self.Y = self.fixDecimal(self.data[y_axis].values)
        self.regression = LinearRegression().fit(self.X, self.Y)
        self.r_squared = self.regression.score(self.X, self.Y)
        self.slope = self.regression.coef_
        self.intercept = self.regression.intercept_

    @staticmethod
    def fixDecimal(values):
        new_array = []
        for item in values:
            if isinstance(item, str):
                f = item.replace(',', '.')
                item = float(f)
            new_array.append(item)
        nparray = np.array(new_array)
        return nparray
  

    # predict Y from X values
    def predict(self, values):
        x = values
        try:
            return self.regression.predict(x)
        except:
            raise Exception('Precisa ser uma array bidimensional [[a], [b], [c], ...]')

    
    def r_squared(self):
        return self.regression.score(X, Y)
    
    def plot(self, filename='result.png'):
        plt.xlabel(self.x_axis)
        plt.ylabel(self.y_axis)
        plt.scatter(self.X, self.Y)
        plt.plot(self.X, self.intercept+self.slope*self.X)
        plt.savefig(filename)

    def curve(self):
        return ("y = %(intercept)f + %(slope)f * X" % {'intercept': self.intercept, 'slope': self.slope})


