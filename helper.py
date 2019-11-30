import pandas as pd
import numpy as np
from scipy import stats

sheet_name_dict = {
                    'A' : 'A - aaup', 
                    'B' : 'B - bodyfat',
                    'C' : 'C - plasma',
                    'D' : 'D - homedat'
                  }

def get_tasks_var(my_var):
    excel_file = 'var_matstat_K5.xls'
    df = pd.read_excel(excel_file)
    num_of_task = list(df.columns.values)[1:]
    num_of_var = df.values.tolist()[my_var-1][1:]
    dict_ = dict(zip(num_of_task, num_of_var))
    my_dict = {}
    for ls in dict_.keys():
        for key in ls.split(','):
            k = key.strip()
            if k in ls:
                my_dict[k]=dict_[ls]
    return my_dict


def get_name_of_sheet(my_dict):
    return sheet_name_dict[list(my_dict.values())[0][0]]


def get_data(num_of_task, tasks_var):
    excel_file = 'data_matstat_K5.xls'
    sht_nm = get_name_of_sheet(tasks_var)
    df = pd.read_excel(excel_file, sheet_name=sht_nm)
    rows = tasks_var[num_of_task].split()
    return df[rows]