# Copyright (c) 2023 by Sebastian All Rights Reserved */
#    NAME
#      main.py
#    PURPOSE
     
#    NOTES
     
#    AUTHOR
#      Sebastian (kevin1111006@gmail.com)
#    HISTORY
#      Sebastian - Jun 20, 2023: Created.
import NumberPartition as num
import numpy as np
import matplotlib.pyplot as plt

set1=np.zeros((100,20),dtype=int)
set2=np.zeros((100,20),dtype=int)
minset=np.zeros(100,dtype=int)
index=0
numbers = [443, 552, 217, 319, 3, 708, 756, 342, 669, 133, 984, 405, 718, 105, 553, 66, 877, 705, 924, 654]
t = np.linspace(100,101000,100)
for temperature in t:
    set1[index], set2[index] ,minset[index]= num.number_partitioning(numbers, initial_temperature=temperature,cooling_rate=0.9999, max_iterations=100000000)
    # print(f"when T={temperature}:")
    # print("array=",numbers)
    # print("Set 1:", set1[index])
    # print("Set 2:", set2[index])
    # print("Cost:", minset[index],"\n")
    index+=1

#plot_generate
plt.plot(t,minset)
plt.title('DiffInitemprature_plot & coolingrate=0.99')
plt.xlabel('Initial temprature', fontsize=16)
plt.ylabel('cost', fontsize=16)
plt.grid()
plt.savefig('DiffInitemprature_plot & coolingrate=0.99.png')
plt.show()