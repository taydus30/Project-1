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

    def output(self, data, title, xlable, ylable):
        #show pyplot
        x = self.xaxis(data)
        plt.plot(x, data)
        plt.title(title)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.show()

    def calcLx(self):
        self.Lx = []

        for i in range (len(self.Nx)):
            self.Lx.append(self.Nx[i]/self.Nx[0])

    def calcDx(self):
        self.Dx = []

        for i in range(len(self.Lx)-1):
            self.Dx.append(self.Lx[i]-self.Lx[i+1])

    def calcQx(self):
        self.Qx = []

        for i in range (len(self.Dx)):
            self.Qx.append(self.Dx[i]/self.Lx[i])

    def printTable(self):
        Table = []

        for i in range(len(Nx)):
            try:
                Table.append([self.Nx[i],round(self.Lx[i], 3),round(self.Dx[i],3),round(self.Qx[i],3)])
            except IndexError:
                Table.append([self.Nx[i], round(self.Lx[i],3), '...', '...'])

        print('\n\n\n')

        print(tabulate(Table, headers = ['Nx', 'lx', 'dx', 'qx']))

    def graphAll(self):
        self.xaxis(self.Nx)
        self.output(self.Nx, 'Population Over Time', 'Population', 'Years')

        self.xaxis(self.Lx)
        self.output(self.Lx, 'Lx Graph', 'Lx Values', 'Years')

        self.xaxis(self.Dx)
        self.output(self.Dx, 'Dx Graph', 'Dx Values', 'Years')

        self.xaxis(self.Qx)
        self.output(self.Qx, 'Qx Graph', 'Qx values', 'Years')

mydataset = Dataset()
mydataset.output(mydataset.Nx, 'Nx')

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
