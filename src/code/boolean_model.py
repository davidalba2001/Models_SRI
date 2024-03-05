def get_matching_docs(query_dnf):
    global tokenized_docs, dictionary, corpus

    # Inicializar lista para almacenar los documentos coincidentes
    matching_documents = []

    # Recorrer cada componente conjuntiva de la FND de la consulta
    for conjunctive_term in query_dnf.args:
        conjunctive_terms = list(conjunctive_term.args) if isinstance(conjunctive_term, Or) else [conjunctive_term]
        conjunctive_docs = set(range(len(tokenized_docs)))  # Conjunto de todos los documentos

        # Verificar cada término en la componente conjuntiva
        for term in conjunctive_terms:
            term_str = str(term)
            if term_str.startswith("~"):
                term_str = term_str[1:]
                term_docs = set(dictionary[term_str])  # Documentos que no contienen el término
                conjunctive_docs = conjunctive_docs.difference(term_docs)
            else:
                term_docs = set(dictionary[term_str])  # Documentos que contienen el término
                conjunctive_docs = conjunctive_docs.intersection(term_docs)

        # Agregar los documentos que satisfacen la componente conjuntiva actual
        matching_documents.extend(list(conjunctive_docs))

    # Eliminar duplicados y ordenar los documentos coincidentes
    matching_documents = list(set(matching_documents))
    matching_documents.sort()

    return matching_documents
