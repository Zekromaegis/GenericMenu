import pandas as pd
from string import ascii_lowercase
from random import sample
from typing import Optional, List
# int

df = pd.DataFrame([
    {'points': 50, 'time': 5, 'year': 2010},
    {'points': 25, 'time': 6, 'month': "february"},
    {'points':90, 'time': 9, 'month': 'january'},
    {'points':20, 'time':1, 'month': 'june'},
])
df.fillna(value='-',inplace=True)

pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

TYPE_LIST = list(ascii_lowercase)

ptype = 'Water'

def toggle_print(option:str='reset'):
    '''
    Input: option - (String) full, rows, reset. Defaults to reset.
    Output:
        On default the mode set is rows.
        full - All rows and columns are displayed. Depending on screen size it might not be pretty.
        rows - All rows will be displayed. Middle columns might be hidden.
        reset - The most pretty format. Will probably hide quite a few rows and columns.
    '''
    if option == 'full':
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
    elif option == 'rows':
        pd.set_option('display.max_rows', 500)
        #pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
    elif option == 'reset':
        pd.reset_option('display.max_rows')
        pd.reset_option('display.max_columns')
        pd.reset_option('display.width')
    else:
        raise ValueError('Parameter option can only take values full, rows or reset.')

def get_column(column:str):
    '''
    Input: column - (String) Make sure the case is correct.
    Output: Series of values contained in the column.
    '''
    return df[column]
            
def by_query(column:str,minval:int,maxval:Optional[int]=None):
    '''
    Input:
        column - (String) Column to filter the dataframe on. Example values - time, points
        minval - (int) Minimum value, inclusive.
        maxval - *OPTIONAL* (int or None) Maximum value, inclusive.
        
        if maxval is not given, it is treated as equal to minval.
    
    Output: Returns Dataframe that is filtered by column acc to specified min and max values.
    '''
    if maxval is None:
        maxval = minval
    return df[
        (df[column] >= minval) &
        (df[column] <= maxval)
    ]

def multitype_selector(n:int=2,selected_chars:List[str]=[]):
    '''
    Input:
        n - (Integer) Number of types to be selected at random. Defaults to 2.
        selected_chars - (List of Strings) Types to always be selected in addition to 'n' types.
    Output:
        Prints the randomly selected chars.
    '''
    if not set(selected_chars).issubset(TYPE_LIST):
        raise ValueError('Invalid Type passed in selected types.')
    SAMPLE_TYPES = [i for i in TYPE_LIST if i not in selected_chars]
    ptypes = sample(SAMPLE_TYPES,n) + selected_chars
    print(f"{ptypes}")
