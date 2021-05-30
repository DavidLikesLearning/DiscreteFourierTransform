import numpy as np
def wizardry(lst):
  N = len(lst)
  out =[]
  for k in range(N):
    w = np.exp(np.complex(0,-2*np.pi*k/N))
    quak = np.zeros((N,1))
    for j in range(N):
      quak[j] = (lst[j]*np.power(w,j))
    out.append(np.sum(quak))
  return out
  