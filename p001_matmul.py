'''
p001. Matrix Multiplication

Question:
Implement matrix multiplication without using NumPy or any linear algebra libraries.

```
def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Return A @ B.
    Raise ValueError if dimensions are incompatible.
    """
```
Constraints:

* A is shape (m, k)

* B is shape (k, n)

* 1 ≤ m, k, n ≤ 200

Follow-ups (verbal):

* Time complexity?

* How would you optimize cache locality?

* How would you parallelize?

Hidden pitfalls:

* Non-rectangular input

* Empty matrices

* Avoid repeated list allocations inside loops

'''

def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Return A @ B.
    Raise ValueError if dimensions are incompatible.
    """
    m = len(A)
    if m==0:
      raise ValueError("A has 0 rows")

    n = len(A[0])    
    if n==0:
      raise ValueError("len(A) has 0 cols")

    o = len(B)
    if o==0 or o != n:
      raise ValueError(f"A has {n} cols but B has {o} rows, incompatiblel for matmul.")

    p = len(B[0])
    if p==0:
      raise ValueError("B has 0 cols.")

    # insert checks to ensure each row has same #cols.
    for i in range(m):
      if len(A[i]) != n:
        raise ValueError(f"matrix A: row{i} has {len(A[i])} cols but expected {n}")

    for j in range(n):
      if len(B[j]) != p:
        raise ValueError(f"matrix B: row{j} has {len(B[j])} cols but expected {p}")        

    C = [[0.0 for _ in range(p)] for _ in range(m)] # cannot do [[0.0]*p]*m <-- m references to the same row!


    # cache-optimized version:
    for i in range(m):
      Ai = A[i] 
      Ci = C[i]
      for j in range(n):
        Bj = B[j]
        Aij = Ai[j] # reuse, so you don't keep accessing each time.
        for k in range(p):
          Ci[k] += Aij * Bj[k]      

    # parallelization:
    # note that computing each row of C is independent. 
    # multi-threading is largely useless due to global binstruction lock in Python.
    # multi-processing can help: split a large A matix by its rows, let different processes process different rows of A. 

    # non-optimized version:
    # for i in range(m):      
    #     for k in range(p):
    #       for j in range(n):
    #         C[i][k] += A[i][j] * B[j][k] # walking down a column of B, but python lists are row-major!

    
    # matmul time complexity: O(mnp), space complexity: O(mp)
    return C
        