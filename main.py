from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from ui import Ui_Form
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.firstStart = True

        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        if self.firstStart:
            self.firstStart = False
        else:
            qp = QPainter()
            qp.begin(self)
            self.drawEllipse(qp)
            qp.end()

    def drawEllipse(self, qp):
        qp.setBrush(QColor(random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)))
        r = random.randrange(100, 500, 1)
        x, y = 400 - int(r / 2), 300 - int(r / 2)
        qp.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
