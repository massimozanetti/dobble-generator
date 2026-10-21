""" A script that generates the lines of a finite projective plane of order p^m, which is equivalent to a general Dobble game (the classic one corresponds to p=7, m=1).

"""

import sys
import numpy as np
import galois
np.set_printoptions(threshold=sys.maxsize)



def dobble(p, m):

  Q = p**m          # order of the finite field
  N = Q*(Q+1)+1     # number of points and lines (symbols and cards)
  F = galois.GF(Q)  # initializing the Galois Field of order Q=p^m
  print(f'Dobble of order:   {Q}')
  print(f'Symbols per card:  {Q+1}')
  print(f'Number of cards:   {N}')

  #Symbol-set S of N elements indexed linearly
  dform = '{{:0{}d}}'.format(len(str(N)))
  #S[i] for i=0,...,N-1 is a symbol
  S = np.array([dform.format(s) for s in range(1, N+1)])
  print('Symbols: \n', S)  
  #The first Q+1 symbols are the "b_0, b_1, ..., b_Q"
  B = np.arange(0, Q+1)
  #Subsequent symbols are wrapped into matrix A
  A = np.arange(Q+1, N).reshape((Q, Q))
  #List of arrays indexing the symbols set of each card
  index = []
  #Fill matrix A0 by rows
  index.append(B)
  for l in range(0, Q):
    row = [ B[0], *[ A[l, j] for j in range(0, Q) ] ]
    index.append(row)
  #Fill matrices A1, A2, ..., AQ
  for k in range(1, Q+1):
    #Fill matrix by rows
    for l in range(0, Q):
      row = [ B[k], *[ A[j, F(l)+F(j)*F(k-1)] for j in range(0, Q) ] ]
      index.append(row)
  #Convert indexes to symbols
  deck = np.array([S[q] for q in index])
  #Print the Dobble deck
  print('Deck: \n',deck)




if __name__ == "__main__":
    
    p = sys.argv[1]
    m = sys.argv[2]

    dobble(p, m)
