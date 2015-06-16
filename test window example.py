import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from name_widget import *
from hello_widget import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.name_widget = NameWidget()
        self.setCentralWidget(self.name_widget)

        self.hello_widget = HelloWidget()
        #self.setCentralWidget(self.hello_widget)

        self.name_widget.NameEntered.connect(self.name_provided)

    def name_provided(self):
        print("got here")
        self.setCentralWidget(self.hello_widget)
        name = self.name_widget.username.text()
        print(name)
        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.hellolabel.setText("Hello {0}".format(name))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
