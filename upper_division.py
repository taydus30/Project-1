import matplotlib.pyplot as plt
import os.path
import json
from tabulate import tabulate

class Dataset():

    def __init__(self, species):
        """ The Dataset is a collection of calculated data and visualization
        -----
        nx : int array
            uses an array of population over data
        """
        self.Nx = species.pop_over_time
        self.species_name = species.name
        self.calcLx()
        self.calcDx()
        self.calcQx()

    def xaxis (self, data):
        """ Calculates an array for the xaxis of the graphs
        -----
        data : int array
            uses and array of data
        """
        x = []

        for i in range(len(data)):
            x.append(i)

        return x

    def output(self, data, title, ylable, xlable):
        """ Creates and shows a graph of given data
        -----
        data : int array
            uses an array of data
        title : String
            Used as the title of the graph
        xlable : String
            Used as the lable for the xaxis
        ylable : String
            used as the lable for the y axis
        """
        #show pyplot
        x = self.xaxis(data)
        plt.plot(x, data)
        plt.title(title + ": " + self.species_name)
        plt.xlabel(xlable)
        plt.ylabel(ylable)
        plt.show()

    def calcLx(self):
        """ Calculates the Lx values and creates an array
        """
        self.Lx = []

        for i in range (len(self.Nx)):
            self.Lx.append(self.Nx[i]/self.Nx[0])

    def calcDx(self):
        """ Calculates the Dx values and creates an array
        """
        self.Dx = []

        for i in range(len(self.Lx)-1):
            self.Dx.append(self.Lx[i]-self.Lx[i+1])

    def calcQx(self):
        """ Calculates the Qx values and creates an array
        """
        self.Qx = []

        for i in range (len(self.Dx)):
            self.Qx.append(self.Dx[i]/self.Lx[i])

    def printTable(self):
        """ Formulates and prints the data in a nice table
        """
        Table = []

        for i in range(len(self.Nx)):
            try:
                Table.append([self.Nx[i],round(self.Lx[i], 3),round(self.Dx[i],3),round(self.Qx[i],3)])
            except IndexError:
                Table.append([self.Nx[i], round(self.Lx[i],3), '...', '...'])

        print('\n\n\n')

        print(tabulate(Table, headers = ['Nx', 'lx', 'dx', 'qx']))

    def graphAll(self):
        """ Graphs all of the Nx, Lx, Dx, Qx data
        """
        self.xaxis(self.Nx)
        self.output(self.Nx, 'Population Over Time', 'Population', 'Years')

        self.xaxis(self.Lx)
        self.output(self.Lx, 'Lx Graph', 'Lx Values', 'Years')

        self.xaxis(self.Dx)
        self.output(self.Dx, 'Dx Graph', 'Dx Values', 'Years')

        self.xaxis(self.Qx)
        self.output(self.Qx, 'Qx Graph', 'Qx values', 'Years')

class Settings():

    def __init__(self):
        """Holds information used by Generations and Species
        -----

        """
        self.json = None
        self.name = None
        self.starting_population = None
        self.iterations = None
        self.death_rates = None
        self.fecundity = None

    def from_file(self, file_name = ""):
        """ Reads Json file and sets properties according
        -----
        file_name : string
            file path of your json file
        """
        f = None
        if(os.path.isfile(file_name)):
            file = open(file_name)
            self.json = json.load(file)
            self.starting_population = self.json['starting_population']
            self.iterations = self.json['iterations']
            self.death_rates = self.json['death_rates']
            self.fecundity = self.json['fecundity']
            self.name = self.json['name']
        else:
            print('Improper File Path!')

    def valid(self):
        return(self.json != None)

class Generation():

    def __init__(self, starting_population):
        """Contains one generation of a creature and methods that update it
        -----
        starting_population : int
        """
        self.age = 0;
        self.population = starting_population;

    def update(self, death_rates, fecundity):
        """Reads Json file and sets properties accordingly
        -----
        death_rates : float array
            from Settings object
        fecundity : float array
            from Settings object
        """
        upper_d = len(death_rates) -1
        upper_f = len(fecundity) - 1
        new_pop = 0
        if(self.age < upper_f):
            new_pop = self.population / 2 * fecundity[self.age]
        else:
            new_pop = self.population / 2 * fecundity[-1]
        if(self.age < upper_d):
            self.population = self.population * death_rates[self.age]
        else:
            self.population = self.population * death_rates[-1]
        self.age += 1
        return(Generation(new_pop))

class Species():
    def __init__(self, settings):
        """Container for multiple generations of a population
        -------
        settings : Settings
            Settings object containing needed json
        """

        self.pop_over_time = []
        self.name = settings.name
        self.generations = [Generation(settings.starting_population)]
        for i in range(settings.iterations):
            total = 0
            for g in self.generations:
                total += g.population
            self.pop_over_time.append(total)
            for p in range(len(self.generations)):
                new_pop = self.generations[p].update(settings.death_rates, settings.fecundity)
                if(new_pop.population > 0):
                    self.generations.append(new_pop)
