# PH COVID-19 Network Analysis
Initial EDA and Network Analysis on PH COVID-19 cases in the Philippines from official Department of Health source.
<br>
Future development and source code maintained at this [repo](https://github.com/enzoampil/phcovid).
<br>
<br>
## Code used in analysis is now packaged and installable via pip.
```
pip install phcovid
```


<br>
## Contents and Methodology:
<br>1. Query official data source (returns JSON), transform JSON into Pandas DataFrame and do initial data cleaning to mine relevant features.
<br>2. Create a graph which maps all direct connections of each case and use depth first search to identify large networks
<br>3. Function case_plot to plot cumulative number of cases as well as earliest and latest case in a network. 

<br><br>
## References:
<br> 1. DOH Data Source from this [blog post](https://www.facebook.com/notes/wilson-chua/working-with-doh-covid-data/2868993263159446/)
<br> 2. [Code](https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe) on JSON to Dataframe conversion 
