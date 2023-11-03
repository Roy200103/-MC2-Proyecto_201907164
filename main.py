def evaluar_notacion_polaca(expresion):
    pila = []
    operadores = {'+', '-', '*', '/'}

    tokens = expresion.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            pila.append(int(token))
        elif token in operadores:
            if len(pila) < 2:
                raise ValueError("Error: no hay suficientes operandos para el operador {}.".format(token))
            operando2 = pila.pop()
            operando1 = pila.pop()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                if operando2 == 0:
                    raise ValueError("Error: división por cero.")
                resultado = operando1 / operando2
            pila.append(resultado)
        else:
            raise ValueError("Error: token no reconocido: {}".format(token))

    if len(pila) != 1:
        raise ValueError("Error: la expresión no está bien formada.")

    return pila[0]
c=True
while c:
    entrada=input("Ingrese notación polaca inversa: ")
    # Ejemplo de uso


    resultado = evaluar_notacion_polaca(entrada)
    print("Resultado:", resultado)
    print("Si desea salir ingrese 1, si no ingrese 2")
    op=int(input("Ingrese opción: "))
    if op == 1:
        c=False
    else:
        c=True


