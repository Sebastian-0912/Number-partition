# Copyright (c) 2023 by Sebastian All Rights Reserved */
#    NAME
#      NumberPartitionQubo.py
#    PURPOSE
     
#    NOTES
     
#    AUTHOR
#      Sebastian (kevin1111006@gmail.com)
#    HISTORY
#      Sebastian - Jun 21, 2023: Created.

import random
import numpy as np

# 生成隨機整數列表
def random_array_generator(size):
    random.seed(1)
    random_list = [random.randint(1, 1000) for _ in range(size)]
    return random_list

#QUBO generator
def QUBO(numbers):
    size=len(numbers)
    constant=sum(numbers)
    qubo=np.zeros((size,size),dtype=np.int64)
    for i in range(0,size):
        for j in range(0,size):
            if i==j:
                qubo[i][j]=numbers[i]*(numbers[i]-constant)
            else:
                qubo[i][j]=numbers[i]*numbers[j]
    return qubo

# 定義成本函數
def cost_function(constant,qubo,x):# x is configration
    cost=constant**2 + 4*(x.dot(qubo).dot(x.T))
    return cost

def number_partitioning(numbers, initial_temperature=10000, min_temperature=0.1, cooling_rate=0.9999, max_iterations=1000000):
    random.seed(1)
    # 初始化解
    set1 = np.zeros(len(numbers),dtype=int)
    set2 = np.zeros(len(numbers),dtype=int)
    setindex = np.zeros(len(numbers),dtype=bool)

    #創建QUBO
    qubo=QUBO(numbers)
    
    # 定義初始溫度和冷卻率
    temperature = initial_temperature

    # 隨機分配數字到兩個集合(new)    
    for i in range(len(numbers)):
        setindex[i] = random.choice([True, False])
    ans=cost_function(sum(numbers),qubo,setindex)
    
    for _ in range(max_iterations):
        # 生成鄰近解（隨機交換一對元素的分配）(new)
        i = random.randint(0, len(set1)-1)
        setindex[i]= not setindex[i]
        
        # 計算成本差異
        cost_diff = cost_function(sum(numbers),qubo,setindex)
        if(cost_diff==0):
            for i in range(len(numbers)):
                if(setindex[i]==True):
                    set1[i]=numbers[i]
                else:
                    set2[i]=numbers[i]
            ans=cost_diff
            return set1 , set2 ,ans

        # 判斷是否接受鄰近解
        if cost_diff<=ans or random.random() < np.exp(-(cost_diff-ans)/temperature):
            ans = cost_diff
        else:
            # 不接受鄰近解，恢復原始解
            setindex[i]= not setindex[i]
        # 降低溫度
        temperature *= cooling_rate
        if temperature < min_temperature:
            break
        
    # 返回最佳解
    for i in range(len(numbers)):
        if(setindex[i]==True):
            set1[i]=numbers[i]
        else:
            set2[i]=numbers[i]
    return set1, set2, ans

# # 測試
# numbers = [443, 552, 217, 319, 3, 708, 756, 342, 669, 133, 984, 405, 718, 105, 553, 66, 877, 705, 924, 654]#random_array_generator(20)
# # numbers=[1,2,3,4]
# set1, set2 ,min= number_partitioning(numbers)
# print("array=",numbers)
# print("Set 1:", set1)
# print("Set 2:", set2)
# print("Cost:", sum(set1)-sum(set2))
# # print("Cost:", min)