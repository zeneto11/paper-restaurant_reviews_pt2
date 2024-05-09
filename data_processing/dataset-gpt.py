import os
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

# Define o diretório contendo os arquivos de texto
txt_directory = 'datasets/gpt'

# Lista de arquivos de texto com suas categorias associadas
text_files = [
    ('gpt-ambiente.txt', 'ambiente'),
    ('gpt-bebida.txt', 'bebida'),
    ('gpt-comida.txt', 'comida'),
    ('gpt-geral.txt', 'geral'),
    ('gpt-localizacao.txt', 'localização'),
    # ('gpt-outros.txt', 'outros'),
    ('gpt-preco.txt', 'preço'),
    ('gpt-servico.txt', 'serviço'),
]

# Inicializa uma lista para armazenar os dados
data = []

# Processa cada arquivo de texto
for file_name, category in text_files:
    file_path = os.path.join(txt_directory, file_name)
    
    # Lê as sentenças do arquivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file.readlines()]
    
    # Adiciona os dados à lista
    data.extend([(sentence, category) for sentence in sentences])

# Cria um DataFrame com os dados coletados
combined_df = pd.DataFrame(data, columns=['sentenca', 'categoria'])

# Codifica as categorias em formato binário
mlb = MultiLabelBinarizer()
categorias_matriz = mlb.fit_transform(combined_df['categoria'].apply(lambda x: [x]))

# Cria um DataFrame com as colunas de categoria binárias
df_final = pd.concat([combined_df['sentenca'], pd.DataFrame(categorias_matriz, columns=mlb.classes_)], axis=1)

# Conta as ocorrências de cada categoria
ocorrencias = df_final.iloc[:, 1:].sum().sort_values(ascending=False)

# Salva o DataFrame final em um arquivo CSV
df_final.to_csv('datasets/dataset-GPT-multilabel.csv', index=False)

# Mostra as ocorrências em ordem decrescente
print(ocorrencias)

print('Arquivo CSV salvo com sucesso.')