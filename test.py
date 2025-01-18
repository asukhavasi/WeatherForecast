import pandas as pd
import matplotlib.pyplot as plt
dict = {"days":[1,2,3,4,5],"temp":[20,25,15,28,20]}

df = pd.DataFrame.from_dict(dict)

df.plot(x='days',y='temp',figsize=(15,3))