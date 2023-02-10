# Importando a biblioteca pandas
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

# Selecionando a coluna 'region'
# print(homelessness[['region']])

# Imprimindo os dados, ordenados pela coluna 'family_members'
# print(homelessness.sort_values(["family_members"]))

# Filter for rows where individuals is greater than 10000
# ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
# print(ind_gt_10k)

# Subset for rows in South Atlantic or Mid-Atlantic regions
# regions = ["South Atlantic", "Mid-Atlantic"]
# condition = homelessness["region"].isin(regions)
# south_mid_atlantic = homelessness[condition]
# print(south_mid_atlantic)

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"] 

# See the result
print(homelessness)