#
# Author: Anna Hernandez Duran
# Date: November 2018
#
#


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# define function that will calculate morgage. Input parameter = borrowed amount
def calculate_mortgage(amount):

    # define variables with fixed value
    borrowed = float(amount)
    interest_rate = 0.025
    mortgage_length = 25
    repayment_divident = (1.0-(1/(1+interest_rate)**mortgage_length))*(1/interest_rate)
    annual_repayment = borrowed * 1.0/repayment_divident
    monthly_repayment = annual_repayment/12.0

    # create tracking arrays
    interests = np.empty((0, mortgage_length))
    lefttopay = np.empty((0, mortgage_length))
    capitals = np.empty((0, mortgage_length))

    working_borrowed = borrowed

    # loop through mortgage years to calculate the payments per year
    for year in range(mortgage_length):
        #print('Year',year+1)
        on_interests = working_borrowed*0.025
        interests = np.append(interests, on_interests)
        on_capital = annual_repayment - on_interests
        capitals = np.append(capitals, on_capital)
        
        working_borrowed -= on_capital
        lefttopay = np.append(lefttopay, working_borrowed)
        
        print('\tYear: {}'.format(year))
        print('Repayment divident: {}.'.format(round(repayment_divident,3)))
        print('Annual repayment: {}. '.format(round(annual_repayment,3)))
        print('Monthly repayment: {}. '.format(round(monthly_repayment,3)))
        print('Annual repayment going to interests: {}.'.format(round(on_interests,3)))
        print('Annual repayment going to capital: {}.'.format(round(on_capital,3)))
        print('Left to pay: {}.'.format(round(working_borrowed,3)), end='\n\n')
    

    # --------------------- MAKE PLOT --------------------------

    # create figure
    plt.figure(1, figsize=(10,5))

    # add stacked bar plot
    p1 = plt.bar(np.arange(1,mortgage_length+1), lefttopay, alpha=0.8)
    p2 = plt.bar(np.arange(1,mortgage_length+1), capitals, bottom=lefttopay, alpha=0.8)
    p3 = plt.bar(np.arange(1,mortgage_length+1), interests, bottom=lefttopay+capitals, alpha=0.8)
    p4 = plt.plot(np.arange(1,mortgage_length+1), [annual_repayment]*mortgage_length,color='black', linestyle='--', linewidth=1)
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Left to pay', 'Capital repayment', 'Interest repayment', 'Annual repayment'))
    plt.title('Mortgage repayment over time')
    plt.xlabel('Time (years)')
    plt.ylabel('Amount (currency)')
    plt.yticks(np.arange(0, 300001, 50000))
    plt.xticks(np.arange(1,mortgage_length+1,1))
    plt.ylim(top=300000)

    # show plot
    plt.show()
    


# ---------------------------- MAIN ------------------------------

# call function with desired amount
calculate_mortgage(273000.0)


