##记得写Pseudo Code！！！！！

import numpy as np
import matplotlib.pyplot as plt

N_infected = 1
N_susceptible = 9999
N_recovered = 0
N_total = 10000
beta = 0.3
gamma = 0.05

infection_proportion = N_infected / N_total
infection_rate = beta * infection_proportion

sus_number_info = np.array([N_susceptible])
infected_number_info = np.array([N_infected])
recovered_number_info = np.array([N_recovered])

for time_point in range(1000):
    new_infections = np.random.choice(range(int(N_susceptible+1)),1,p=None)
    N_infected += new_infections

    new_recoveries = np.random.choice(range(int(N_infected+1)),1,p=None)
    N_recovered += new_recoveries
    N_infected -= new_recoveries

    N_susceptible=N_total-N_infected-N_recovered


    sus_number_info = np.append(sus_number_info, N_susceptible)
    infected_number_info = np.append(infected_number_info, N_infected)
    recovered_number_info = np.append(recovered_number_info, N_recovered)


plt.figure()
plt.plot(sus_number_info, label='Susceptible')
plt.plot(infected_number_info, label='Infected')
plt.plot(recovered_number_info, label='Recovered')
plt.title("SIR Model")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend()
plt.show()
plt.clf()
