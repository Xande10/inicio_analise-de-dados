import pandas as pd 

# Definindo o caminho do arquivo 'homelessness.csv' em uma variavel chamada url
url = (
    "~/python/projetinhos/homelessness.csv"
)

# Usando url para que o pandas leia os dados 
tips_csv = pd.read_csv(url)
# Criando um DataFrame chamado homelessness
homelessness = pd.DataFrame(tips_csv)

# Print the head of homelessness data
# print(homelessness.head())

# Print information about homelessness data
# print(homelessness.info())

# Print the shape of homelessness
# print(homelessness.shape)

# Print a description of homelessness data
# print(homelessness.describe())

# Print the values of homelessness
# print(homelessness.values)

# Print the column index of homelessness
# print(homelessness.columns)

# Print the row index of homelessness
# print(homelessness.index)