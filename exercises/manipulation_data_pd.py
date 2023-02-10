import pandas as pd

# Definindo o caminho do arquivo 'homelessness.csv' em uma variavel chamada url
url = (
    "~/python/projetinhos/homelessness.csv"
)

# Usando url para que o pandas leia os dados 
tips_csv = pd.read_csv(url)
# Criando um DataFrame chamado homelessness
homelessness = pd.DataFrame(tips_csv)

# Selecionando a coluna 'region'
# print(homelessness[['region']])

# Imprimindo os dados, ordenados pela coluna 'family_members'
# print(homelessness.sort_values(["family_members"]))
print(homelessness.sort_values(by="family_members" , ascending=True))

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