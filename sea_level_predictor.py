import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    ig, ax = plt.subplots(figsize=(10, 4))
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=3)

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    result = linregress(x, y)
    x_fit = np.arange(1880, 2051)
    y_fit = list(map(lambda x: x * result.slope + result.intercept, x_fit))
    plt.plot(x_fit, y_fit, color='red')
    
    # Create second line of best fit
    index_2000 = df[df['Year'] == 2000].index[0]
    x_2 = df['Year'][index_2000:]
    y_2 = df['CSIRO Adjusted Sea Level'][index_2000:]

    result_2 = linregress(x_2, y_2)
    x_fit_2 = np.arange(2000, 2051)
    y_fit_2 = list(map(lambda x: x * result_2.slope + result_2.intercept, x_fit_2))
    plt.plot(x_fit_2, y_fit_2, color='green')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()