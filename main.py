"""

Created on Wednesday 03-24-2021
Function :
Project :
Author : Ragunath Anbarasu

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
from sklearn.impute import SimpleImputer


"""
Read training CSV data in data frame

"""
original_df = pd.read_csv("Files/csv_result-Descriptors_Training.csv")

df_without_id = original_df.drop(['id'], 1)

df_without_id.head()


