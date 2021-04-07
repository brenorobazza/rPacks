from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


class Polinomial:
    def __init__(self, file, x_axis, y_axis, order=2, *args, **kwargs):
        self.data = self.read_file(file, x_axis)
        self.x = self.fix_decimal(self.data[x_axis].values)
        self.y = self.fix_decimal(self.data[y_axis].values)

        fit = np.polyfit(self.x,self.y,order)
        self.model = np.poly1d(fit)
        self.r_squared = r2_score(self.y, self.model(self.x))
    
    @staticmethod
    def read_file(file, x_axis):
        for separator in [',', ';']:
            try:
                data = pd.read_csv(file, sep=separator)
                test_column = data[x_axis].values
                return data
            except:
                print("erro utilizando %s" %separator)
        return data
    
    @staticmethod
    def fix_decimal(values):
        new_array = []
        for item in values:
            if isinstance(item, str):
                f = item.replace(',', '.')
                item = float(f)
            new_array.append(item)
        nparray = np.array(new_array)
        return nparray
    
    def predict(self, values):
        x = values
        try:
            return self.model(x)
        except Exception as e:
            raise e
    
    def plot(self, filename='plot'):
        plt.clf()
        plt.scatter(self.x,self.y)
        plt.plot(self.x, self.predict(self.x), label="Accuracy = %.2f%%" %(self.r_squared * 100))
        plt.legend()
        plt.savefig(filename)


class Linear:
    def __init__(self, file, x_axis, y_axis, *args, **kwargs):
        self.data = self.read_file(file, x_axis)
        self.x = self.fix_decimal(self.data[x_axis].values)
        m = len(self.x)

        self.x = self.x.reshape((m,1))
        self.y = self.fix_decimal(self.data[y_axis].values)

        self.model = LinearRegression().fit(self.x,self.y)
        self.r_squared = self.model.score(self.x,self.y)
        self.slope = self.model.coef_
        self.intercept = self.model.intercept_


    @staticmethod
    def read_file(file, x_axis):
        for separator in [',', ';']:
            try:
                data = pd.read_csv(file, sep=separator)
                test_column = data[x_axis].values
                return data
            except:
                print("erro utilizando %s" %separator)
        return data
    
    @staticmethod
    def fix_decimal(values):
        new_array = []
        for item in values:
            if isinstance(item, str):
                f = item.replace(',', '.')
                item = float(f)
            new_array.append(item)
        nparray = np.array(new_array)
        return nparray

    def predict(self, values):
        x = values
        try:
            return self.model.predict(x)
        except:
            pass
        try:
            return self.model.predict([[x]])
        except:
            raise Exception('Precisa ser um valor único ou uma array bidimensional [[a], [b], [c], ...]')
    
    def plot(self, filename='plot'):
        plt.clf()
        plt.scatter(self.x,self.y)
        plt.plot(self.x, self.predict(self.x), label="Accuracy = %.2f%%" % (self.r_squared * 100))
        plt.legend()
        plt.savefig(filename)


        
    

    
    
