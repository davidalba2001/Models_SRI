#dependencias
from lex_process import remove_stopwords_spacy, morphological_reduction_spacy
from utils import list_to_set
from process_corpus import load

#devolver la query parseada
def parse_query(query: list) -> list:
  return list(map(list_to_set, [clean_query(porcion) for porcion in query if len(porcion) != 0]))

#eliminar stopwords y signos de puntuacion
def clean_query(query_porcion: list) -> list:
  return morphological_reduction_spacy(remove_stopwords_spacy(query_porcion))
