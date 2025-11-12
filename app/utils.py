import pandas as pd
import os 
 

# Function to load a country's solar dataset
def load_data(country):
    """
    load solar dataset for the selected country
    The file names are:
       -benin-malanville-cleaned.csv
       -sierraleone-bumbuna.csv
       -togo_cp-cleaned.csv
    """
    file_map={
        "Benin":"benin-malanville-cleaned.csv",
        " Sierra":"sierraleone-bumbuna.csv",
        "Togo":"togo_cp-cleaned.csv"
    }
    # get absolute path for data 
    base_path=os.path.join(os.path.dirname(__file__),"..","data")

    filename=os.path.join(base_path,file_map.get(country,""))
    if os.path.exists(filename): # check the existance of the file
        df=pd.read_csv(filename) 
        # keep GHI only is it exists
        if "GHI" in df.columns:
            return df[["GHI"]].dropna()
        else:
            return pd.DataFrame({"Error":[f"File not found:{filename}"]})
def get_summary_stats(df):
    if "GHI" in df.columns:
        return df["GHI"].describe()
    return {"Error":"GHI column not found"}
