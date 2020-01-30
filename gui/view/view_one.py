import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class PageOne(QDialog):
    def __init__(self):
        super().__init__()
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
        self.vbox.setAlignment(Qt.AlignCenter)

        self.label_banner = QLabel()
        self.label_banner.setPixmap(QPixmap("img\\routine_logo_1_cut.png"))
        self.label_banner.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.label_banner)

        self.init_group_box()
        self.vbox.addWidget(self.group_box)

        self.boton_siguiente = QPushButton("Continuar", self)
        self.boton_siguiente.setIcon(QIcon("img\\siguiente.png"))
        self.boton_siguiente.setIconSize(QSize(30, 30))
        self.vbox.addWidget(self.boton_siguiente)

        self.setLayout(self.vbox)

    def init_group_box(self):
        self.group_box = QGroupBox("Complete los siguientes campos")
        self.grid_layout = QGridLayout()

        self.label_obj = QLabel("<b>Fija un objetivo:</b>")
        self.label_obj.setAlignment(Qt.AlignLeft)
        self.entry_obj = QLineEdit()
        self.grid_layout.addWidget(self.label_obj, 0, 0)
        self.grid_layout.addWidget(self.entry_obj, 0, 1)

        self.label_num_act = QLabel("<b>Cantidad de actividades:</b>")
        self.label_num_act.setAlignment(Qt.AlignLeft)
        self.entry_num_act = QLineEdit()
        self.grid_layout.addWidget(self.label_num_act, 1, 0)
        self.grid_layout.addWidget(self.entry_num_act, 1, 1)

        self.label_num_hor = QLabel("<b>Cantidad de horas:</b>")
        self.label_num_hor.setAlignment(Qt.AlignLeft)
        self.entry_num_hor = QLineEdit()
        self.grid_layout.addWidget(self.label_num_hor, 2, 0)
        self.grid_layout.addWidget(self.entry_num_hor, 2, 1)

        self.group_box.setLayout(self.grid_layout)

    def show_info(self, text, err, title):
        msg = QMessageBox(self)
        msg.setWindowIcon(QIcon("img\\warning.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setText(err)
        msg.setInformativeText(text)
        msg.setWindowTitle(title)
        msg.show()


if __name__ == "__main__":
    # TEST PAGE_ONE:
    App = QApplication(sys.argv)
    page = PageOne()
    page.show()
    sys.exit(App.exec())
