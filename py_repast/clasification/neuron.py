#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

class Neuron():
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be positive integer')
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b


    @property
    def A(self):
        return self.__A

    def forward_prop(self, X):
        Z = np.matmul(self.__W, X) + self.__b
        a = 1 / (1 + np.exp(-Z))
        self.__A = a
        return self.__A

    def cost(self, Y, A):
        m = - (1 / Y.shape[1])
        C = m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return C

    def evaluate(self, X, Y):
        a = self.forward_prop(X)
        evaluate = np.where(a >= 0.5, 1, 0)
        c = self.cost(Y, a)
        return evaluate, c

    def gradient_descent(self, X, Y, A, alpha=0.05):
        m = Y.shape[1]
        dw = np.matmul(A - Y, X.T) / m
        db = np.sum(A - Y) / m
        self.__W = self.__W - alpha * dw
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose == True or graph == True:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if step < 0 or step > iterations:
                raise ValueError('step must be positive and <= iterations')
        for i in range(iterations):
            self.__A = self.forward_prop(X)
            y, c = self.evaluate(X, Y)
            if i < iterations:
                self.gradient_descent(X, Y, self.__A)
            if verbose == True:
                if i % step == 0:
                    print('Cost after {} iterations: {}'.format(i, c))
        if graph == True:
            plt.plot(i, c)
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.title('Training Cost')
            plt.show()
        return y, c

