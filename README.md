# Calculo-de-liquidaci-n
Desarrollado por:
Santiago Gonzalez Orrego
Kesman Posso Parra

Audio donde se explica acerca del proyecto: https://github.com/kesman0709/Calculo-de-liquidaci-n/blob/main/explicaci%C3%B3n%20del%20proyecto.m4a

Descripción: 
El sistema calcula el total a pagar a un empleado teniendo en cuenta: Salario por hora, Días trabajados, Vacaciones pendientes e Indemnización (si aplica).

Los casos de prueba fueron definidos previamente en un archivo Excel y la implementación se realizó con base en esos escenarios.

Formula usada:
El sistema asume una jornada laboral de 10 horas por día, de acuerdo con los valores definidos en los casos de prueba.

El total se calcula de la siguiente manera:
Salario base = salario_hora × 10 × días_trabajados
Vacaciones = salario_hora × 10 × vacaciones_pendientes
Total = salario base + vacaciones + indemnización (si aplica)

Validaciones:
El sistema valida que:
El salario por hora sea mayor que cero.
Los días trabajados estén entre 1 y 30.
Las vacaciones pendientes no sean negativas.
La indemnización no sea negativa si aplica

Pruebas:
Se implementaron pruebas unitarias utilizando la librería unittest.
Las pruebas cubren: Casos normales ,Casos extraordinarios, Casos de error
Los valores esperados utilizados en las pruebas son valores fijos definidos en el archivo Excel de casos de pruebas.
