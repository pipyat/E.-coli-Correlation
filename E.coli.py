

import random
import math
import numpy as np
import matplotlib.pyplot as plt
def simu():
    
    
    R = 3 #Rate of protein use
    N=[] #Number of proteins
    T=[] #Time until division for one daughter
    T_prime=[] #Time until division for the other
    random.seed(1)
    mean_T = 0 #Mean time
    mean_T_prime = 0
    sum_sisters = 0 #Sum as part of correlation coefficient 
    SD = 0 #Standard deviation as part of correlation coefficient 
    SD_prime = 0
    c_sisters = [] #Correlation coefficient
    c_MD = 0
    sum_MD = 0
    mean_N = [] #Mean number of the randomly generated N proteins before they are shared
    std = []
    MD = []

    i = 0 #counters
    j = 0 
    
    

    for j in range(100):
    
        for i in range(1000):
            
#A random number is generated from a Gaussian distribution
            
            n = random.gauss(50+j,2*(50+j)**0.5)
            N.append(n)
            
#This number is shared between daughters via a Gaussian distribution
        
            mu = n/2
            sigma = math.sqrt(n)/2
            T_current = random.gauss(mu,sigma)/R
            T.append(T_current)
            T_prime.append((n/R)-T_current)
            
        
            
#            print(n)
            
#            print(T_current*R, (n/R-T_current)*R)
            
#            print('--------')
            
            
#Pearson correlation coefficient between sisters is calculated
        
        mean_T = np.mean(T)
        mean_T_prime = np.mean(T_prime)
        
        for i in range(1000):
            
            sum_sisters = sum_sisters + (T[i]-mean_T)*(T_prime[i]-mean_T_prime)
        
        SD = np.std(T)
        SD_prime = np.std(T_prime)
            
        
#Correlation between mother and daughter is calculated
        
        for i in range(999):
            
            sum_MD = sum_MD + (T[i]-mean_T)*(T[i+1]-mean_T)
        
        c_MD = ((1/998)*(sum_MD/(SD**2)))
        
        MD.append(((1/998)*(sum_MD/(SD**2))))
        
#        print('{Correlation coefficient between sisters: ', c_sisters)
        
#        print('{Correlation coefficient between mother and daughter: ', c_MD)
        
#        print('{Standard deviation for T: ', SD)
#        print('{Standard deviation for T_prime: ', SD_prime)
        
        
        c_sisters.append((1/999)*(sum_sisters)/(SD*SD_prime))
        mean_N.append(50+j)
        std.append(SD)
        
        
#Variables are reset before the next loop
        
        R = 3 #Rate of protein use
        N=[] #Number of protiens
        T=[] #Time until division for one daughter
        T_prime=[] #Time until division for the other
        random.seed(1)
        mean_T = 0 #Mean time
        mean_T_prime = 0
        sum_sisters = 0 #Sum as part of correlation coefficient 
        SD = 0 #Standard deviation as part of correlation coefficient 
        SD_prime = 0
        c_MD = 0
        sum_MD = 0
    
        i = 0   
    
#The standard deviation in the time to divide is plotted
        
    
    plt.plot(mean_N, c_sisters)
    
    plt.xlabel('mean N')
    plt.ylabel('Sister correlation')
    plt.savefig("plot1.png")
    plt.show()
    
    
        
simu()
