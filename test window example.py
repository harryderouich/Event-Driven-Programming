import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from name_widget import *
from hello_widget import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        #Create both widgets from 'blueprint'
        self.name_widget = NameWidget()
        self.hello_widget = HelloWidget()

        #Create the stacked layout
        self.stack = QStackedLayout()


        #Add both widgets to the stacked layout
        self.stack.addWidget(self.name_widget)
        self.stack.addWidget(self.hello_widget)

        
        #Create a widget to use in the main window
        self.widget = QWidget()

        #Set the stacked layout to the widget
        self.widget.setLayout(self.stack)

        #Set the stacked layout widget as the central widget
        self.setCentralWidget(self.widget)

        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.BackPushed.connect(self.back_clicked)



    def name_provided(self):
        self.stack.setCurrentIndex(1)
        name = self.name_widget.username.text()
        self.name_widget.NameEntered.connect(self.name_provided)
        self.hello_widget.hellolabel.setText("Hello {0}".format(name))

    def back_clicked(self):
        self.stack.setCurrentIndex(0)
        self.name_widget.username.clear()
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
