# ----------- Download Libraries & Import Dataset ---------------
# %%
import os
import pandas as pd

base_path = os.path.join(
    "C:\\Users", "LUQMAAN", "OneDrive", "Documents", "gitprojects",
    "Marketing Funnel & Attribution Analysis",
    "marketing-analytics-performance-analyst"
)

# Add the filename at the end
file_path = os.path.join(base_path, "marketing_touchpoints.csv")
df = pd.read_csv(file_path)


if __name__ == "__main__":
    print(df.head())
    print(df.describe())