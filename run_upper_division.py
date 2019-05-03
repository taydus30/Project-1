"""
Creators: Dustyn, Tucker
Date Created: May 2nd 2019
"""

import upper_division as ud

set = ud.Settings()
#file import
set.from_file('IncreasingPopulation.json')
#pass settings to species
species = ud.Species(set)
#species features: species.pop_over_time array, species.generations[x].age, population
sheep_data = ud.Dataset(species)
sheep_data.printTable()
sheep_data.graphAll()
