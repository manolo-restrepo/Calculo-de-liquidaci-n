class SalarioInvalido(Exception):
    """Excepción que se dispara cuando el salario es menor o igual que cero"""

class DiasInvalidos(Exception):
    """Excepción que se dispara cuando los dias son menores o iguales a cero o son mayores a treinta"""

class VacacionesInvalidas(Exception):
    """Excepción que se dispara cuando las vacaciones son menores que cero"""

class IndemnizacionInvalida(Exception):
    """Excepción que se dispara cuando la indemnización es menor que cero"""



def calcular_liquidacion(salario_hora, dias_trabajados, vacaciones_pendientes=0, aplica_indemnizacion=False, valor_indemnizacion=0):
    """
    Calcula el valor total de una liquidación.

    salario_hora: valor pagado por hora trabajada
    dias_trabajados: número de días trabajados (1 a 30)
    vacaciones_pendientes: valor adicional por vacaciones
    aplica_indemnizacion: booleano
    valor_indemnizacion: monto adicional si aplica
    """

    # VALIDACIONES

    if salario_hora <= 0:
        raise SalarioInvalido("Salario debe ser mayor que cero")

    if dias_trabajados <= 0 or dias_trabajados > 30:
        raise DiasInvalidos("Días trabajados deben estar entre 1 y 30")

    if vacaciones_pendientes < 0:
        raise VacacionesInvalidas("Vacaciones no pueden ser negativas")

    if aplica_indemnizacion and valor_indemnizacion < 0:
        raise IndemnizacionInvalida("Indemnización no puede ser negativa")

    horas_por_dia = 10

    # Cálculamos el salario base
    total_base = salario_hora * horas_por_dia * dias_trabajados

    # Calculamos Vacaciones (se pagan como días adicionales)
    total_vacaciones = salario_hora * horas_por_dia * vacaciones_pendientes

    total = total_base + total_vacaciones

    # Verificamos Indemnización
    if aplica_indemnizacion:
        total += valor_indemnizacion

    return total