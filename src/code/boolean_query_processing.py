from sympy import sympify, to_dnf

def query_to_dnf(query):
    #Convertir la consulta a minúsculas
    query = query.lower()
    # Reemplazar los términos lógicos con las representaciones de sympy
    processed_query = query.replace("and", "&").replace("or", "|").replace("not", "~")

    # Convertir a expresión sympy y aplicar to_dnf
    query_expr = sympify(processed_query, evaluate=False)
    query_dnf = to_dnf(query_expr, simplify=True)

    return query_dnf
