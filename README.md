# PH NCOV Network Analysis
Network Analysis on NCOV cases in the Philippines. Goal is to use analytics to a.) identify and isolate large networks of cases and b.) identify action points and preventive measures to flatten the curve

<br>
## Contents and Methodology:
<br>1. Query official data source (returns JSON), transform JSON into Pandas DataFrame and do initial data cleaning to mine relevant features.
<br>2. Create a graph which maps all direct connections of each case and use depth first search to identify large networks
<br>3. Function case_plot to plot cumulative number of cases as well as earliest and latest case in a network. 

<br><br>
## References:
<br> 1. Article on how to source DOH Data: https://www.facebook.com/notes/wilson-chua/working-with-doh-covid-data/2868993263159446/
<br> 2. Code on JSON to Dataframe conversion: https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
