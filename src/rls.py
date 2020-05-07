import numpy as np


class RLS:
    def __init__(self, num_features, nu):
        self.beta = np.zeros(num_features)
        v0 = 10  ## initialization covariance
        self.V = np.diag(np.zeros(num_features) + v0)  ## initial covariance matrix for model 1
        self.nu = nu  # forgetting factor

    def fit_one(self, x, y):
        x = np.array(x)
        y = np.array(y)
        self.V = np.array(self.V)
        self.beta = np.array(self.beta)
        x.shape = (1, len(x))
        self.beta.shape = (1, x.shape[1])
        self.V = 1.0 / self.nu * (self.V - self.V.dot(x.T).dot(x).dot(self.V) / (1.0 + float(x.dot(self.V).dot(x.T))))
        alpha = self.V.dot(x.T)
        y_hat = x.dot(self.beta.T)
        err = y - y_hat
        self.beta = self.beta + alpha.T * err

    def predict_one(self, x):
        return np.atleast_1d(x.dot(self.beta.T))
