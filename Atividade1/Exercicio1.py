import numpy as np

# Coeficientes das equações
A = np.array([[100, 50, 0],
              [30, 30, 30],
              [230, 130, 30]])

# Lado direito das equações
B = np.array([2000, 1500, 5500])

# Resolver o sistema de equações
X = np.linalg.solve(A, B)

# Arredondar as soluções para números inteiros
X_int = np.round(X).astype(int)

print("Número de caminhões de cada tipo:")
print("Tipo I:", X_int[0])
print("Tipo II:", X_int[1])
print("Tipo III:", X_int[2])
