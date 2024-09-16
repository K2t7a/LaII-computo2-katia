import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QVBoxLayout

class DatosPersona(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Datos Personales")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # Etiqueta de género
        self.label_genero = QLabel("Seleccione su género:", self)
        layout.addWidget(self.label_genero)

        # Radiobox para género
        self.radio_hombre = QRadioButton("Hombre", self)
        self.radio_mujer = QRadioButton("Mujer", self)
        layout.addWidget(self.radio_hombre)
        layout.addWidget(self.radio_mujer)

        # Combobox para país de residencia
        self.label_pais = QLabel("Seleccione su país:", self)
        layout.addWidget(self.label_pais)

        self.combo_pais = QComboBox(self)
        self.combo_pais.addItems(["Costa Rica", "El Salvador", "Argentina", "Mexico", "Estados Unidos"])
        layout.addWidget(self.combo_pais)

        # Spinbox para edad
        self.label_edad = QLabel("Indique su edad:", self)
        layout.addWidget(self.label_edad)

        self.spinbox_edad = QSpinBox(self)
        self.spinbox_edad.setRange(1, 100)
        layout.addWidget(self.spinbox_edad)

        # Botón para enviar datos
        self.boton_enviar = QPushButton("Enviar", self)
        self.boton_enviar.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)

    def mostrar_datos(self):
        genero = "Hombre" if self.radio_hombre.isChecked() else "Mujer"
        pais = self.combo_pais.currentText()
        edad = self.spinbox_edad.value()

        print(f"Género: {genero}, País: {pais}, Edad: {edad}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DatosPersona()
    ventana.show()
    sys.exit(app.exec_())
