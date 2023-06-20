import NumberPartition as num
import numpy as np
import matplotlib.pyplot as plt

set1=np.zeros((1000,20),dtype=int)
set2=np.zeros((1000,20),dtype=int)
minset=np.zeros(1000,dtype=int)
cool = np.linspace(0.3,0.9999,1000)
index=0
numbers = [443, 552, 217, 319, 3, 708, 756, 342, 669, 133, 984, 405, 718, 105, 553, 66, 877, 705, 924, 654]
for cooling in cool:
    set1[index], set2[index] ,minset[index]= num.number_partitioning(numbers, initial_temperature=62000,cooling_rate=cooling, max_iterations=100000000)
    print(f"when cooling_rate={cooling}:")
    print("array=",numbers)
    print("Set 1:", set1[index])
    print("Set 2:", set2[index])
    print("Cost:", minset[index],"\n")
    index+=1

#plot_generate
plt.plot(cool,minset)
plt.title('DiffInitemprature_plot')
plt.xlabel('Initial temprature', fontsize=16)
plt.ylabel('cost', fontsize=16)
plt.grid()
plt.savefig('DiffCoolingRate_plot.png')
plt.show()