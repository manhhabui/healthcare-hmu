import pandas as pd
from datetime import datetime
import numpy as np

def read_elan_data_sets(file_path):
    data = pd.read_csv(file_path,delimiter="\t")
    return data

def read_data_sets(file_path):
    column_names = ['timestamp','x-axis', 'y-axis', 'z-axis']
    data = pd.read_csv(file_path,header = None, names = column_names,delimiter="\t")
    return data

def read_txt_data_sets(file_path):
    column_names = ['ACEL','timestamp','155', 'id','x-axis', 'y-axis', 'z-axis']
    data = pd.read_csv(file_path,header = None, names = column_names, delimiter=r",")
    return data

folder_root="Pat_14_23_9/Recorder_2019_10_22_15_16/"
elan_data=read_elan_data_sets(folder_root+"/label.txt")
data=read_data_sets(folder_root+"/elan_shoes.csv")
txt_data=read_txt_data_sets(folder_root+"/wax-2019-10-22-15-16-40.csv")
e_idx=0
activities=[]
pat_id=[]
add_info=[]
for idx in range(len(data["timestamp"])):
    if (e_idx<len(elan_data["End Time - ss.msec"]) and data["timestamp"][idx]>=elan_data["End Time - ss.msec"][e_idx]):
        e_idx+=1
    if(e_idx>=len(elan_data["End Time - ss.msec"])):
        label="0"
        add_if=np.nan
    else:
        label=elan_data["default"][e_idx]
        add_if=elan_data["NaN"][e_idx]
    activities.append(label)
    add_info.append(add_if)
    pat_id.append(elan_data["id"][0]) 

del txt_data['ACEL']
del txt_data['155']
del txt_data['id']

txt_data['id']=pat_id
txt_data['activity']=activities
txt_data['NaN']=add_info
columns_titles=['id','timestamp','x-axis', 'y-axis', 'z-axis','activity','NaN']
txt_data=txt_data.reindex(columns=columns_titles)
txt_data.to_csv(folder_root+"/wax-2019-10-22-15-16-40.csv",header=None, sep='\t', encoding='utf-8', index=False, float_format='%.7f')