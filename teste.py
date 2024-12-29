import pandas as pd
import matplotlib.pyplot as plt

lojas = ['Neoenergia', 'Kempetro Engenharia', 'Lotus LTDA', 'Petro']

vendas_2022 = {
    'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

df = pd.DataFrame(vendas_2022, index=lojas)

cores = ["green", "yellow", "green", "black"]

soma = df.sum(axis=1)

df_maior = df.assign(Total=soma).sort_values('Total', ascending=True)

fig, ax = plt.subplots(figsize=(12, 5))

ax.barh(df_maior.index, df_maior['Total'], color=cores)

for i, v in enumerate(df_maior['Total']):
    ax.text(v + 20, i, str(v), va='center', fontsize=10, color='black')

ax.set_title("Vendas durante o ano de 2022", loc="left", fontsize=12)
ax.set_xlabel("Número de vendas")
ax.set_ylabel("Lojas")
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=8)

fig.savefig("grafico_loja.png", transparent=False, dpi=300)

plt.show()
