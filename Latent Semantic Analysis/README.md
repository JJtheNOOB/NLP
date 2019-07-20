## Latent Semantic Analysis (LSA)

- Application: Dimensionality Reduction
    - Improve processing time
    - Allows you to see your data (signal + noise)
    - Lets you to find similar / related words, remove redundancy
    - Polysemy: one words have multiple meanings (eg: bat, the animal and sports equip)
    - Information Retrieval (kinda like k-nearest neighbour search)
          - Google use this to find similar words and post search results on their search engine as well. 

## SVD - Sigular Vector Decompositio

- __Goal__: reduce redundency (eg: small and little)
     - Purpose: Saving space
     - Formula: __X(N by D) = U(shape N by D, feature importance, singular matrix) * S(shape D by D, covariance matrix) * V(Transposed, shape D by D, Eigen vectors)__
     - Advantage: 
          - Keep important data, drop the least important ones, since the singular matrix is ordered by importance (LSA / PCA)
          - Align signal and noise, easy to remove noise for the dataset         
     - How it works: cut off the right most part of z which is the least important ones

## Other dimensionality Reduction Techniques
     __Linear__
   - Independent Component Analysis (ICA): eg: decompose mix of sounds to sound(1) + sound(2) + noise
   - Factor Analysis
   
   __Non Linear__
   - t-SNE: 
   - Isomap
   - Local Linear Embedding
   - Spectral Embedding
   - Multi-Dimensional Scaling

