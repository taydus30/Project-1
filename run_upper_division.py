import upper_division as ud

set = ud.Settings()
#file import
set.from_file('DecreasingPopulation.json')
#pass settings to species
species = ud.Species(set)
#species features: species.pop_over_time array, species.generations[x].age, population
sheep_data = ud.Dataset(species)
sheep_data.printTable()
sheep_data.graphAll()
