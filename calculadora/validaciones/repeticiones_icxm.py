"""
Nivel 2: Validación de repeticiones I/X/C/M.

Los símbolos I, X, C y M pueden repetirse hasta 3 veces consecutivas.
Ejemplos válidos: III, XXX, CCC, MMM
Ejemplos inválidos: IIII, XXXX, CCCC, MMMM
"""
SIMBOLOS_REPETIBLES= ["I", "X", "C", "M"]
MAX_REPETICIONES= 3

def validar_repeticiones_icxm(cadena: str) -> bool:
    """
    Valida que los símbolos I, X, C, M no se repitan más de 3 veces consecutivas.

    Nivel 2: Análisis Sintáctico - Repeticiones de símbolos repetibles

    💡 PISTA: Verifica si existen los patrones "IIII", "XXXX", "CCCC", "MMMM"
    💡 PISTA: Si encuentras cualquier patrón de 4+ repeticiones, retorna False
    💡 PISTA: Recuerda: IIII, XXXX, CCCC, MMMM son INVÁLIDOS

    Args:
        cadena (str): La cadena de números romanos validada en Nivel 1

    Returns:
        bool: True si no hay más de 3 repeticiones, False en caso contrario

    Examples:
        >>> validar_repeticiones_icxm("III")
        True
        >>> validar_repeticiones_icxm("IIII")
        False
        >>> validar_repeticiones_icxm("XIX")
        True
        >>> validar_repeticiones_icxm("XXXX")
        False
        >>> validar_repeticiones_icxm("MMMCMXCIV")
        True
        >>> validar_repeticiones_icxm("MMMM")
        False
    """
    for caracter in SIMBOLOS_REPETIBLES: #un "for anidado"
        restriccion = caracter * (MAX_REPETICIONES + 1) # contara las veces que se repite el simbolo (no mas de 3)

        if restriccion in cadena: # si el simbolo se repite mas de 3 veces, la cadena no es valida
            return False
    return True

    raise NotImplementedError()

''' zona de pruebas
print(validar_repeticiones_icxm("III"))
print(validar_repeticiones_icxm("IIII"))
print(validar_repeticiones_icxm("XIX"))
print(validar_repeticiones_icxm("XXX"))
print(validar_repeticiones_icxm("XXXX"))
print(validar_repeticiones_icxm("CCCC"))
print(validar_repeticiones_icxm("MMMM"))
print(validar_repeticiones_icxm("MMMCMXCIV"))
'''
