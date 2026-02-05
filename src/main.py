"""
Docstring for budget_software.budget_software.main:
Main file for budget software.

"""
# pylint: disable=import-error, undefined-variable
# temporary disabling of the pylint errors running up against PyQt5

import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

def main():
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
