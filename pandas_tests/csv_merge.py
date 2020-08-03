# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd


def main():
    df = pd.read_csv(r"data.csv", names=['a', 'b', 'c', 'd', 'e', 'f'])
    df_extra = pd.read_csv(r"extra_data.csv")    
    df_header = df.loc[:5, :]
    df_body = df.loc[6:, :].astype(float)
    df_tip_centres = df_body[list('abc')]
    df_tip_centres += df_extra.loc[0]
    df_body[list('abc')] = df_tip_centres
    
    df_result = df_header.append(df_body)
    df_result.to_csv("output.csv", header=False, index=False, float_format='%.6f')
    
    

if __name__ == "__main__":
    main()