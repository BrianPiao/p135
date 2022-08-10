import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("filtstar.csv")
#df.drop(["Unnamed:0","Unnamed:0.1"], axis = 1,inplace = True)

name = df["Star_name"].tolist()
mass = df["Mass"].tolist()
radius = df["Radius"].tolist()
distance = df["Distance"].tolist()
gravity = df["Gravity"].tolist()

plt.figure(figsize = (10,5))
plt.title("star solar mass")
plt.bar(name[0:9] ,mass[0:9])

plt.figure(figsize = (10,5))
plt.title("star solar radius")
plt.bar(name[0:9] ,radius[0:9])

plt.figure(figsize = (10,5))
plt.title("star solar distance")
plt.bar(name[0:9] ,distance[0:9])

plt.figure(figsize = (10,5))
plt.title("star solar gravity")
plt.bar(name[0:9] ,gravity[0:9])

plt.show()