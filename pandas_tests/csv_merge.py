# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd


def main():
    """Main method, reads 2 .csv files, adds the contents of one to a
    subframe of the other, then saves the result."""
    df_original = pd.read_csv(r"data.csv", names=['a', 'b', 'c', 'd', 'e', 'f'])
    df_extra = pd.read_csv(r"extra_data.csv")
    df_header = df_original.loc[:5, :]
    df_body = df_original.loc[6:, :].astype(float)
    df_tip_centres = df_body[list('abc')]
    df_tip_centres += df_extra.loc[0]
    df_body[list('abc')] = df_tip_centres
    df_result = df_header.append(df_body)
    df_result.to_csv("output.csv", header=False, index=False, float_format='%.6f')

if __name__ == "__main__":
    main()
