# id: 5 caracteres que describen el protocolo, el primero siempre una letra
# apellido y nombre del paciente, finaliza en una ","
# cantidad de estudios realizados: 2 caracteres
# segun la cantidad de estdio realizados, la codificacion de los estudios
# puede empezar por
# A: $300
# E: $420
# I: $670

# Ejemplo: A2462Reina Isabel,03A123E345E333
#          id   nombre       n estudios(n)

id: str
nombre: str
cantidad_estudios: str
codificacion_estudios: str  # "123" -> 123


def cargar_id():
    while (True):
        user_input = input("Ingrese el id: ")
        if user_input[0].isalpha() and len(user_input) == 5:
            return user_input
        else:
            print("El id ingresado no es valido.")


def cargar_nombre():
    while (True):
        user_input: str = input("Ingrese el nombre: ")
        if len(user_input) > 1:
            return user_input
        else:
            print("Debe ingresar un nombre valido")


def cargar_cantidad_estudios():
    while True:
        user_input: str = input("Ingrese la cantidad de estudios: ")
        if user_input.isdigit() and int(user_input) < 100:
            if int(user_input) > 9:
                return user_input
            else:
                return "0" + user_input
        else:
            print("El valor ingresado es incorrecto.")


def cargar_codificacion_estudios(cantidad_de_estudios: int) -> str:
    codigos_estudios = ""

    for nro_estudio in range(cantidad_de_estudios):
        while True:
            user_input: str = input(
                f"Ingrese el codigo del estudio {nro_estudio + 1} de {cantidad_de_estudios}: ")
            if user_input[0].isalpha() and len(user_input) == 4 and user_input[0] in ["A", "E", "I"]:
                codigos_estudios += user_input
                break
            else:
                print("El codigo ingresado no es valido.")

    return codigos_estudios


def calcular_total_gastos_estudio(codigo_paciente: str) -> int:
    lista = codigo_paciente.split(",")
    codigos_de_estudios = lista[1][2:]
    cantidad_de_bloques = len(codigos_de_estudios) // 4

    gastos_estudio = 0
    indice = 0
    for _ in range(cantidad_de_bloques):
        letra = codigos_de_estudios[indice]
        indice += 4

        match letra:
            case "A":
                gastos_estudio += 300
            case "E":
                gastos_estudio += 420
            case "I":
                gastos_estudio += 670
            case _:
                pass

    return gastos_estudio


id = cargar_id()
nombre = cargar_nombre()
cantidad_estudios = cargar_cantidad_estudios()
codificacion_estudios = cargar_codificacion_estudios(int(cantidad_estudios))


codigo_paciente: str = f"{id}{nombre},{cantidad_estudios}{codificacion_estudios}"
total_gastos_estudio: int = calcular_total_gastos_estudio(codigo_paciente)

print(f"Resultado: {codigo_paciente}")
print(f"Total de gastos de estudio: ${total_gastos_estudio}")
