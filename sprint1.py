import sys
import pandas as pd

filename = sys.argv[1]

print(filename)

data = pd.read_csv(filename)
print("Number of Rows:" + len(data.index))
print("Number of Columns:" + len(data.columns))
