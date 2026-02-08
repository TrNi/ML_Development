'''
p002. Sparse Matrix Multiplication

Question: Matrices are given in COO (Coordinate) format.

```
def sparse_matmul(
    A: list[tuple[int, int, float]],
    B: list[tuple[int, int, float]],
    m: int, k: int, n: int
) -> list[tuple[int,int,float]]:
    """
    A is mxk, B is kxn.
    Return the resulting sparse matrix.    
    """
```

Each tuple is (row, col, value).

Constraints:

* Number of non-zeros ≤ 10^5
* Output matrix can be dense

Follow-ups:

How would you return a sparse output?

What if both matrices are extremely sparse?
'''
from collections import defaultdict
def sparse_matmul(
    A: list[tuple[int, int, float]],
    B: list[tuple[int, int, float]],
    m: int, k: int, n: int
) -> list[tuple[int,int,float]]:
    """
    A is mxk, B is kxn.
    Return the resulting sparse matrix.    
    """
    if m<=0 or k<=0 or n<=0:
      raise ValueError(f"m,k,n = {m,k,n}, each should be a positive integer instead")

    # add additional check for all entries or check when looping.

    C = defaultdict(float)
    Ais = {}
    Bjs = {}

    for i,j,num in A:
      if i not in Ais:
        Ais[i] = defaultdict(float)
      Ais[i][j] += num # In COO matrices, duplicate entries should be summed. 

    for j,k,num in B:
      if j not in Bjs:
        Bjs[j] = defaultdict(float)
      Bjs[j][k] += num # In COO matrices, duplicate entries should be summed. 

    for i,Ai in Ais.items():
      for j in Ai:
        if j in Bjs:
          Aij = Ai[j]
          for k in Bjs[j]:
            C[(i,k)] += Aij * Bjs[j][k]

    Cfinal = []
    # for key,val in C.items():
    #   Cfinal.append((*key,val))
    cfinal = list(map(lambda x: (*x[0], x[1]), C.items()))
    return Cfinal
























# Expected approach

# Pre-index matrix B by row

# Only multiply matching (i, j) pairs

# Accumulate into output matrix
