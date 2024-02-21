# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:14:38 2024

@author: nehak
"""

import pandas as pd

# transactions_data = pd.read_excel(r"C:\Neha\kaggle Projects\Git hub\PowerBI\Sales Dashboard\Raw_data.xlsx",sheet_name='Transactions')
# newcustomer_data = pd.read_excel(r"C:\Neha\kaggle Projects\Git hub\PowerBI\Sales Dashboard\Raw_data.xlsx",sheet_name='NewCustomerList')
# customerdemographic_data = pd.read_excel(r"C:\Neha\kaggle Projects\Git hub\PowerBI\Sales Dashboard\Raw_data.xlsx",sheet_name='CustomerDemographic')
# customeraddress_data = pd.read_excel(r"C:\Neha\kaggle Projects\Git hub\PowerBI\Sales Dashboard\Raw_data.xlsx",sheet_name='CustomerAddress')


import numpy as np

m = np.array([[2,5,8],[9,0,7]])


def set_zero(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0: 
                matrix[i] = np.zeros(cols,dtype='int')
                matrix[:,j] = np.zeros(rows,dtype='int')
                
    return matrix

p = set_zero(m)