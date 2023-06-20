import NumberPartition as num

numbers = [443, 552, 217, 319, 3, 708, 756, 342, 669, 133, 984, 405, 718, 105, 553, 66, 877, 705, 924, 654]
set1, set2 ,min= num.number_partitioning(numbers)
print("array=",numbers)
print("Set 1:", set1)
print("Set 2:", set2)
print("Cost:", sum(set1)-sum(set2))