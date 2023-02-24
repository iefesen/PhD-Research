# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:11:12 2023

@author: 20224695
"""

from matplotlib import pyplot as plt

"Parameter Definition here"

Q = 100
I = 50

lambda_b = 0.1
lambda_s = 0.4
lambda_c = 0.4

obj_list = []
t_list = []

t_list_decay_I = []
t_list_decay_Q = []

I_list = []
Q_list = []

#This is where we define how the objective function behaves as a 
for t in range(1, 500):
    
    t_doubleprime = (Q + (lambda_s + lambda_c - lambda_b)*t)/(lambda_s + lambda_c)
    t_prime = I/(lambda_s + lambda_c)
    
    obj = (I - lambda_s*t_prime/2)*t_prime + (Q - lambda_b*t - ((t_doubleprime-t)*lambda_s)/(2))*(t_doubleprime - t)
    
    if t_prime >= t:
        t_prime = (I - lambda_c*t)/(lambda_s) 
        obj = (I - lambda_s*t/2)*t + (Q - lambda_b*t - ((t_doubleprime-t)*lambda_s)/(2))*(t_doubleprime - t)
        if t_prime >= t_doubleprime:
            t_prime = (I - lambda_c*t + lambda_c*t_doubleprime)/(lambda_s + lambda_c)
            obj = (I - lambda_s*t/2)*t + (Q - lambda_b*t - ((t_doubleprime-t)*lambda_s)/(2))*(t_doubleprime - t) + (t_prime - t_doubleprime)*(I - (lambda_s + lambda_c)*t -lambda_s*(t_doubleprime - t) - (lambda_s + lambda_c)*(t_prime - t_doubleprime)/(2))

    obj_list.append(obj)
    t_list.append(t)


plt.plot(t_list, obj_list)
plt.show()

opt_obj = max(obj_list)

max = obj_list[0]

opt_t = 0
for i in range(1,len(obj_list)):
    if obj_list[i] > max:
        max = obj_list[i]
        opt_t = i
        
        
print(f'Optimal t is: {opt_t}')
print(f'Optimal objective function value is: {opt_obj}')



for i in range(0, opt_t):
    if I >= 0:
        I = I - lambda_s - lambda_c
        Q = Q - lambda_b
        I_list.append(I)
        Q_list.append(Q)
        

for i in range(0, 1000):
    
    if Q >= 0:
        Q = Q - lambda_s - lambda_c
        Q_list.append(Q)
        if I >=0:
            I = I - lambda_s
        else:
            I = 0
        I_list.append(I)


plt.plot(I_list)
plt.plot(Q_list)
plt.show()


