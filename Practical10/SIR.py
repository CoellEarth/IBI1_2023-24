import numpy as np
import matplotlib.pyplot as plt

N_infected = 1
N_susceptible = 9999
N_recovered = 0
N_total = 10000
beta = 0.3
gamma = 0.05

sus_number_info = [N_susceptible]
infected_number_info = [N_infected]
recovered_number_info = [N_recovered]

for time_points in range(1000):
    infection_proportion = N_infected / N_total
    infection_rate = beta * infection_proportion
    recovery_rate = gamma
    
    new_infections = np.random.choice([True, False], size=N_susceptible, p=[infection_rate, 1 - infection_rate])
    N_infected += np.sum(new_infections)
    N_susceptible -= np.sum(new_infections)
    
    new_recoveries = np.random.choice([True, False], size=N_infected, p=[recovery_rate, 1 - recovery_rate])
    N_recovered += np.sum(new_recoveries)
    N_infected -= np.sum(new_recoveries)

    sus_number_info.append(N_susceptible)
    infected_number_info.append(N_infected)
    recovered_number_info.append(N_recovered)


plt.plot(sus_number_info, label='Susceptible')
plt.plot(infected_number_info, label='Infected')
plt.plot(recovered_number_info, label='Recovered')
plt.title("SIR Model")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend()
plt.show()

#PSEUDOCODE
# Initialize variables:
#     N_infected = 1
#     N_susceptible = 9999
#     N_recovered = 0
#     N_total = 10000
#     beta = 0.3
#     gamma = 0.05
#     sus_number_info = list containing N_susceptible
#     infected_number_info = list containing N_infected
#     recovered_number_info = list containing N_recovered
#
# For time_points from 0 to 999:
#     Calculate infection_proportion = N_infected / N_total
#     Calculate infection_rate = beta * infection_proportion
#     Calculate recovery_rate = gamma
#
#     Generate a random boolean array of size N_susceptible with True probability = infection_rate
#     Count the number of True values in the array
#     Add the count to N_infected
#     Subtract the count from N_susceptible
#
#     Generate a random boolean array of size N_infected with True probability = recovery_rate
#     Count the number of True values in the array
#     Add the count to N_recovered
#     Subtract the count from N_infected
#
#     Append the updated values of N_susceptible, N_infected, and N_recovered to their respective lists
#
# Plot the lists sus_number_info, infected_number_info, and recovered_number_info as line plots
# Set the plot title to "SIR Model"
# Set the x-axis label to "Time"
# Set the y-axis label to "Number of People"
# Add a legend to the plot
# Display the plot
