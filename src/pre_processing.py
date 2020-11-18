def pre_processing_text2(corpus):
    lemmatizer = WordNetLemmatizer()
    #remove html tags
    corpus = re.sub(r'<.*?>', '', str(corpus))
    
    #remove non-alphanumeric characters
    corpus = re.sub(r'[^a-z A-Z 0-9 \s]', '', str(corpus))
    
    #remove duplicated spaces
    corpus = re.sub(r' +', ' ', str(corpus))
    
    #capitalization
    corpus = corpus.lower()
    
    #tokenization
    corpus = re.findall(r"\w+(?:'\w+)?|[^\w\s]", corpus)
    
    #lammatization
    corpus = [lemmatizer.lemmatize(c) for c in corpus]
    
    #remove punctuation
    corpus = [t for t in corpus if t not in string.punctuation]
    
    #remove stopwords
    #it makes the model worst
    #stopwords_ = stopwords.words("english")
    #corpus = [t for t in corpus if t not in stopwords_]
    
    corpus = ' '.join(corpus)

    return corpus