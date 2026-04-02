"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.

    Nivel 7.1: Parsing completo de expresiones aritméticas de números romanos.

    💡 PISTA: Primero llama a tokenizar_expresion(expresion) para obtener los tokens
    💡 PISTA: Luego llama a validar_estructura_tokens(tokens) para validar la estructura
    💡 PISTA: Si validar_estructura_tokens(tokens) retorna False, lanza ExpresionInvalida
    💡 PISTA: Si la expresión está vacía (no tokens), retorna lista vacía []
    💡 PISTA: Usa try-except para capturar errores de tokenizar_expresion
    💡 PISTA: Mensaje de error: f'La expresión "{expresion}" tiene una estructura inválida'

    Args:
        expresion (str): La expresión a parsear

    Returns:
        List[Token]: La lista de tokens encontrados (vacía si la expresión es vacía)

    Raises:
        ExpresionInvalida: Si la expresión contiene caracteres inválidos o tiene estructura inválida

    Examples:
        >>> evaluar_expresion("XIV + LX")
        [Token("ROMANO", "XIV", 0), Token("ESPACIO", " ", 3), Token("SUMA", "+", 4), ...]
        >>> evaluar_expresion("")
        []
    """
    # para realizar esta parte primero se tiene que hacer los puntos 7.2 y 7.3, ya que se necesitan en esta función
    if not expresion.strip():
        return []
    try:
        # Tokenizar
        tokens = tokenizar_expresion(expresion)
        # Validacion de estructuras
        if not validar_estructura_tokens(tokens):
            raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
        return tokens
    except ExpresionInvalida as e:
        # Volver a hacer la excepción para que sea capturada por el nivel superior
        raise e
    raise NotImplementedError()


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza una expresión de texto en una lista de tokens.

    Nivel 7.2: Tokenización de expresiones aritméticas.

    💡 PISTA: Recorre la expresión caracter por caracter con un índice `i` usando while
    💡 PISTA: Usa if-elif para identificar el tipo de cada caracter:
    💡 PISTA:   - Espacio (' ') → Token('ESPACIO', ' ', i)
    💡 PISTA:   - Suma ('+') → Token('SUMA', '+', i)
    💡 PISTA:   - Resta ('-') → Token('RESTA', '-', i)
    💡 PISTA:   - Romano ('IVXLCDM') → Lee todos los caracteres romanos consecutivos
    💡 PISTA: Para números romanos:
    💡 PISTA:   - Guarda la posición inicial: inicio = i
    💡 PISTA:   - Avanza i mientras el caracter actual esté en 'IVXLCDM'
    💡 PISTA:   - Crea Token('ROMANO', expresion[inicio:i], inicio)
    💡 PISTA: Si el caracter no es ninguno de los anteriores, lanza ExpresionInvalida
    💡 PISTA: Mensaje de error: f"Carácter inválido '{expresion[i]}' en posición {i}"
    💡 PISTA: Ejemplo "XIV + LX":
    💡 PISTA:   - X(0) → ROMANO "XIV", i=3
    💡 PISTA:   - espacio(3) → ESPACIO, i=4
    💡 PISTA:   - +(4) → SUMA, i=5
    💡 PISTA:   - espacio(5) → ESPACIO, i=6
    💡 PISTA:   - L(6) → ROMANO "LX", i=8

    Args:
        expresion (str): La expresión a tokenizar

    Returns:
        List[Token]: La lista de tokens encontrados

    Raises:
        ExpresionInvalida: Si la expresión contiene caracteres inválidos

    Examples:
        >>> tokenizar_expresion("XIV + LX")
        [Token("ROMANO", "XIV", 0), Token("ESPACIO", " ", 3), Token("SUMA", "+", 4), ...]
        >>> tokenizar_expresion("X+V")
        [Token("ROMANO", "X", 0), Token("SUMA", "+", 1), Token("ROMANO", "V", 2)]
    """
    tokens = []
    i = 0
    alfabeto_romano = "IVXLCDM"

    while i < len(expresion):
        char = expresion[i]
        if char == ' ': # Si el caracter es un espacio, creamos un token de tipo ESPACIO
            tokens.append(Token("ESPACIO", " ", i))
            i += 1
        elif char == '+': # Si el caracter es una suma, creamos un token de tipo SUMA
            tokens.append(Token("SUMA", "+", i))
            i += 1
        elif char == '-': # Si el caracter es una resta, creamos un token de tipo RESTA
            tokens.append(Token("RESTA", "-", i))
            i += 1
        elif char in alfabeto_romano: # Si el caracter es un símbolo romano, leemos todos los caracteres romanos consecutivos
            inicio = i
            while i < len(expresion) and expresion[i] in alfabeto_romano: # Si el caracter actual es un símbolo romano, seguimos avanzando
                i += 1
            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))
        else:
            # Caracter no reconocido
            raise ExpresionInvalida(f"Caracter inválido '{char}' en posicion {i}")
    return tokens
    raise NotImplementedError()


def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida que la expresión tenga una estructura válida.

    Nivel 7.3: Validación de estructura de tokens.

    💡 PISTA: Filtra tokens de tipo 'ESPACIO' para facilitar la validación
    💡 PISTA: Usa list comprehension: [t for t in tokens if t.tipo != 'ESPACIO']
    💡 PISTA: Verifica que haya al menos 3 tokens (ROMANO, OPERADOR, ROMANO)
    💡 PISTA: Verifica que el número de tokens sea impar (alternancia correcta)
    💡 PISTA: Verifica que el primer token sea de tipo 'ROMANO'
    💡 PISTA: Verifica que el último token sea de tipo 'ROMANO'
    💡 PISTA: Recorre los tokens con enumerate(i, token):
    💡 PISTA:   - Posiciones pares (0, 2, 4, ...) deben ser 'ROMANO'
    💡 PISTA:   - Posiciones impares (1, 3, 5, ...) deben ser 'SUMA' o 'RESTA'
    💡 PISTA: Ejemplo [ROMANO, SUMA, ROMANO] → True (alternancia correcta)
    💡 PISTA: Ejemplo [SUMA, ROMANO] → False (empieza con operador)
    💡 PISTA: Ejemplo [ROMANO, SUMA, ROMANO, RESTA, ROMANO] → False (dos operadores seguidos)

    Args:
        tokens (List[Token]): La lista de tokens a validar

    Returns:
        bool: True si la estructura es válida, False en caso contrario

    Examples:
        >>> validar_estructura_tokens([Token("ROMANO", "X", 0), Token("SUMA", "+", 1), Token("ROMANO", "V", 2)])
        True
        >>> validar_estructura_tokens([Token("SUMA", "+", 0), Token("ROMANO", "X", 1)])
        False
    """
    tokens_se= [t for t in tokens if t.tipo != 'ESPACIO'] # Filtrar los tokens de tipo 'ESPACIO' para que sea
    # facil la validacion. Si no hay nada, no es una estructura válida
    if not tokens_se:
        return False
    # La estructura mínima es A + B (3 tokens) y debe ser impar (A, A+B, A+B-C...)
    if len(tokens_se) < 3 or len(tokens_se) % 2 == 0:
        return False
    # Validar alternancia
    for i, token in enumerate(tokens_se):
        if i % 2 == 0:
            # Posiciones 0, 2, 4... deben ser números
            if token.tipo != "ROMANO":
                return False
        else:
            # Posiciones 1, 3, 5... deben ser operadores
            if token.tipo not in ("SUMA", "RESTA"):
                return False
    return True
    raise NotImplementedError()
