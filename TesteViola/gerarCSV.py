import copy
import csv

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from atom import ATOMClassifier
from PIL import Image

data = pd.read_csv("dataset_descriptor.csv")
print("Leu DATASET")

columns = ["ip_proto","ip_len_mean","ip_len_median","ip_len_var",
               "ip_len_std","ip_len_entropy","ip_len_cv","ip_len_cvq",
               "ip_len_rte", "sport_mean","sport_median","sport_var","sport_std",
               "sport_entropy","sport_cv","sport_cvq","sport_rte",
               "dport_mean","dport_median","dport_var","dport_std",
               "dport_entropy","dport_cv","dport_cvq","dport_rte",
               "tcp_flags_mean","tcp_flags_median","tcp_flags_var",
               "tcp_flags_std","tcp_flags_entropy","tcp_flags_cv",
               "tcp_flags_cvq","tcp_flags_rte", "Label2"]

data = data[columns]

#Transformando o target em int
for i in range(0,len(data)):
  if data.loc[i,'Label2']=="normal":
    data.loc[i,'Label2']=0
  else: #data[i,'Label2']=='attack' :
    data.loc[i,'Label2']=1
data['Label2'] = data['Label2'].astype('int64')


#Utilizando modelo ATOM para geração de novas características
# https://towardsdatascience.com/deep-feature-synthesis-vs-genetic-feature-generation-6ba4d05a6ca5

# https://tvdboom.github.io/ATOM/v4.13/API/ATOM/atomclassifier/

#atom = ATOMClassifier(data, y="Label2", n_rows=1e3, verbose=2)
atom = ATOMClassifier(data, y="Label2", n_rows=1, verbose=2)
#atom.impute()
#atom.encode()

#Deep Feature Synthesis - DFS
print("============================DFS=======================")
atom.branch="dfs"

atom.feature_generation(
    strategy="dfs",
    n_features=543,
    verbose=1,
    operators=["add", "mul"],
)

#print("======DFS======")
#print(atom.dataset.head())

data2=atom.dataset
#print("data2\n", data2)

data2.to_csv('dataset_2.csv')
