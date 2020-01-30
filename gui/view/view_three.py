# @Author : Roger Ramos (yihsic@gmail.com)

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class PageThree(QDialog):
    def __init__(self, list_poms=[], obj=""):
        super().__init__()
        self.list_poms = list_poms
        self.obj = obj
        self.title = "Routine"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 250
        self.iconName = "img\\logo.png"
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout()
        self.label_banner = QLabel()
        self.label_banner.setPixmap(QPixmap("img\\routine_logo_3"))
        self.label_banner.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.label_banner)
        self.label_obj = QLabel(f"<h1>¡{self.obj.title()}!</h1>")
        self.label_obj.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.label_obj)
        self.init_poms_group_box()
        self.vbox.addWidget(self.group_box)
        self.setLayout(self.vbox)

    def init_poms_group_box(self):
        self.group_box = QGroupBox("@Routine - ¡A trabajar! ")
        self.grid_layout = QGridLayout()
        i = 0
        for pom in self.list_poms:
            text = f"<h1>{pom.ID + 1}º</h1>"
            text += f"<h2>{pom.act.nom.upper()}</h2>\n"
            text += f"<h3>Trabajo: <b>{pom.MINUTOS_TRABAJO}</b> min.</h3>\n"
            text += f"<h3>Descanso: <b>{pom.MINUTOS_DESCANSO}</b> min.</h3>\n"
            label = QLabel(text)
            label.setAlignment(Qt.AlignCenter)
            f = int((i - (i % 6)) / 6)
            c = int(i % 6)
            self.grid_layout.addWidget(label, f, c)
            i += 1

        self.group_box.setLayout(self.grid_layout)


if __name__ == '__main__':
    # TEST PAGE_THREE
    from src.actividad import Actividad
    from src.pomodoro import Pomodoro

    App = QApplication(sys.argv)
    page = PageThree([Pomodoro(Actividad("aritmetiCa", 3, 3, 4)), Pomodoro(Actividad("fiSiCa", 3, 3, 4))],
                     obj="AumEntaR inGresos")
    page.show()
    sys.exit(App.exec())
