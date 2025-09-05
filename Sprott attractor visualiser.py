# Copywrite 2025 Daniel Nicholson
# If using my code, please credit me

import numpy as np
import matplotlib.pyplot as plt

# Setting up the plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Phase space for Sprott attractor")
ax.set_axis_off()

# Specifying the domain
domainStartxyz = [-0.5, -0.5, -0.5]
domainEndxyz = [0.5, 0.5, 0.5]

# Function that takes in an input position and outputs where that position is
# mapped to under the differential equations (after a certain time step)
def transformCoordinates(x1, y1, z1, step):

    # Calculating the gradient at x1 and y1
    # Here is where we define the differential equations
    a = 2.07
    b = 1.79
    xdot = y1 + a*x1*y1 + x1*z1
    ydot = 1 - b*x1*x1 + y1*z1
    zdot = x1 - x1*x1 - y1*y1

    # Calculating how to scale the gradients to make the line length = step
    scaleFactor = step / np.sqrt(xdot*xdot + ydot*ydot + zdot*zdot)

    # Adding the scaled gradients to calculate the transformed coordinates
    x2 = x1 + scaleFactor*xdot
    y2 = y1 + scaleFactor*ydot
    z2 = z1 + scaleFactor*zdot

    return x2, y2, z2

# Function to create a flow field show how int
def plotFlowField(amount):

    resolution = 500000
    step = 0.0005

    # Spawing specified amount of particles and plotting trajectories
    for i in range(amount):

        # Arrays to store the trajectory
        x = np.zeros(resolution)
        y = np.zeros(resolution)
        z = np.zeros(resolution)

        # Setting the starting conditions
        x[0], y[0], z[0] = 0.63, 0.47, -0.54

        # Computing the trajectory
        for j in range(1, resolution):

            # Interpolating where the particle will be after the step
            x[j], y[j], z[j] = transformCoordinates(x[j-1], y[j-1], z[j-1], step)

        ax.plot3D(x, y, z, c="black", lw=0.4)

# Plotting and displaying the data
plotFlowField(1)
plt.show()