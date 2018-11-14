#
# Author: Anna Hernandez Duran
# Date: November 2018
#
#


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook # this is to call the output_notebooke() function
from bokeh.models import ColumnDataSource # to add interactivity you need ColumnDataSource
from bokeh.models import tools # to add interactivity you need ColumnDataSource



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
        
    
    # create dataframe to return the morgage data
    mortgage = pd.DataFrame({'year': np.arange(1, mortgage_length+1), 'interest': interests, 'capital':capitals, 'pay':lefttopay})
    
    # return dataframe
    return mortgage
   



# define function to create Bokeh plot
def make_plot(amount):
   
    # call function with desired amount 
    mortgage = calculate_mortgage(float(amount))

    # convert the dataframe returned by calculate_mortgage() into a ColumnDataSource (to be used by Bokeh)
    mortgage_cds = convert_df_to_cds(mortgage)
    stacks = ['pay','capital','interest']
    colors_arr = ["#c9d9d3", "#718dbf", "#e84d60"]
    
    p = figure(title="Mortgage repayment over time", 
               plot_width = 600, plot_height = 600, 
               x_axis_label='x', 
               y_axis_label='y')

    
    p.vbar_stack(stacks, source=mortgage_cds, x='year',  width=0.9, fill_alpha=0.5, color=colors_arr, line_color = 'black')

    # refer to data with @ and
    # to graph properties, e.g. x and y, with $
    h = tools.HoverTool(tooltips = [('Year: ','@year'),
                                    ('Capital left to repay', '@pay'),
                                    ('Repayment on interests', '@interest'),
                                    ('Repayment on capital', '@capital')])

    # add tool to the graph
    p.add_tools(h)

    output_notebook()

    return p





# ---------------------------- MAIN ------------------------------


# create plot
p = make_plot(273000.0)

# show plot
show(p)


