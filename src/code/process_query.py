#dependencias
from lex_process import remove_stopwords_spacy, morphological_reduction_spacy
from process_corpus import word_index, doc_value

#devolver la query parseada
def parse_query(query: list) -> list:
  return [clean_query(porcion) for porcion in query if len(porcion) != 0]

#eliminar stopwords y signos de puntuacion
def clean_query(query_porcion: list) -> list:
  return morphological_reduction_spacy(remove_stopwords_spacy(query_porcion))

#devolver los documentos de la query con sus respectivos valores en bits
def query_porcion_values(query: list) -> list:
  parts = parse_query(query)
  words_corpus = word_index()
  return [doc_value(doc, words_corpus) for doc in parts]
 
