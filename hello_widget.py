from PyQt4.QtGui import *
from PyQt4.QtCore import *

class HelloWidget(QWidget):
    BackPushed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
                
        #Create Components
        self.hellolabel = QLabel("Hello")
        self.back = QPushButton("Back")


        #Set the layout
        self.layout = QVBoxLayout()


        #Add the widgets to the layout
        self.layout.addWidget(self.hellolabel)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)


        self.back.clicked.connect(self.back_pushed)

    def back_pushed(self):
        self.BackPushed.emit()
            



       
