import src.model.logica_liquidacion as logica_liquidacion

try:
    print("=== Cálculo de Liquidación ===")

    salario = float(input("Salario por hora: "))
    dias = int(input("Días trabajados: "))
    vacaciones = float(input("Valor vacaciones pendientes: "))

    aplica = input("¿Aplica indemnización? (s/n): ").lower()
    if aplica == "s":
        valor_indemnizacion = float(input("Valor indemnización: "))
        aplica_bool = True
    else:
        valor_indemnizacion = 0
        aplica_bool = False

    total = logica_liquidacion.calcular_liquidacion(
        salario,
        dias,
        vacaciones,
        aplica_bool,
        valor_indemnizacion
    )

    print(f"Total liquidación: {total}")

except Exception as e:
    print("Error:", e)