"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""

from calculadora.error import ExpresionInvalida
from calculadora.validaciones import (
    validar_orden_descendente,
    validar_repeticiones_icxm,
    validar_repeticiones_vld,
    validar_restas,
)
from calculadora.validaciones.alfabeto import validar_simbolos

diccionario = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Examples:
        >>> romano_a_entero("I")
        1
        >>> romano_a_entero("V")
        5
        >>> romano_a_entero("IV")
        4
        >>> romano_a_entero("IX")
        9
        >>> romano_a_entero("XIV")
        14
        >>> romano_a_entero("MCMXCIV")
        1994
        >>> romano_a_entero("MMMCMXCIX")
        3999

    Raises:
        ExpresionInvalida: Si la cadena no es válida según las reglas de números romanos (símbolos inválidos, repeticiones inválidas, orden incorrecto, restas inválidas)
    """
    total = 0
    valor_anterior = 0
    cadena_limpia = cadena.strip()
    # Validaciones antes de la conversión (zona de errores)
    if not validar_simbolos(cadena_limpia):
        raise ExpresionInvalida("La expresion contiene caracteres invalidos o está vacía.")
    if not validar_repeticiones_icxm(cadena_limpia):
        raise ExpresionInvalida("Error de sintaxis: repetición excesiva de I, X, C o M (máximo 3).")
    if not validar_repeticiones_vld(cadena_limpia):
        raise ExpresionInvalida("Error de sintaxis: los caracteres V, L o D no pueden repetirse.")
    if not validar_restas(cadena_limpia):
        raise ExpresionInvalida("Error semántico: se detectó una combinación de resta inválida.")
    if not validar_orden_descendente(cadena_limpia):
        raise ExpresionInvalida("Error de sintaxis: el orden de los caracteres es incorrecto.")
    # Usamos reversed() para cumplir con la pista del algoritmo recomendado
    for simbolo in reversed(cadena_limpia):
        valor_actual = diccionario[simbolo]
        if valor_actual < valor_anterior:
            # Caso resta
            total -= valor_actual
        else:
            # Caso suma
            total += valor_actual
        valor_anterior = valor_actual

    return total
    raise NotImplementedError()

''' zona de pruebas
print(romano_a_entero("I")) #1
print(romano_a_entero("V")) #5
print(romano_a_entero("IV")) #4
print(romano_a_entero("IX")) #9
print(romano_a_entero("XIV")) #14
print(romano_a_entero("MCMXCIV")) #1994
print(romano_a_entero("MMMCMXCIX")) #3999
'''
