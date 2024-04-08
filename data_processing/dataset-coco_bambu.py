import pandas as pd

# Carregar dataset
df_cocobambu = pd.read_csv('datasets/dataset-coco_bambu.csv')

# Informações sobre o conjunto de dados
print(df_cocobambu.info)

# Remover sentenças nulas
print("\nLinhas com valores nulos:\n", df_cocobambu.isnull().sum())
print('Removendo comentários nulos...')
df_cocobambu = df_cocobambu.dropna().reset_index(drop=True)

# Remover sentenças duplicadas
comentarios_duplicados = df_cocobambu.duplicated(subset='comentario').sum()
print("\nTotal de comentários duplicados:", comentarios_duplicados)
print('Removendo comentários duplicados...\n')
df_cocobambu = df_cocobambu.drop_duplicates(subset='comentario', keep='first').reset_index(drop=True)

# Remover colunas: restaurante, cidade e estado
df_cocobambu = df_cocobambu.drop(['restaurante', 'cidade', 'estado'], axis=1)

# Informações sobre o conjunto de dados
print(df_cocobambu.info)

# Salva o DataFrame final em um arquivo CSV
df_cocobambu.to_csv('datasets/dataset-coco_bambu-tratado.csv', index=False)