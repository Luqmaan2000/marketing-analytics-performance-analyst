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
# %%
print("Shape:", df.shape)
# %%
df.head()
# %%
df.info()
# %%
df.isnull().sum()
df.duplicated().sum()
# %%
df['conversion'].value_counts()
df.groupby('channel')['conversion'].mean()
# %%
df['conversion_value'].describe()
df.groupby('channel')['conversion_value'].sum().sort_values(ascending=False)
