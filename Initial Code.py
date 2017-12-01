#This code serves as the first sequence of this study.

import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

import csv

import seaborn as sns

import statsmodels.formula.api as sm


#Below we let python read the two csv files here, one country data and one soccer data, respectively.

country=pd.read_csv("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/country.csv")
dictobj = csv.DictReader(open("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/country.csv"))

soccer=pd.read_csv("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/soccer.csv")
dictobj = csv.DictReader(open("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/soccer.csv"))

mergedsheet = pd.merge(country,
                    soccer,
                    on='Country')


#Here the two csv has been merged into one by country. Hence each country becomes associated with both economic data (GDP, Inflation, Unemployment rate) and Soccer Data (Expenditure, Income)

print(mergedsheet)

#Below we look at the scatter plot to intuitively approximate the relaitonship between economic activities and soccer investment.

mergedsheet.plot(kind='scatter', x = 'GDP Log Change', y = 'Expenditure log change')
plt.show()

#Then with respect to the country data, we generate independent variables and dependent variables for the regression model.
#Apart from the country data csv itself, we also set instrumental variables to account for cultural and institutional effects outside of the data.

Y = mergedsheet['Expenditure log change']
X1 = mergedsheet['GDP Log Change']
X2 = mergedsheet['Inflation Log Change']
X3 = mergedsheet['Unemployment Log Change']
X4 = mergedsheet['Europe']
X5 = mergedsheet ['Asia']
X6 = mergedsheet ['America']

#Below we run the data and find the linear relationship between soccer investment, and the 6 independent variables.

model = sm.ols(formula = 'Y ~ X1+ X2 + X3 + X4 + X5 + X6', data = mergedsheet).fit()
model.summary()

#But here we want to see the relationship between soccer investment, and GDP growth alone. It shows that GDP growth on the margin increases investment growth.

sns.regplot(data = mergedsheet, x = X1, y = Y)
plt.show()

#But given the original scatter plot of country data and soccer data, and given the plot we see just above, we wonder whether there're outliers influcing this correlation.

plt.boxplot(mergedsheet['Expenditure log change'])
plt.show()

plt.boxplot(mergedsheet['GDP Log Change'])
plt.show()

#Thus we find that China, Ukraine, Greece, and Egypt are economic outliers. Greece, Colombia, Slovakia are soccer investment outliers.

plt.boxplot(mergedsheet['Expenditure log change'], ['GDP Log Change'])
plt.show()

#It seems that all together, investment outliers plays a more important role.
#Hence in the other pydoc, we exclude Greece, Colombia and Slovakia from soccer data, and keep everything else the same.
#Let's see if the regression is improved.
