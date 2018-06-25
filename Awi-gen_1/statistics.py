import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaB


def gen_stats(col):
    '''Generates the mean, median and standard deviation from a given column of data'''
    mean = np.mean(col)
    sd =np.std(col)
    median = np.median(col)
    return mean,sd,median

def calculate_stats (col,name,standard_deviation_limit):
    '''Checks that the data gen_stats produces '''
    [mean,sd,median] = gen_stats(col)
    all_good = True
    
    if sd > standard_deviation_limit:
        
        all_good = False
        
    return mean,sd,median,all_good