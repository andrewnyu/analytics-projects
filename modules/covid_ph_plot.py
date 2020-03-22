import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_case_plot(df, date_col = 'confirmed'):
    """
    This function plots the case growth curve for the given dataframe (df) 
    and prints the first and latest confirmed case.
    
    df:
        Format - data extracted in part I (from DOH source)
        Can be full data extract or a slice
    date_col:
        current decision is to use column 'confirmed.' see Data Validation section for details
    """
    case_dates = df[date_col]

    def get_date_part(d):
        #Function removes empty/invalid dates
        try:
            date = pd.to_datetime(d)
            return d
        except ValueError:
            return np.nan

    case_dates = case_dates.apply(lambda x: get_date_part(x))
    case_count = pd.DataFrame(case_dates[~case_dates.isnull()].unique())
    case_count.rename(columns = {0: 'date'}, inplace = True)
    
    for row in case_count.itertuples():
        current_date = getattr(row, 'date')
        case_count.loc[getattr(row, 'Index'), 'case_count'] = len(df[df[date_col]==current_date])

    for i in range(1, len(case_count)):
        case_count.loc[i, 'case_count'] += case_count.loc[i-1, 'case_count']
    
    #print first and latest confirmed date
    print("First Confirmed Case: ", str(min(pd.to_datetime(case_count['date']))).split(' ')[0])
    print("Latest Confirmed Case: ", str(max(pd.to_datetime(case_count['date']))).split(' ')[0])
    #plot
    plt.plot(case_count['date'], case_count['case_count'])