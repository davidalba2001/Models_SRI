#dependencias
import ir_datasets
import spacy
from lex_process import *

#cargar el corpus
def load() -> list:
  datasets = ir_datasets.load("cranfield")
  docs = [doc.text for doc in datasets.docs_iter()]
  return docs

#devolver el corpus parseado
def parse_corpus() -> list:
  #cargar el corpus y el modulo de spacy para trabajar con lenguaje natural
  docs = load()
  nlp = spacy.load("en_core_web_sm")

  #procesar el documento
  tok = tokenization_spacy(docs, nlp)
  rem_noise = remove_noise_spacy(tok)
  rem_sw = remove_stopwords_spacy(rem_noise)
  morph_red = morphological_reduction_spacy(rem_sw)
  return morph_red

#devolver los documentos con sus respectivos valores en bits
def docs_values() -> list:
  docs = parse_corpus()
  words_corpus = word_index()
  return [doc_value(doc, words_corpus) for doc in docs]
 
#saber el numero de bit de cada palabra
def word_index() -> dict:
  docs = parse_corpus() #corpus
  words_set = set() #palabras del corpus sin repetir
  result = {}
  i = 0

  for doc in docs:
    for word in doc:
      if not word in words_set:
        words_set.add(word)
        result[word] = i
        i += 1

  return result

#valor de un documento
def doc_value(doc: list, words_corpus: dict) -> int:
  words_set = set() #palabras del documento sin repetir
  result = 0
  
  for word in doc:
    if not word in words_set:
      words_set.add(word)
  
  for word in words_set:
    result += 2 ** words_corpus[word]
  
  return result