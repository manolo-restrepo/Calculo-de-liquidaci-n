from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import sys
sys.path.append("src")

from model.logica_liquidacion import DatosLiquidacion, calcular_liquidacion


class LiquidacionApp(App):

    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=10)

        # 🔹 Entradas
        contenedor.add_widget(Label(text="Salario por hora"))
        self.salario = TextInput()
        contenedor.add_widget(self.salario)

        contenedor.add_widget(Label(text="Días trabajados"))
        self.dias = TextInput()
        contenedor.add_widget(self.dias)

        contenedor.add_widget(Label(text="Vacaciones pendientes"))
        self.vacaciones = TextInput(text="0")
        contenedor.add_widget(self.vacaciones)

        contenedor.add_widget(Label(text="Aplica indemnización (1=Sí, 0=No)"))
        self.aplica = TextInput(text="0")
        contenedor.add_widget(self.aplica)

        contenedor.add_widget(Label(text="Valor indemnización"))
        self.indemnizacion = TextInput(text="0")
        contenedor.add_widget(self.indemnizacion)

        # 🔹 Resultado
        self.resultado = Label(text="Resultado: ")
        contenedor.add_widget(self.resultado)

        # 🔹 Botón
        calcular = Button(text="Calcular")
        contenedor.add_widget(calcular)

        calcular.bind(on_press=self.calcular)

        return contenedor

    def calcular(self, instance):
        # 🔹 Convertir datos
        datos = DatosLiquidacion(
            salario_hora=float(self.salario.text),
            dias_trabajados=int(self.dias.text),
            vacaciones_pendientes=int(self.vacaciones.text),
            aplica_indemnizacion=bool(int(self.aplica.text)),
            valor_indemnizacion=float(self.indemnizacion.text),
        )

        # 🔹 Llamar tu lógica
        total = calcular_liquidacion(datos)

        # 🔹 Mostrar resultado
        self.resultado.text = "Total a pagar: " + str(total)


if __name__ == "__main__":
    LiquidacionApp().run()