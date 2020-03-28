import numpy as np
import pandas as pd

from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
#Read JSON from src url
src_url = 'https://services5.arcgis.com/mnYJ21GiFTR97WFg/arcgis/rest/services/PH_masterlist/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=%2A&outSR=102100&cacheHint=true&fbclid=IwAR38QbvClnSnwMEw23qlVwTBcgl_fqsFQaYNM1XiCThVVus0sBjclLyp8F0'

def get_covid_ph(url = None):
    """
    Function 
    1.) Queries into PH Department of Health Data (returns JSON)
    2.) Extracts values from JSON into Pandas Dataframe

    url: default value is original url provided (src_url)
    """
    if(url == None):
        url = src_url
    raw = json.loads(urlopen(url).read())
    df = json_normalize(raw['features'])

    #rename columns for easier navigation
    df.rename(columns = lambda x: x.split('attributes.')[-1], inplace = True)
    return df

import re
def extract_contact_cols(df, extract_col = 'travel_hx'):
    """"
    Function returns updated dataframe with columns:
    contacts: complete code of contact [PHX]
    contacts_num: numeric code of contact [x]

    default extract from column 'travel_hx'
    """
    def get_contacts (s):
        try:
            return re.findall(r'\bPH\w+',s)
        except TypeError:
            return ""

    def get_contacts_num (l):
        nums = []
        for i in l:
            nums.append(i.split('PH')[-1])
        return nums
    
    df['contacts'] = df[extract_col].apply(lambda x: get_contacts(x))        
    df['contacts_num'] = df['contacts'].apply(lambda x: get_contacts_num(x))
    return df