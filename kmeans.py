# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# ================================
# Determina el número K óptimo
# ================================
dfp = df[["Food%","total_items"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee) # Número óptimo para K
print(f"Number of clusters suggested by knee method: {k}")

# ================================
# Ya con el K, calculamos los clusters
# ================================
kmeans = KMeans(n_clusters=k).fit(df[["Food%","total_items"]])

# Generar el scatterplot con la organización de los clusters
sns.scatterplot(data=df, x="Food%", y="total_items", hue=kmeans.labels_)
plt.show()

# %%

cluster0 = df[kmeans.labels_ == 1]
cluster0.describe()

# %%
