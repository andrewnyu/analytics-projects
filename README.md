# ph-covid19-analytics
Network Analysis on NCOV cases in the Philippines. Goal is to use analytics to a.) identify and isolate large networks of cases and b.) identify action points and preventive measures to flatten the curve

<br><br>
Contents:
<br>1. Query official data source (returns JSON), transform JSON into Pandas DataFrame and do initial data cleaning to mine relevant features.
<br>2. Create a graph which maps all direct connections of each case and use depth first search to identify large networks
<br>3. EDA to identify action points with the goal of flattening the curve of cases in networks.

<br><br>
Initial Findings:
<br> 1. Largest connected group (8 people) is a.) loosely connected and b.) spread across multiple hospitals in NCR and 10 days
<br> 2. 10.75% of cases come from "connected components" of two or more people. 

References:
<br> 1. Article on how to source DOH Data: https://www.facebook.com/notes/wilson-chua/working-with-doh-covid-data/2868993263159446/
<br> 2. Code on JSON to Dataframe conversion: https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
