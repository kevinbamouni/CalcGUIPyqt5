import pandas as pd

def VaR_fi(pathfile):

    df = pd.read_csv(pathfile, sep=',')
    
    df['returns'] = df['Close'].pct_change().dropna()
    
    return [df['returns'].quantile(0.1), df['returns'].quantile(0.05), df['returns'].quantile(0.01), df['returns'].quantile(0.005)]

A = pd.DataFrame(VaR_fi('C:/Users/work/Documents/varui/FCHI.csv'))