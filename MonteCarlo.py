import numpy as np
from matplotlib import pyplot as plt
from random import random

def f(x):
    return 1.0/(1.0+x**2) 

N = [10, 10**3, 10**5, 10**7]
area_avgs = []
standards = []

for n in  N:
    areas = []
    for _ in range(10):
        count = 0.0
        for _ in range(n):
            x = random()  # [0,1]までの一様乱数をxに格納
            y = random()  # [0,1]までの一様乱数をyに格納
            if y < f (x):  
                count +=1.0
        area = 4*count/n
        areas.append(area)
    area_avg = sum(areas)/10
    area_avgs.append(area_avg)
    s = 0.0
    for a in areas:
        s+=(a-area_avg)**2
    standard = (s/9)**0.5
    standards.append(standard)
    print("\n\nN=", n, "\nstandared=",standard,"\npi=" ,area_avg )

# グラフの描画
plt.plot(N,area_avgs)
plt.show()
plt.plot(N,standards)
plt.show()
