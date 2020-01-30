# @Author : Roger Ramos (yihsic@gmail.com)

import sys

from PyQt5.QtWidgets import QApplication

from gui.controller.controller import Controller
from gui.model.model import Model
from gui.view.view_one import PageOne
from gui.view.view_three import PageThree
from gui.view.view_two import PageTwo


def main():
    app = QApplication(sys.argv)
    model = Model()
    page_one = PageOne()
    page_two = PageTwo()
    page_three = PageThree()
    controller = Controller(page_one, page_two, page_three, model)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
