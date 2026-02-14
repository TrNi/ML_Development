'''
p004. K-Means Clustering 

Question:

Implement K-Means clustering using Euclidean distance.

def kmeans(
    X: ndarray,
    k: int,
    max_iters: int = 100,
    tol: float = 1e-4
) -> tuple[list[int], ndarray]:
    """
    Returns:
      labels: length N
      centroids: kxd
    """

Constraints:

- N ≤ 10^4, d ≤ 50
- No sklearn. Numpy okay for arrays.

Expected features:

- Random centroid initialization
- Early stopping via centroid shift
- Handle empty clusters

Follow-ups:

- Time complexity per iteration?
- K-Means++?
- How does this relate to EM?
'''