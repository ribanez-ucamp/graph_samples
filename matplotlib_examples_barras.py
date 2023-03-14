import matplotlib.pyplot as plt

# plt es el alias

fig, ax = plt.subplots()

# Crea 2 objetos: una Figure fig (figura) que es un contenedor de todo 
# lo que verás en el gráfico y los Axes ax (ejes) que contienen la información 
# a graficar.

# La función matplotlib.pyplot.subplots crea una figura y 
# uno (o varios) conjunto de ejes, devolviendo una referencia a la figura y a los ejes. Por defecto -si no se especifica otra cosa- crea un único conjunto de ejes:

# A continuación se definen los conjuntos de datos que servirán para
# mostrar una opción de gráficos

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
# Etiquetas que se añaden a la leyenda descriptiva
bar_labels = ['red', 'blue', '_red', 'orange']
# Colores del conjunto, en este caso de las frutas o barras
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

# Axes.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

# METODOS

# Añade un título con el contenido de la cadena titulo al eje y de ax

ax.set_ylabel('fruit supply')

# Se añade el título en la parte superior de la gráfica

ax.set_title('Fruit supply by kind and color')

# Se añade una leyenda 

ax.legend(title='Fruit color')

plt.show()

