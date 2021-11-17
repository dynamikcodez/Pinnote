import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsOpacityEffect

x = 0
class MainWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Note app')
        
        text_box = QtWidgets.QTextEdit()
        self.pin_button = QtWidgets.QPushButton(text='Pin')
        slider_label = QtWidgets.QLabel("Adjust transparency below")
        
        
        v_layout = QtWidgets.QVBoxLayout()
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)

        self.slider.setRange(1,10)
        self.slider.setValue(1)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setTickInterval(1)

        self.slider_value = self.slider.value()

        # Changing transparency based on slider value
        self.slider.valueChanged.connect(lambda: self.setWindowOpacity(self.slider.value() *0.1))
        
        # adding opacity effect to the widget
        self.setWindowOpacity(0.5)

        self.setLayout(v_layout)
        
        v_layout.addWidget(text_box)
        v_layout.addWidget(self.pin_button)
        v_layout.addWidget(slider_label)
        v_layout.addWidget(self.slider)
        
        self.pin_button.clicked.connect(self.pin)
        self.show()
        
    def pin(self):
        global x
        #print(x)
        #need to think of a better way to check if button has been pressed
        #currently i'm using x as a sort of counter to handle that.
        if x % 2 == 0:
            self.pin_button.setText("Unpin")
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.pin_button.setText("Pin")
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        x+=1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWidget()
    sys.exit(app.exec_())
