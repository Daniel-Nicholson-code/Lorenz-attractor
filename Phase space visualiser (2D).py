# Copywrite 2025 Daniel Nicholson
# If using my code, please credit me

import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
plt.title("Phase space for Van der Pol oscillator")
plt.xlabel("x")
plt.ylabel("y")

# Specifying the domain
domainStartxy = [-5, -5]
domainEndxy = [5, 5]

# Function that takes in an input position and outputs where that position is
# mapped to under the differential equations (after a certain time step)
def transformCoordinates(x1, y1, step):

    # Calculating the gradient at x1 and y1
    # Here is where we define the differential equations
    mu = 1
    xdot = mu*( x1 - x1*x1*x1/3 - y1 )
    ydot = x1/mu

    # Calculating how to scale the gradients to make the line length = step
    scaleFactor = step / np.sqrt(xdot*xdot + ydot*ydot)

    # Adding the scaled gradients to calculate the transformed coordinates
    x2 = x1 + scaleFactor*xdot
    y2 = y1 + scaleFactor*ydot

    return x2, y2

# Function to create a vector field showing how the gradient changes in the
# specified domain
def plotVectorField():

    resolution = [40, 40]
    vectorLength = 0.5

    # Creating a grid
    xGrid = np.linspace(domainStartxy[0], domainEndxy[0], resolution[0])
    yGrid = np.linspace(domainStartxy[1], domainEndxy[1], resolution[1])

    # Iterating on the grid and plotting the corresponding vector for each
    # coordinate
    for i in xGrid:
        for j in yGrid:

            # Calculating the start and end coordinate for the vecot
            x1, y1 = i, j
            x2, y2 = transformCoordinates(x1, y1, vectorLength)

            plt.plot([x1, x2], [y1, y2], c="black", lw=0.4)

# Function to create a flow field show how int
def plotFlowField(amount):

    resolution = 200
    step = 0.1

    # Spawing specified amount of particles and plotting trajectories
    for i in range(amount):

        # Arrays to store the trajectory
        x = np.zeros(resolution)
        y = np.zeros(resolution)

        # Setting the starting conditions to be a random point within the domain
        x[0] = domainStartxy[0] + (domainEndxy[0] - domainStartxy[0])*np.random.rand()
        y[0] = domainStartxy[1] + (domainEndxy[1] - domainStartxy[1])*np.random.rand()

        # Computing the trajectory
        for j in range(1, resolution):

            # Interpolating where the particle will be after the step
            x[j], y[j] = transformCoordinates(x[j-1], y[j-1], step)

        plt.plot(x, y, c="black", lw=0.6)

# Plotting and displaying the data
plotVectorField()
plotFlowField(100)

plt.show()

