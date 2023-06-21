# Copyright (c) 2023 by Sebastian All Rights Reserved */
#    NAME
#      main.py
#    PURPOSE
     
#    NOTES
     
#    AUTHOR
#      Sebastian (kevin1111006@gmail.com)
#    HISTORY
#      Sebastian - Jun 20, 2023: Created.
import NumberPartitionQubo as num
import numpy as np
import matplotlib.pyplot as plt

size_arr=np.arange(20,200,10)
minset=np.zeros(len(size_arr),dtype=int)
index=0
for size in size_arr:
    numbers=num.random_array_generator(size)
    set1, set2 ,minset[index]= num.number_partitioning(numbers)
    print(f"when size={size}:")
    print("array=",numbers)
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Cost:", minset[index],"\n")
    index+=1

#plot_generate
plt.plot(size_arr,minset)
plt.title('Different_size_plot')
plt.xlabel('size of array', fontsize=16)
plt.ylabel('cost', fontsize=16)
plt.grid()
plt.savefig('Different_size_plot.png')
plt.show()