import nltk

from nltk.stem import WordNetLemmatizer

#Setting up lemmetizer, transform words to their original form
word_lemmetizer = WordNetLemmatizer()

#Read in all the titles and save them into a list called titles
titles = [line.rstrip() for line in open('C:/Users/lianj/Desktop/Udemy/NLP_machine_learning_examples-master/nlp_class/all_book_titles.txt')]

#Read in stopwords and make them into a set
stopwords = set(w.rstrip() for w in open('C:/Users/lianj/Desktop/Udemy/NLP_machine_learning_examples-master/nlp_class/stopwords.txt'))
#Append additional stop words into the set
stopwords = stopwords.union({
    'introduction', 'edition', 'series', 'application',
    'approach', 'card', 'access', 'package', 'plus', 'etext',
    'brief', 'vol', 'fundamental', 'guide', 'essential', 'printed',
    'third', 'second', 'fourth', })

#Now start processing the words
def tokenizer(s):
    s = s.lower() #Make everything in lower case
    tokens = nltk.tokenize.word_tokenize(s) #split string into words
    tokens = [t for t in tokens if len(t) > 2] #Remove short words that is less than 2 characters long (not going to be so usefyul)
    tokens = [word_lemmetizer.lemmatize(t) for t in tokens] #Now we starts to lemmetize our tokens
    tokens = [t for t in tokens if t not in stopwords]  #Remove all the stop words
    tokens = [t for t in tokens if not any(c.isdigit() for c in t)] #looping through all the tokens and its characters to remove the numbers
    return tokens

word_index_map = {}
current_index = 0
all_tokens = []
error_count = 0
for title in titles:
    try:
        title = title.encode('ascii', 'ignore').decode('utf-8') # QA: this will throw exception if bad characters
        tokens = tokenizer(title)  #process the title
        all_tokens.append(tokens)  #Append the tokens from the titles into tokens list
        for token in tokens:
            if token not in word_index_map:
                word_index_map[token] = current_index
                current_index += 1
    except Exception as e:
        print(e)
        print(title)
        error_count += 1

print(index_word_map)