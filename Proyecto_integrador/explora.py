# %%
from scipy.io import arff
import pandas as pd
# %%
# Cargar archivos .arff
train_data, train_meta = arff.loadarff('./datasets/training.arff')
test_data, test_meta = arff.loadarff('./datasets/testing.arff')
# %%
# Convertir a DataFrame de Pandas
df_train = pd.DataFrame(train_data)
df_test = pd.DataFrame(test_data)
# %%
# Convertir columnas en formato bytes a strings si es necesario
df_train = df_train.applymap(lambda x: x.decode("utf-8") if isinstance(x, bytes) else x)
df_test = df_test.applymap(lambda x: x.decode("utf-8") if isinstance(x, bytes) else x)
# %%
# Mostrar primeras filas de cada conjunto
print("Train Data:")
print(df_train.head())
# %%
print("\nTest Data:")
print(df_test.head())
# %%
# Si quieres combinarlos en un solo DataFrame:
df_combined = pd.concat([df_train, df_test], ignore_index=True)
print("\nCombined Data:")
print(df_combined.head())
# %%
