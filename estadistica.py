# %%
import pandas as pd
import numpy as np
import seaborn as sns

#Definir tamaño del dataset
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
print("Tamaño del data set: ", len(df.index), " entradas" )

# %%
#Variables presentes en el dataset
print("Variabless presentes: ")
for variable in df.columns:
    print(variable)

# %%
#Verificar máximos y mínimos de las variables (rango)
for i in range(len(df.columns)): #Ignoramos las primeras dos columnas, pues no son datos cuantitativos
    print(str(df.columns[i]) + " --- Máximo: ", df.iloc[:, i].max(), "Mínimo: ", df.iloc[:, i].min())
    print("-"*40)



# %%
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no  son datos cuantitativos
    print(str(df.columns[i]) + " --- Media: ", (df.iloc[:, i]).mean(), "Mediana: ", (df.iloc[:, i]).median(),"Moda: ", (df.iloc[:, i]).mode()[0])
    print("-"*60)

#print("Mínimos: ", df.min())
#print("Máximos:", df.max())
#print(df.quantile([0.25, 0.5, 0.75]))
#df.head() #primero cinco o numero especifico
#df.tail() #ultimos cinco o numero especifico
#df.sample() #uno o numero especificos al azar
#df.info()
#print("Moda: ")
#df.mode()
#df.tail(3)


# %%
df.describe()
#df.mode()


print("\n\n")

# Código para obtener la desviación estandar de los datos
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no  son datos cuantitativos
    print(str(df.columns[i]) + " --- Desviación estandar: ", (df.iloc[:, i]).std())
    print("-"*60)

# %%
#print(np.percentile(df,1))

print("\n\n")

# Código para obtener el cuartil 1 de los datos
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no  son datos cuantitativos
    print(str(df.columns[i]) + " --- Cuartil 1: ", np.percentile((df.iloc[:, i]),25))
    print("-"*60)
print()
# Código para obtener el cuartil 2 de los datos
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no  son datos cuantitativos
    print(str(df.columns[i]) + " --- Cuartil 2: ", np.percentile((df.iloc[:, i]),50))
    print("-"*60)
print()
# Código para obtener el cuartil 1 de los datos
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no  son datos cuantitativos
    print(str(df.columns[i]) + " --- Cuartil 3: ", np.percentile((df.iloc[:, i]),75))
    print("-"*60)

"""
Tarea 3. Actividad devaluable: Mapas de calor y boxplots 
Visualizaciones de los datos. Cada linea representa una gráfica distinta.
Para evitar que se junten todas en una misma gráfica, recomendamos solo des-comentar una gráfica a la vez
"""

# %%
#df_variables_cuantitativas = df.drop(["customer", "order", "weekday", "hour"], axis = 1)
#sns.heatmap(data = df_variables_cuantitativas.corr(), annot = True)

#sns.scatterplot(x = "order", y= "discount%", data = df) #discount tiene outlayers
#sns.scatterplot(x = "discount%", y = "total_items", data = df)
#sns.scatterplot(x = "discount%", y = "Pets%", data = df)
#df_sin_ti_outliers  = df [df["total_items"] <= 75]
#sns.histplot(x = "total_items", data = df)
#sns.boxplot(x= "total_items", data = df)
#sns.boxplot(x= "discount%", data = df)
df_tmp = (df.groupby("weekday"))["order"].count()
df_tmp.plot.bar()
#sns.barplot(data  = df_tmp)

#sns.scatterplot(x= "weekday", y = "total_items", data = df)
#sns.histplot(y = "total_items",  data = tmp)


# %%
#sns.scatterplot(x= "total_items", y = "discount%", data = df, hue = "weekday")
#sns.scatterplot(x = "discount%", y = "Food%", data = df, hue = "weekday")


# %%
