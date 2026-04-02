"""
Nivel 3: Validación de repeticiones V/L/D.

Los símbolos V, L y D NO pueden repetirse.
Ejemplos válidos: V, L, D, MCMXCIV
Ejemplos inválidos: VV, LL, DD
"""
SIMBOLOS_UNICOS = {'V', 'L', 'D'}
MAX_REPETICIONES_VLD = 1

def validar_repeticiones_vld(cadena: str) -> bool:
    """
    Valida que los símbolos V, L y D no se repitan (máximo 1).

    Nivel 3: Análisis Sintáctico - Repeticiones de símbolos únicos

    💡 PISTA: Verifica si existen los patrones "VV", "LL", "DD"
    💡 PISTA: Si encuentras cualquier patrón de 2+ repeticiones, retorna False
    💡 PISTA: Recuerda: VV, LL, DD son INVÁLIDOS

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-2

    Returns:
        bool: True si no hay repeticiones de V/L/D, False en caso contrario

    Examples:
        >>> validar_repeticiones_vld("V")
        True
        >>> validar_repeticiones_vld("VV")
        False
        >>> validar_repeticiones_vld("MCMXCIV")
        True
        >>> validar_repeticiones_vld("LL")
        False
        >>> validar_repeticiones_vld("DD")
        False
    """
    for simbolo in SIMBOLOS_UNICOS: #un "for anidado"
        restriccion = simbolo * (MAX_REPETICIONES_VLD + 1) # contara las veces que se repite el simbolo (no mas de 1)

        if restriccion in cadena: # si el simbolo se repite mas de 1 vez, la cadena no es valida
            return False
    return True
    raise NotImplementedError()

''' zona de pruebas
print(validar_repeticiones_vld("V")) #True
print(validar_repeticiones_vld("VV")) #False
print(validar_repeticiones_vld("MCMXCIV")) #True
print(validar_repeticiones_vld("LL")) #False
print(validar_repeticiones_vld("DD")) #False
'''
