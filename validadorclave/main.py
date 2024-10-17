from validadorclave.modelo.validador import ReglaValidacionGanimedes, ReglaValidacionCalisto, Validador


def validar_clave(clave: str, reglas: list):
    for regla in reglas:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para la regla {regla.__class__.__name__}.")
        except ValueError as e:
            print(f"Error: {regla.__class__.__name__}: {e}")


if __name__ == "__main__":
    clave = "cAliStO123$"
    reglas = [ReglaValidacionGanimedes(), ReglaValidacionCalisto()]
    validar_clave(clave, reglas)
