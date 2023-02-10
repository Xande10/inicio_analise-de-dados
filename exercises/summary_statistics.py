import pandas as pd

# Definindo o caminho do arquivo 'homelessness.csv' em uma variavel chamada url
url = (
    '~/python/projetinhos/homelessness.csv'
)

# Usando url para que o pandas leia os dados
tips_csv = pd.read_csv(url)
# Criando um DataFrame chamado homelessness
homelessness = pd.DataFrame(tips_csv)

# Métodos para analisar estatistica com pandas 

# Print the Mode from DataFrame
# print(homelessness["state_pop"].mean())

# Print the Median from DataFrame
# print(homelessness["state_pop"].median())

# Print the Maximum of a determined column
# print(homelessness["state_pop"].max())

# Print the minimum of a determined column
# print(homelessness["state_pop"].min())

# A custom IQR function
# def iqr(column):
#    return column.quantile(0.75) - column.quantile(0.25) 
# Print IQR of the state_pop column
# print(homelessness[["individuals", "family_members", "state_pop"]].agg(iqr))

# Get the cumulative sum of inviduals, add as sum_individuals 
homelessness["sum_individuals"] = homelessness["individuals"].cumsum()
print(homelessness[["individuals", "sum_individuals"]])
