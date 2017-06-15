# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:31:15 2016

@author: HongYu
"""

import numpy as np
import matplotlib.pyplot as plt
K=9100
Interval=500
ST=np.arange(K-Interval,K+Interval)
#naked long/short call
plt.figure(1)
Premium_Call=179
P_LC= np.maximum(ST-K,0) - Premium_Call
P_SC= Premium_Call - np.maximum(ST-K,0)
plt.plot(ST,P_LC,color='#FF0000',label="Long Call")
plt.plot(ST,P_SC,color='#00FF00',label="Short Call")
plt.axhline(color='black')
plt.ylabel('Options payoff')
plt.xlabel('Stock Index')
plt.title('Naked Call Strategy')
plt.legend(loc=2)
#naked long/short put
plt.figure(2)
Premium_Put=185
P_LP= np.maximum(K-ST,0) - Premium_Put
P_SP= Premium_Put - np.maximum(K-ST,0)
plt.plot(ST,P_LP,color='#FF0000',label="Long Put")
plt.plot(ST,P_SP,color='#00FF00',label="Short Put")
plt.axhline(color='black')
plt.ylabel('Options payoff')
plt.xlabel('Stock Index')
plt.title('Naked Put Strategy')
plt.legend()
plt.show()