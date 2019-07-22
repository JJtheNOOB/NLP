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
        - Weights number counts by how important the words are to documents
        - raw word count / Document count

## N-Grams
 - a sequence of N consecutive words
 - aka Markov Assumption (the word depends on the previous n words)
 - Usage: 
     - Word prediction (given the last n-1 words, model the distribution of the Nth word)
      - Such as article spinner (Replacing part of the article with new words)
 - Usually do bigrams (N = 2, first-order Markov) and trigrams (n = 3, second order Markov)
   - Better performance on the unseen data (larger training samples)
 - If N is too big, say n = 10, some sentences would not be that long
 - Formula ( p(Wt | Wt-1, Wt-2, ... Wt-n+1) = count(Wt-n+1 -> Wt) / count(Wt-n+1 -> Wt-1) )
   - counting of entire sequence / counting of entire sequence excluding the last word
 - Not only looking at previous words, can also look at future words
