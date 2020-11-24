# importando la librería numpy, para trabajar más fácilmente
# con vectores, los cuales simplifican los cálculos numéricos.
# Luego utilizamos la instrucción def para definir la función,
# que este caso se va a llamar f y va a tener como único 
# parámetro al objeto x. Esta función nos va a devolver el 
# valor de la raíz cuadrada de # x+2
import numpy as np  

def f(x):
    return np.sqrt(x + 2)

x = np.array([-2, -1, 0, 2, 4, 6])  # Creando el vector de valores de x
y = f(x)
