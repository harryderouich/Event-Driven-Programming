from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HelloWidget(QWidget):
    def __init__(self):
        super().__init__()
                

        self.hellolabel = QLabel("Hello")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.hellolabel)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        

       
