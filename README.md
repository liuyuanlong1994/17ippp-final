# Will Economic Growth Drive Soccer Clubs' Spending in Purchasing Players?
Authors:
  Tianyuan Bai /
  Yuanlong Liu  
_______________
  Please read First.ipynb and Second.ipynb for our code and analysis.
  
  The codes are initialcode.py for First.ipynb, and nooutlier.py for Second.ipynb.
  
  For country economic data, please refer to country.csv
  For soccer investment data, please refer to soccer.csv for a comprehensive set of transfer markets; or nooutlier.csv, for our second part analysis without outliers markets.

_______________
  In this study, we attempt to find the correlation between economic activities, and soccer clubs' spending in purchasing players. In other words, will more GDP growth lead to more investment into the soccer transfer market?

  Most soccer clubs all over the world can purchase and sell players on a free market basis across national boundaries. Hence we frequently see wealthy clubs collect talented players from every corner of the world. Often times, either these wealthy clubs are in developed countries, such as the UK, France, Germany, Spain and Italy; or in other cases, high-profile deals invovle clubs located at emerging markets where their GDP grows much faster than others, ie. China and Saudi Arabia.

  Hence, is it likely that the quicker the economy develops, the more investment of its soccer league into purchasing soccer players in the market?

  We select the top-50 soccer leagues by the amount of transfer fees they spent in year 2012, and 2017. We correspond their soccer investment data with their country economic data, including GDP growth, Inflation growth and unemployment rate growth, from 2011 to 2016. The matching is between 2011-2016 vs. 2012-2017 because we assumed that just like any other exogenous shocks, soccer investments have time lags to absorb influences from the economy.

First.ipynb

  In the first model, the country data and soccer data are comprehensive. We run a multi-variate regression of the log change of soccer expenditure, on the log change of GDP growth, inflation growth, unemployment rate growth and instrumental variables that account for unobserved characteristics such as culture and institutions. For instance, it may be assumed that European countries may be willing to spend more into soccer, than Asian countries, given equal amount of GDP growth. The function is outlined as below:

  logSoccerExpenditure = β0 + β1×logGDP + β2×logInflation + β3×logUnemployment + β4×Europe + β5×Asia + β6×America

  The result turns back, as a weak negative correlation. Meaning more GDP growth contribute to less increarse in soccer spending.

  This surprised us. Hence we wonder whether several outliers significantly downplayed the effect of economic development on soccer expenditure. In the second part, we ruled out the outliers and run the same regression once again. Here, the only change takes place in the dataset, where 3 observations are pulled out.

Second.ipynb

  The second result appears more intuitively sensible, also with an improved R-square. The correlation of GDP growth and soccer expenditure increase becomes positive. In addition, the most statistically significant explanatory variable is unemployment growth, with a negative correlation with soccer expenditure increase. This demonstrates that the lower the unemployment an economy features, in other words, the more virbrant the market economy is, the more expenditure will be into purchasing soccer players in a given soccer transfer market.

  We conclude that economic development indeed contributes to more spending in purchasing soccer players across the world.
