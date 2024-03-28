import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    years = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']

    plt.figure(figsize=(10, 6))
    plt.scatter(years, sea_level)

    # Create first line of best fit

    fit = linregress(years, sea_level)
    slope = fit.slope
    intercept = fit.intercept
    x_values = pd.Series([i for i in range(df['Year'].min(), 2051)])
    y_values = intercept + slope * x_values
    plt.plot(x_values, y_values, 'r')


    # Create second line of best fit

    recent_data = df[df['Year'] >= 2000]
    recent_years = recent_data['Year']
    recent_sea_level = recent_data['CSIRO Adjusted Sea Level']
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years, recent_sea_level)
    x_values_recent = pd.Series([i for i in range(2000, 2051)])
    y_values_recent = intercept_recent + slope_recent * x_values_recent
    plt.plot(x_values_recent, y_values_recent, 'g')


    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Draw the plot
draw_plot()
plt.show()
