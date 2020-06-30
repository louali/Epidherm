import pandas as pd

def ConvertDataFrame(mat):
    for i in mat:
        i["fam_name"] = i["family"]["name"]
        i["fam_id"] = i["family"]["id"]
        i["masse_surfacique"] = i["details"]["masse_surfacique"]
        i["masse_combustible"] = i["details"]["masse_combustible"]
        del i["details"]
        del i["family"]
    return(pd.DataFrame(mat))

def GroupByFam(mat):
    data = ConvertDataFrame(mat)
    group = data.groupby("fam_name")
    df = pd.DataFrame()
    df['MAX_Masse_Surfacique'] = group['masse_surfacique'].max()
    df['MIN_Masse_Surfacique'] = group['masse_surfacique'].min()
    df['MAX_Masse_Combustible'] = group['masse_combustible'].max()
    df['MIN_Masse_Combustible'] = group['masse_combustible'].min()
    df['MIN_Masse_Combustible'] = group['masse_combustible'].min()
    df['Nb_mat'] = group['masse_combustible'].count()
    return(df.to_json())