import matplotlib.pyplot as plt

# Colección clave y valor

# Colección - Diccionario

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}

# Clave

names = list(data.keys())

# Valor

values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

# Machine learning
# (nrows=1, ncols=3, figsize=(9, 3), sharey)
# El parámetro sharey=True permite compartir el eje Y entre los subplots

axs[0].bar(names, values)               # Barra
axs[1].scatter(names, values)           # Dispersión
axs[2].plot(names, values)              # Trama o línea
fig.suptitle('Categorical Plotting')

plt.show()