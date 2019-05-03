import matplotlib.pyplot as plt

class Dataset():

    def __init__(self, nx):
        self.Nx = nx

        self.Lx = None
        self.Dx = None
        self.Qx = None

    def output(self):
        #show pyplot
        print('oout')
