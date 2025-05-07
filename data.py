# ----------- Download Libraries & Import Dataset ---------------
# %%
import os
import pandas as pd

def load_data(filename='marketing_touchpoints.csv'):
    base_path = os.path.join(
    "C:\\Users", "LUQMAAN", "OneDrive", "Documents", "gitprojects",
    "Marketing Funnel & Attribution Analysis",
    "marketing-analytics-performance-analyst"
    )

    file_path = os.path.join(base_path,filename)
    df = pd.read_csv(file_path)
    return df




if __name__ == "__main__":
    df=load_data()
    print(df.head())