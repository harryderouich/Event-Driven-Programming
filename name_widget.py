from PyQt4.QtGui import *
from PyQt4.QtCore import *

class NameWidget(QWidget):
    NameEntered = pyqtSignal()
    
    def __init__(self):
        super().__init__()
    
        #Create Components
        self.username = QLineEdit()
        self.label = QLabel("Please enter your name")
        self.submit = QPushButton("Submit")
    
    
        #Set the layout
        self.layout = QVBoxLayout()
    
        #Add the widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.submit)
    
        self.setLayout(self.layout)
    
    
        
        self.submit.clicked.connect(self.submit_pushed)
    
    def submit_pushed(self):
        name = self.username.text()
        self.NameEntered.emit()

        
