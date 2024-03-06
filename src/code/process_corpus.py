#dependencias
import ir_datasets
import spacy
from lex_process import *

#metodos auxiliares
from utils import *

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
  return list(map(list_to_set, morph_red))

#print(parse_corpus()[0])