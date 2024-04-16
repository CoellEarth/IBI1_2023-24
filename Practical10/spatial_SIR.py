import numpy as np
import matplotlib.pyplot as plt

beta=0.3
gamma=0.05

population = np. zeros((100,100))
outbreak = np. random . choice (range(100) ,2)
population[outbreak[0],outbreak[1]]=1

time_points_to_plot = [1,50,100,150,175,200,250,300,350,400,600]

for time_points in range(1000):
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        if population[x,y]==1:
            population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]

    if time_points + 1 in time_points_to_plot:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"population at time point {time_points + 1}")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

##PSEUDOCODE
# Import necessary libraries
# Import the numpy library as np
# Import the pyplot module from the matplotlib library as plt

# Define parameters
# Set beta to 0.3
# Set gamma to 0.05

# Create the population grid
# Create a 2D array named population filled with zeros, with dimensions (100, 100)

# Introduce an initial outbreak
# Generate a random outbreak location (x, y) within the population grid
# Set the population at the outbreak location to 1 (infected)

# Define time points to plot
# Create a list named time_points_to_plot containing specific time points to plot, e.g., [1, 50, 100, ...]

# Simulate the spread of infection over time
# Iterate over each time point from 0 to 999:
    # Spread infection to neighboring cells
    # Find the indices of infected cells in the population grid
    # Iterate over each infected cell index:
        # Extract the x and y coordinates of the infected cell
        # Iterate over each neighboring cell of the infected cell:
            # Iterate over the x and y coordinates of neighboring cells:
                # If the neighboring cell is not the infected cell itself:
                    # If the neighboring cell is within the population grid boundaries:
                        # If the neighboring cell is not already infected:
                            # Infect the neighboring cell with probability beta
                            # Update the population grid with the infected status of the neighboring cell
        
        # Apply recovery process
        # If the current cell is still infected:
            # Recover the cell with probability gamma
            # Update the population grid with the recovered status of the cell

    # Plot population grid at specific time points
    # If the current time point plus one is in the time_points_to_plot list:
        # Create a new figure with specified size and resolution
        # Display the population grid using imshow, with 'viridis' colormap and nearest-neighbor interpolation
        # Add a title to the plot indicating the time point
        # Label the x and y axes
        # Show the plot

# End of simulation

