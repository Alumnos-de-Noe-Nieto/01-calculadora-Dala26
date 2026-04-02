"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""
alfabeto_romano = set("IVXLCDM")

def validar_simbolos(cadena: str) -> bool:
    cadena_limpia = cadena.strip() # Eliminar los espacios en blanco al inicio y al final de la cadena

    if (cadena_limpia == ""): # Si la cadena está vacía después de eliminar los espacios,
        return False # No es válida porque no contiene ningún símbolo romano
    return set(cadena_limpia).issubset(alfabeto_romano) #Verificar si todos los caracteres de la cadena están en el alfabeto romano

    raise NotImplementedError()

""" zona de pruebas
print(validar_simbolos("XIV")) #True
print(validar_simbolos("MCMXCIV")) #True
print(validar_simbolos("ABCD")) #False
print(validar_simbolos("X-IV")) #False
print(validar_simbolos("")) #False
print(validar_simbolos("  XIV  ")) #True
"""
