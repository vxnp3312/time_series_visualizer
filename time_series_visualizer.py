import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

#import the data from "fcc-forum-pageviews.csv"
ds = pd.read_csv('fcc-forum-pageviews.csv')

#Set the index to the date column.
ds['date'] = pd.to_datetime(ds['date'])
ds.set_index('date', inplace=True)
ds

#days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
ds = ds[(ds['value'] >= ds['value'].quantile(0.025)) & (ds['value'] <= ds['value'].quantile(0.975))]
ds

#Create a draw_line_plot function
def draw_line_plot():
  plt.figure(figsize=(14, 4))
  plt.plot(ds.index, ds['value'], linestyle='-')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.grid(True) #Display grid
  plt.show()

draw_line_plot()


#Create a draw_bar_plot function that show average daily page views for each month grouped by year. 
def draw_bar_plot():
  ds_bar = ds.copy()
  ds_bar['year'] = ds_bar.index.year
  ds_bar['month'] = ds_bar.index.month_name()
  ds_bar = ds_bar.groupby(['year', 'month'])['value'].mean().unstack()

  fig = ds_bar.plot(kind='bar', figsize=(14,4 )).figure
  plt.title('Months')
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
  plt.show()

draw_bar_plot()


#Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots
def draw_box_plot():
    ds_box = ds.copy()
    ds_box.reset_index(inplace=True)
    ds_box['year'] = [d.year for d in ds_box.date]
    ds_box['month'] = [d.strftime('%b') for d in ds_box.date] #Convert to Index using specified date_format (mounth in that case)
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(x='year', y='value', data=ds_box, ax=axes[0]).set(title='Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='value', data=ds_box, ax=axes[1]).set(title='Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.savefig('box_plot.png')
draw_box_plot()


