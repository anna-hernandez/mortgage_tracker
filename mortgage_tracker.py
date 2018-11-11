#
#
#
#
#


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


borrowed = 273000.0
interest_rate = 0.025
mortgage_length = 25.0
repayment_divident = (1.0-(1/(1+interest_rate)**mortgage_length))*(1/interest_rate)
annual_repayment = borrowed * 1.0/repayment_divident
monthly_repayment = annual_repayment/12.0

interests = np.empty([1, int(mortgage_length)])
lefttopay = np.empty([1,int(mortgage_length)])
capitals = np.empty([1,int(mortgage_length)])

working_borrowed = borrowed
for year in range(int(mortgage_length)):
	#print('Year',year+1)
	on_interests = working_borrowed*0.025
	interests[0][year] = on_interests
	on_capital = annual_repayment - on_interests
	capitals[0][year] = on_capital
	#print('Repayment divident: {}'.format(repayment_divident))
	#print('Annual repayment: {}'.format(annual_repayment))
	#print('Monthly repayment: {}'.format(monthly_repayment))
	#print('Annual repayment going to interests: {}'.format(on_interests))
	#print('Annual repayment going to capital: {}'.format(on_capital))

	working_borrowed -= on_capital
	lefttopay[0][year] = working_borrowed
	print('Left to pay: {}'.format(working_borrowed))
	
print(interests)
plt.figure(1, figsize=(10,5))

p1 = plt.bar(np.arange(1,int(mortgage_length)+1), lefttopay[0], alpha=0.8)
p2 = plt.bar(np.arange(1,int(mortgage_length)+1), capitals[0], bottom=lefttopay[0], alpha=0.8)
p3 = plt.bar(np.arange(1,int(mortgage_length)+1), interests[0], bottom=lefttopay[0]+capitals[0], alpha=0.8)
p4 = plt.plot(np.arange(1,int(mortgage_length)+1), [annual_repayment]*int(mortgage_length),color='black', linestyle='--', linewidth=1)
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Left to pay', 'Capital repayment', 'Interest repayment', 'Annual repayment'))
plt.title('Mortgage repayment over time')
plt.xlabel('Time (years)')
plt.ylabel('Amount (currency)')
plt.yticks(np.arange(0, 300001, 50000))
plt.xticks(np.arange(1,int(mortgage_length)+1,1))
plt.ylim(top=300000)
plt.show()



