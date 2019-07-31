import pandas as pd

data = pd.read_csv("replacewithfilename")
print("Number of Rows:" + len(data.index))
print("Number of Columns:" + len(data.columns))
