import matplotlib.pyplot as plt
import os.path
import json

class Dataset():

    def __init__(self, nx):
        self.Nx = nx

        self.Lx = None
        self.Dx = None
        self.Qx = None

    def xaxis (self, data):
        x = []

        for i in range(len(data)):
            x.append(i)

        return x

    def output(self, data, title):
        #show pyplot
        x = self.xaxis(data)
        plt.plot(x, data)
        plt.xlabel('X')
        plt.ylabel(title + ' Values')
        plt.show()

class InputFile():

    def __init__(self, file_name):
        f = None
        if(os.path.isfile(file_name)):
            f = json.load(file_name)
        else:
            string(input('Improper File Path!'))

class Generation():

    def __init__(self):
        self.age = 0;
        self.population = 0;

    def update(self):
        self.age += 1
