import time
import pandas as pd
import matplotlib.pyplot as plt
import os
from iterative import power
from recursiveTwoCalls import recursivePower
from recursiveSingleCall import recursivePowerOptimized

# Define input size
inputSize = 10
inputList = list(range(1, inputSize + 1))

# Create directory for results if it doesn't exist
results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

powerTime = []
recursivePowerTime = []
recursivePowerOptimizedTime = []

for i in inputList:
    powerTime_list = []
    recursivePowerTime_list = []
    recursivePowerOptimizedTime_list = []

    for j in range(10):
        start = time.time()
        power(2, i)
        end = time.time()
        powerTime_list.append(end - start)
    
    powerTime.append(sum(powerTime_list) / len(powerTime_list))

    for _ in range(10):
        start = time.time()
        recursivePower(2, i)
        end = time.time()
        recursivePowerTime_list.append(end - start)

    recursivePowerTime.append(sum(recursivePowerTime_list) / len(recursivePowerTime_list))
    
    for _ in range(10):
        start = time.time()
        recursivePowerOptimized(2, i)
        end = time.time()
        recursivePowerOptimizedTime_list.append(end - start)

    recursivePowerOptimizedTime.append(sum(recursivePowerOptimizedTime_list) / len(recursivePowerOptimizedTime_list))

# Plotting and saving the figure

plt.figure(figsize=(10, 5))
plt.plot(inputList, powerTime, label='Power brute-force')
plt.plot(inputList, recursivePowerTime, label='Recursive Power')
plt.plot(inputList, recursivePowerOptimizedTime, label='Recursive Power Optimized')
plt.xlabel('Input size')
plt.ylabel('Time (s)')
plt.title('Algorithms execution time')
plt.legend()
plt.grid(True)

fig_name = f'{results_dir}/figure-{inputSize}.png'
plt.savefig(fig_name)

plt.show()

# Save the data into a dataframe
data = {
    'Input size': inputList,
    'Power brute-force': powerTime,
    'Recursive Power': recursivePowerTime,
    'Recursive Power Optimized': recursivePowerOptimizedTime
}

df = pd.DataFrame(data)

df_name = f'{results_dir}/dataframe-{inputSize}.xlsx'
df.to_excel(df_name, index=False)