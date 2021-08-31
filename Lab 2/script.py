import numpy as np

def integration(m):

  E = 1 - (1 / np.exp(1))

  for j in range(1,m+1):
    E = 1 - (j * (E))

  return E

print(integration(10))