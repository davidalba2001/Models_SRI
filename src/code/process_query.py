#dependencias
from lex_process import *
from process_corpus import *
import spacy

#metodos auxiliares
from utils import list_to_set

#devolver la query parseada
def parse_query(query: list) -> list:
  #cargar el modulo de spacy para trabajar con lenguaje natural
  nlp = spacy.load("en_core_web_sm")
  
  #procesar la query
  tok = tokenization_spacy(query, nlp)
  rem_noise = remove_noise_spacy(tok)
  rem_sw = remove_stopwords_spacy(rem_noise)
  morph_red = morphological_reduction_spacy(rem_sw)
  return list(map(list_to_set, morph_red))

#devolver los documentos
def rec_docs(query):
  docs = load()
  data_query = parse_query(query)
  data_corpus = parse_corpus()
  result = set()
  
  for doc in data_corpus:
    for part in data_query:
      if part.issubset(doc):
        result.add(doc)
        break
  
  return result
