# Natural Language Processing

## Libraries avaliable
- [NLTK](https://www.nltk.org/) 1.5G Nautral Language Toolkit
- [TextBlob](https://textblob.readthedocs.io/en/dev/) Good for beginners
- [Spacy](https://spacy.io/) Industrial-Strength Natural Language Processing
- Differences: https://www.quora.com/What-is-the-use-of-NLTK-and-TextBlob-What-is-the-difference-between-both-And-for-text-analysis-which-tool-is-better

## Some Typical steps for text processing:
   - __Spell checking__
      - too many typos will lose signal in the text
      - tend to overfit to edge cases of unique spelling mistakes
      - For example:
      ```
      from textblob import TextBlob
      text = TextBlob("He is a gret peron").correct()
      ```
   - __Industry specific Abbrevation Conversion__
      - Important to give your model more understanding of the indutry specific langugage
   - __Remove Stop words__
      - Reduce size of inputs, go easy on algorithm
      - For example:
      ```
      from nltk.corpus import stopwords
      stop_words = set(stopwords.words("english"))  #179 of them, you can potentially append more to this set
      ```
   - __Remove Punctuation__
      - Reduce size of inputs, go easy on algorithm
      - For example: 
      ```
      re.findall(r"[a-z]+(?:[a-z]+)?", s.lower())  #Returns a list of removed punctuation text
      ```
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
        - Raw word count / Document count
        - Not good for word analogies

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
 
 ## Word Embeddings
   - Vectors that represents a word
   - Embedding a categorical entity (a word) into a vector space

## Distance Measurements between pieces of text
   - __Jaccard Distance__: The Jaccard distance between two sets of values is defined as the size of their intersection divided by the size of their union, i.e. the number of the values they have in common divided by the total number of unique values that appear in both sets.
   - __Levenshtein distance__: The Levenshtein distance between two texts is a string distance metric that indicates the number of single-character changes required to convert the one string to the other.Referring to the [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy) Library
   - [__Scipy's cdist__](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.cdist.html) also allow you to measure similarities between numerical encoded categorical variables. Might not be used in NLP process but it is good to know. 
