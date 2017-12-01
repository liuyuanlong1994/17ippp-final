#This code serves as the second sequence of this study.

import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

import csv

import seaborn as sns

import statsmodels.formula.api as sm

country=pd.read_csv("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/country.csv")
dictobj = csv.DictReader(open("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/country.csv"))


soccer=pd.read_csv("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final//No outlier.csv")
dictobj = csv.DictReader(open("/Users/liuyuanlong/Desktop/上课/chicago/programming/17ippp-final/No outlier.csv"))

mergedsheet = pd.merge(country,
                    soccer,
                    on='Country')

#everything untill here is the same to the first code we wrote.

mergedsheet.plot(kind='scatter', x = 'GDP Log Change', y = 'Expenditure log change')
plt.show()

#But here because we dropped soccer outliers, the data seems to be more sensible and less noisy.

plt.boxplot(mergedsheet['Expenditure log change'])
plt.show()

plt.boxplot(mergedsheet['Expenditure log change'], ['GDP Log Change'])
plt.show()

#The boxplot also proves that there remains no more outliers.

Y = mergedsheet['Expenditure log change']
X1 = mergedsheet['GDP Log Change']
X2 = mergedsheet['Inflation Log Change']
X3 = mergedsheet['Unemployment Log Change']
X4 = mergedsheet['Europe']
X5 = mergedsheet ['Asia']
X6 = mergedsheet ['America']

model = sm.ols(formula = 'Y ~ X1+ X2 + X3 + X4 + X5 + X6', data = mergedsheet).fit()
model.summary()

#with the same independent and dependent variable but a changed dataset, the regression's R-squared is improved, so is
#the statistical significance of independent variables.

sns.regplot(data = mergedsheet, x = X1, y = Y)
plt.show()

#Nevertheless, the linear correlation between Soccer expenditure and GDP growth becomes negative. 
