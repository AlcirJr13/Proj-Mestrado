import pandas as pd
from atom import ATOMClassifier

data = pd.read_csv("dataset_descriptor.csv")
#print(data.head())

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

for i in range(0,len(data)):
  if data.loc[i,'Label2']=="normal":
    data.loc[i,'Label2']=0
  else: #data[i,'Label2']=='attack' :
    data.loc[i,'Label2']=1


data['Label2'] = data['Label2'].astype('int64')
print(data.info())

atom = ATOMClassifier(data, y="Label2", n_rows=1e3, verbose=2)
atom.impute()
atom.encode()

#print(atom.dataset.head())

print(atom.run(models="LGB", metric="accuracy"))


print("============================DFS=======================")
atom.branch="dfs"

atom.feature_generation(
    strategy="dfs",
    n_features=543,
    verbose=1,
    operators=["add", "mul"],
)

print("======DFS======")
print(atom.dataset.head())

atom.run(models="LGB_dfs")


print("============================GFS=======================")
atom.branch = "gfg_from_master"
atom.feature_generation(
    strategy="GFG",
    n_features=543,
    operators=["add", "mul"],
)

#print(atom.genetic_features) #visão geral das características recém-geradas, seus nomes e pontuação obtida durante o algoritmo genético

print("======GFS======")
print(atom.dataset.head())

atom.run(models="LGB_gfg")


print("RESULTADOS")
print(atom.results)

atom.plot_roc()

with atom.canvas(1, 3, figsize=(20, 8)):
    atom.lgb.plot_feature_importance(show=10, title="LGB")
    atom.lgb_dfs.plot_feature_importance(show=10, title="LGB + DFS")
    atom.lgb_gfg.plot_feature_importance(show=10, title="LGB + GFG")
