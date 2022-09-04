#!/usr/bin/env python3
import numpy as np

class NeuralNetwork():
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be positive integer')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nx < 1:
            raise ValueError('nodes must be positive integer')
        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros(nodes).reshape(nodes,1)
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0


    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1


    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2


    def forward_prop(self, X):
        Z_1 = np.matmul(self.__W1, X) + self.__b1
        A_1 = 1 / (1 + np.exp(-Z_1))
        self.__A1 = A_1
        Z_2 = np.matmul(self.__W2, self.__A1) + self.__b2
        A_2 = 1 / (1 + np.exp(-Z_2))
        self.__A2 = A_2
        return self.__A1, self.__A2

    def cost(self, Y, A):
        m = - (1 / Y.shape[1])
        C = m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A))
        return C

    def evaluate(self, X, Y):
        _, a = self.forward_prop(X)
        evaluate = np.where(a >= 0.5, 1, 0)
        c = self.cost(Y, a)
        return evaluate, c

