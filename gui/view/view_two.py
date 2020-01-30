# @Author : Roger Ramos (yihsic@gmail.com)

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout


class PageTwo(QDialog):
    def __init__(self, num_act=0):
        super().__init__()
        self.num_act = num_act
        self.campos_por_materia = [{"nom": "", "dif": "", "urg": "", "vol": ""} for i in range(self.num_act)]
        self.title = "Routine"
        self.iconName = "img\\logo.png"
        self.init_window()

    def set_num_act(self, n):
        self.num_act = n
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconName))
        self.init_vbox()
        self.setLayout(self.vbox)

    def init_vbox(self):
        self.vbox = QVBoxLayout()
        for i in self.campos_por_materia:
            index = self.campos_por_materia.index(i)
            self.group_box = QGroupBox(f"Actividad {index + 1}")
            self.grid_layout = QGridLayout()

            label_nom = QLabel("<b>Nombre: </b>")
            label_urg = QLabel("<b>Urgencia: </b>")
            label_dif = QLabel("<b>Dificultad: </b>")
            label_vol = QLabel("<b>Volumen: </b>")

            i["nom"] = QLineEdit()
            i["urg"] = QLineEdit()
            i["dif"] = QLineEdit()
            i["vol"] = QLineEdit()

            self.grid_layout.addWidget(label_nom, 0, 0)
            self.grid_layout.addWidget(i["nom"], 0, 1)
            self.grid_layout.addWidget(label_urg, 1, 0)
            self.grid_layout.addWidget(i["urg"], 1, 1)
            self.grid_layout.addWidget(label_dif, 2, 0)
            self.grid_layout.addWidget(i["dif"], 2, 1)
            self.grid_layout.addWidget(label_vol, 3, 0)
            self.grid_layout.addWidget(i["vol"], 3, 1)

            self.group_box.setLayout(self.grid_layout)
            self.vbox.addWidget(self.group_box)

        self.boton_continue = QPushButton("¡Generar rutina!")
        self.vbox.addWidget(self.boton_continue)

    def show_info(self, title, err, text):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon("img\\warning.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setText(err)
        msg.setInformativeText(text)
        msg.setWindowTitle(title)
        msg.show()


if __name__ == "__main__":
    # TEST PAGE_TWO
    App = QApplication(sys.argv)
    page = PageTwo(num_act=4)
    page.show_info("title test", "err", "text")
    page.show()

    sys.exit(App.exec())
