## SVD - Sigular Vector Decomposition

- __Goal__: reduce redundency (eg: small and little)
     - Purpose: Saving space
     - Formula: __X(N by D) = U(shape N by D, feature importance, singular matrix) * S(shape D by D, covariance matrix) * V(Transposed, shape D by D, Eigen vectors)__
     - Advantage: Keep important data, drop the least important ones, since the singular matrix is ordered by importance
     - How it works: cut off the right most part of z which is the least important ones

