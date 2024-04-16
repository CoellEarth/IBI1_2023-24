import numpy as np
import matplotlib.pyplot as plt

##act 1
N_infected = 1
N_susceptible = 9999
N_recovered = 0
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info = [N_infected]

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

    infected_number_info.append(N_infected)

##act 2
N_infected = 1
N_susceptible = 8999
N_recovered = 1000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_10 = [N_infected]

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

    infected_number_info_10.append(N_infected)

##act 3
N_infected = 1
N_susceptible = 7999
N_recovered = 2000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_20 = [N_infected]

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

    infected_number_info_20.append(N_infected)

##act 3
N_infected = 1
N_susceptible = 6999
N_recovered = 3000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_30 = [N_infected]

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

    infected_number_info_30.append(N_infected)

##act 4
N_infected = 1
N_susceptible = 5999
N_recovered = 4000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_40 = [N_infected]

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

    infected_number_info_40.append(N_infected)

##act 5
N_infected = 1
N_susceptible = 4999
N_recovered = 5000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_50 = [N_infected]

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

    infected_number_info_50.append(N_infected)

##act 6
N_infected = 1
N_susceptible = 3999
N_recovered = 6000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_60 = [N_infected]

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

    infected_number_info_60.append(N_infected)

##act 7
N_infected = 1
N_susceptible = 2999
N_recovered = 7000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_70 = [N_infected]

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

    infected_number_info_70.append(N_infected)

##act 8
N_infected = 1
N_susceptible = 1999
N_recovered = 8000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_80 = [N_infected]

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

    infected_number_info_80.append(N_infected)

##act 9
N_infected = 1
N_susceptible = 999
N_recovered = 9000
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_90 = [N_infected]

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

    infected_number_info_90.append(N_infected)

##act 10
N_infected = 1
N_susceptible = 0
N_recovered = 9999
N_total = 10000
beta = 0.3
gamma = 0.05

infected_number_info_100 = [N_infected]

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

    infected_number_info_100.append(N_infected)



plt.plot(infected_number_info, label='0%')
plt.plot(infected_number_info_10, label='10%')
plt.plot(infected_number_info_20, label='20%')
plt.plot(infected_number_info_30, label='30%')
plt.plot(infected_number_info_40, label='40%')
plt.plot(infected_number_info_50, label='50%')
plt.plot(infected_number_info_60, label='60%')
plt.plot(infected_number_info_70, label='70%')
plt.plot(infected_number_info_80, label='80%')
plt.plot(infected_number_info_90, label='90%')
plt.plot(infected_number_info_100, label='100%')
plt.title("SIR Model with different vaccination rates")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend()
plt.show()

