# Natural Language Processing

## Some Typical steps for text processing:
   - __Spell checking__
      - too many typos will lose signal in the text
      - tend to overfit to edgge cases of unique spelling mistakes
   - __Industry specific Abbrevation Conversion__
      - Important to give your model more understanding of the indutry specific langugage
   - __Remove Stop words__
      - Reduce size of inputs, go easy on algorithm
   - __Remove Punctuation__
      - Reduce size of inputs, go easy on algorithm
   - __Stemming or Lemmatization__
      - Chopping off words to their original form: snowball & porter
      - Remember to preserve the industry specific words
   - __Tokenisation and Conversion to Numbers__
      - The process of breaking words into vectors that machine can understand __aka Tokens__
      - Bag of Words (BOW)
        - Retains word count, ignore grammar
        - Results in a table where each column represents a unique word
        - The resulting table can be fed into a model to make predictions
      - TF - iDF (Term frequency - inverse document frequency)
        - Weights number counts by how important the words are to a specific document
