#llevar de lista a set
def list_to_set(list: list) -> set:
  result = set()
  
  for element in list:
    if not element in result:
      result.add(element)
  
  return result