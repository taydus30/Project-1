import matplotlib.pyplot as plt

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

mydataset = Dataset()
mydataset.output(mydataset.Nx, 'Nx')
