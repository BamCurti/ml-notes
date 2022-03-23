import pandas as pd
import csv

if __name__ == '__main__':
    df = pd.read_csv('./projects/3_bouquet_flower/data/train.csv')
    
    #filter the dataset to only 10 categories
    df_min = df[df.category <= 10]
    
    df_min.to_csv('./projects/3_bouquet_flower/dataset.csv')        
    
    
    