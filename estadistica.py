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
for i in range(2, len(df.columns)): #Ignoramos las primeras dos columnas, pues no son datos cuantitativos
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

