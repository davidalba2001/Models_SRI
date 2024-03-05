#dependencias
import spacy
import nltk

#tokenizar
def tokenization_spacy(texts, nlp):
  return [[token for token in nlp(doc)] for doc in texts]

#remover signos de puntuacion
def remove_noise_spacy(tokenized_docs):
  return [[token for token in doc if token.is_alpha] for doc in tokenized_docs]

#remover las palabras comunes como preposiciones y conjunciones
def remove_stopwords_spacy(tokenized_docs):
  stopwords = spacy.lang.en.stop_words.STOP_WORDS
  return [
      [token for token in doc if token.text not in stopwords] for doc in tokenized_docs
  ]
  
#analisis morfologico de las palabras
def morphological_reduction_spacy(tokenized_docs, use_lemmatization=True):
  stemmer = nltk.stem.PorterStemmer()
  return [
    [token.lemma_ if use_lemmatization else stemmer.stem(token.text) for token in doc]
    for doc in tokenized_docs
  ]  
  

