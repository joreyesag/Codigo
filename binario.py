#Estudiantes:
#Jordan Reyes, Mateo Charro, Anthony Herrera
numero_decimal = int(input("Ingrese un número de dos(2) dígitos: "))

def decimal_a_binario_manual(numero_decimal):

    while numero_decimal <= 9 or numero_decimal >= 100:
        print("El número ingresado debe ser de dos(2) dígitos.")
        numero_decimal = int(input("Ingrese un número de dos(2) dígitos: "))

    residuos = []
    cociente = numero_decimal

    print("-" * 35)
    print(f"Iniciando conversión para el número: {numero_decimal}")
    print("-" * 35)

    while cociente > 0:
        residuo = cociente % 2
        nuevo_cociente = cociente // 2
        print(f"| {cociente} // 2 = {nuevo_cociente} | Residuo (bit): {residuo}")
        residuos.append(residuo)
        cociente = nuevo_cociente

    binario_invertido = "".join(map(str, residuos))
    binario_original = binario_invertido[::-1]

    print("-" * 35)
    print(f"Bits obtenidos (antes de invertir): {binario_invertido}")
    print(f"Binario invertido y original: {binario_original}")

    binario_8_bits = binario_original.zfill(8)
    print(f"Resultado final ajustado a 8 bits:")
    return binario_8_bits

mi_numero = numero_decimal
resultado_final = decimal_a_binario_manual(mi_numero)

print("=" * 35)
print(f"Resultado de {mi_numero} en 8 bits: {resultado_final}")
print("=" * 35)
