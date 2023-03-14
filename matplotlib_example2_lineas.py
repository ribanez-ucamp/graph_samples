import matplotlib.pyplot as plt

# A continuación se definen los conjuntos de datos que servirán para
# mostrar una opción de gráficos

# Estados de ánimo de perros y gatos relacionados con actividades

cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()

# Crea 2 objetos: una Figure fig (figura) que es un contenedor de todo 
# lo que verás en el gráfico y los Axes ax (ejes) que contienen la información 
# a graficar.

# La función matplotlib.pyplot.subplots crea una figura y 
# uno (o varios) conjunto de ejes, devolviendo una referencia a la figura y a los ejes. Por defecto -si no se especifica otra cosa- crea un único conjunto de ejes:

#ax.plot = gráfica de líneas
#actividades relacionadas, primero con el perro y después con el gato

ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.show()
