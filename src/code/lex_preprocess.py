import nltk  # Importar la biblioteca nltk

# Función para tokenizar documentos usando NLTK
def tokenization_nltk(texts):
    # Tokeniza cada documento en la lista de textos
    tokenized_docs = [nltk.tokenize.word_tokenize(doc) for doc in texts]
    return tokenized_docs

# Función para eliminar ruido de los documentos tokenizados usando NLTK
def remove_noise_nltk(tokenized_docs):
    # Convierte cada palabra a minúsculas y elimina las que no son alfabéticas
    tokenized_docs = [
            [word.lower() for word in doc if word.isalpha()] for doc in tokenized_docs]
    return tokenized_docs

# Función para eliminar las palabras vacías de los documentos tokenizados
def remove_stopwords(tokenized_docs):
    stop_words = set(nltk.corpus.stopwords.words('english'))  # Obtiene las palabras vacías en inglés
    # Elimina las palabras vacías de cada documento
    tokenized_docs = [
        [word for word in doc if word not in stop_words] for doc in tokenized_docs
    ]
    return tokenized_docs

# Función para reducción morfológica usando NLTK
def morphological_reduction_nltk(tokenized_docs, use_lemmatization=True):
    # Si use_lemmatization es True, utiliza lematización, de lo contrario, utiliza la derivación de palabras
    if use_lemmatization:
        lemmatizer = nltk.stem.WordNetLemmatizer()  # Inicializa el lematizador de WordNet
        # Lematiza cada palabra en cada documento
        tokenized_docs = [
            [lemmatizer.lemmatize(word) for word in doc]
            for doc in tokenized_docs
        ]
    else:
        stemmer = nltk.stem.PorterStemmer()  # Inicializa el stemmer de Porter
        # Aplica la derivación de palabras a cada palabra en cada documento
        tokenized_docs = [
            [stemmer.stem(word) for word in doc] for doc in tokenized_docs
        ]

    return tokenized_docs

def preprocess_documents(documents):
    # Tokenización
    tokenized_docs = tokenization_nltk(documents)

    # Eliminación de ruido (solo tokens alfabéticos)
    tokenized_docs = remove_noise_nltk(tokenized_docs)
    
    # Eliminación de stopwords
    tokenized_docs = remove_stopwords(tokenized_docs)
    
    # Reducción Morfológica
    tokenized_docs = morphological_reduction_nltk(tokenized_docs)

    return tokenized_docs