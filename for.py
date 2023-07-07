codigo_paciente = "A1234Matias Almiron,02I908E435"

lista = codigo_paciente.split(",")

print(lista)

codigos_de_estudios = lista[1][2:]
print(codigos_de_estudios)

cantidad_de_bloques = len(codigos_de_estudios) // 4
print(cantidad_de_bloques)

acumulador_total = 0
indice = 0
for _ in range(cantidad_de_bloques):
    letra = codigos_de_estudios[indice]
    indice += 4
    print(letra)

    match letra:
        case "A":
            acumulador_total += 300
        case "E":
            acumulador_total += 420
        case "I":
            acumulador_total += 670
        case _:
            pass

print(acumulador_total)
