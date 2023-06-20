# Copyright (c) 2023 by Sebastian All Rights Reserved */
#    NAME
#      NumberPartition.py
#    PURPOSE
     
#    NOTES
     
#    AUTHOR
#      Sebastian (kevin1111006@gmail.com)
#    HISTORY
#      Sebastian - Jun 20, 2023: Created.
     
import random
import numpy as np

# 生成隨機整數列表 (可供使用，但並未使用到)
def random_array_generator(size):
    random_list = [random.randint(1, 1000) for _ in range(size)]
    return random_list

# 定義成本函數
def cost_function(set1, set2):
    return abs(sum(set1) - sum(set2))

def number_partitioning(numbers, initial_temperature=10000, min_temperature=0.1, cooling_rate=0.9999, max_iterations=1000000):
    random.seed(1)
    # 初始化解
    set1 = np.zeros(len(numbers),dtype=int)
    set2 = np.zeros(len(numbers),dtype=int)
    setindex = np.zeros(len(numbers),dtype=bool)

    # 定義初始溫度和冷卻率
    temperature = initial_temperature

    # 隨機分配數字到兩個集合(new)    
    for i in range(len(numbers)):
        setindex[i] = random.choice([True, False])
        if(setindex[i]==True):
            set1[i]=numbers[i]
        else:
            set2[i]=numbers[i]
    ans=cost_function(set1,set2)
    
    for _ in range(max_iterations):
        # 生成鄰近解（隨機交換一對元素的分配）(new)
        i = random.randint(0, len(set1)-1)
        setindex[i]= not setindex[i]
        set1[i],set2[i]=set2[i],set1[i]
        
        # 計算成本差異
        cost_diff = cost_function(set1, set2)
        if(cost_diff==0):
            ans=cost_diff
            return set1 , set2 ,ans
                
        # 判斷是否接受鄰近解
        if cost_diff<=ans or random.random() < np.exp(-(cost_diff-ans)/temperature):
            ans = cost_diff
        else:
            # 不接受鄰近解，恢復原始解
            set1[i], set2[i] = set2[i], set1[i]
            setindex[i]= not setindex[i]
        # 降低溫度
        temperature *= cooling_rate
        if temperature < min_temperature:
            break
        
    # 返回最佳解
    return set1, set2, ans
