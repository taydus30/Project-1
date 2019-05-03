#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:00:25 2019
@author: dustyntaylor, tucker, tyrese
"""
from tabulate import tabulate
import matplotlib.pyplot as plt
starting_population = int(input('starting population' ))
mortality_rate = float(input('enter mortalityrate' ))
#Nx = [314, 198, 89, 39, 28, 27, 24, 23, 20, 8, 4, 4, 2, 2, 1, 0]
Nx = []
lx = []
dx = []
qx = []

# Takes user input for the data
Nxdata = eval(input('Enter your Nx data separated by commas (Ex. 1, 2, 3) \n>'))

for i in Nxdata:
    Nx.append(i)

# Calculates the lx values and appends to lx[]
for i in range (len(Nx)):
    lx.append(Nx[i]/Nx[0])

# Calculates the dx values and appends to dx[]
for i in range(len(lx)-1):
    dx.append(lx[i]-lx[i+1])

# Calculates the qx values and appends to qx[]
for i in range (len(dx)):
    qx.append(dx[i]/lx[i])

# Creates a list of lists for the tabluate function out of the Nx,lx,dx,qx lists
Table = []

for i in range(len(Nx)):
    try:
        Table.append([Nx[i],round(lx[i], 3),round(dx[i],3),round(qx[i],3)])
    except IndexError:
        Table.append([Nx[i], round(lx[i],3), '...', '...'])

# Adds whitespace
print('\n\n\n')

# Creates and Prints the table of values
print(tabulate(Table, headers = ['Nx', 'lx', 'dx', 'qx']))

# This function creates a list of valuse for your x-axis based on the data you
# want to graph
def xaxis (data):
    global x
    x = []

    for i in range(len(data)):
        x.append(i)

# This is how you create and print the graph
xaxis(Nx)
plt.plot(x, Nx)
plt.xlabel('X')
plt.ylabel('Nx Values')
plt.show()

xaxis(lx)
plt.plot(x, lx)
plt.xlabel('X')
plt.ylabel('lx Values')
plt.show()

xaxis(dx)
plt.plot(x, dx)
plt.xlabel('X')
plt.ylabel('dx Values')
plt.show()

xaxis(qx)
plt.plot(x, qx)
plt.xlabel('X')
plt.ylabel('qx Values')
plt.show()
