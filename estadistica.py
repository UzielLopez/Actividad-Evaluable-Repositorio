# %%
import pandas as pd
import numpy as np

#Definir tamaño del dataset
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
print("Tamaño del data set: ", len(df.index), " entradas" )

# %%
#Imprimir las variables presentes en el dataser
print("Variabless presentes: ")
for variable in df.columns:
    print(variable)

# %%
#Verificar máximos y mínimos de las variables (rango)
for i in range(len(df.columns)):
    print(str(df.columns[i]) + " --- Máximo: ", df.max, )



# %%
for i in range(len(df.columns)):
    print(str(df.columns[i]) + " --- Media: ", (df.iloc[i]).mean(), "Mediana: ", (df.iloc[i]).median(),"Moda: ", (df.iloc[i]).mode())


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
