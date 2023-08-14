import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import image_file 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r"E:\Projects\UI\calc.ui", self)
        self.setWindowIcon(QIcon(r'E:\Projects\UI\calculator.png'))

        self.result_calculated = False

        self.one.clicked.connect(lambda x:self.numbers("1"))
        self.two.clicked.connect(lambda x:self.numbers("2"))
        self.three.clicked.connect(lambda x:self.numbers("3"))
        self.four.clicked.connect(lambda x:self.numbers("4"))
        self.five.clicked.connect(lambda x:self.numbers("5"))
        self.six.clicked.connect(lambda x:self.numbers("6"))
        self.seven.clicked.connect(lambda x:self.numbers("7"))
        self.eight.clicked.connect(lambda x:self.numbers("8"))
        self.nine.clicked.connect(lambda x:self.numbers("9"))
        self.zero.clicked.connect(lambda x:self.numbers("0"))

        self.plus.clicked.connect(lambda x: self.operator('+'))
        self.minus.clicked.connect(lambda x: self.operator('-'))
        self.product.clicked.connect(lambda x: self.operator('x'))
        self.divide.clicked.connect(lambda x: self.operator('÷'))

        self.equalsto.clicked.connect(self.result)

        self.reset.clicked.connect(self.reset_method)
        self.delete_2.clicked.connect(self.delete_method)

    def numbers(self, number):
        text = self.label.text()
        if self.result_calculated:
            self.reset_method()  
            self.result_calculated = False  
        text = self.label.text()
        if text != "0":
            self.label.setText(text + number)
        else:
            self.label.setText(number)

  

    def operator(self, operators):
        text = self.label.text()
        if text.endswith(('+', 'x', '-', '÷')):
            text = text[:-1]
        if operators == "+":
            self.label.setText(text + "+")
        elif operators == '-':
            self.label.setText(text + '-')
        elif operators == 'x':
            self.label.setText(text + 'x')
        elif operators == '÷':
            self.label.setText(text + '÷')

    def result(self):
        try:
            text = self.label.text()
            if 'x' in text:
                text1 = text.replace('x', '*')
                if '÷' in text1:
                    text2 = text1.replace('÷', '/')
                    result = round(eval(text2), 3)
                else:
                    result = round(eval(text1), 3)
            elif '÷' in text:
                text1 = text.replace('÷', '/')
                if 'x' in text1:
                    text2 = text.replace('x', '*')
                    result = round(eval(text2),3)
                else:
                    result = round(eval(text1),3)
            else:
                result = eval(text)
            self.label.setText(str(result))
            self.result_calculated = True
        except:
            self.label.setText("Error")

    def reset_method(self):
        self.label.setText('0')

    def delete_method(self):
        text = self.label.text()
        if len(text) > 1:
            self.label.setText(text[:-1])
        else:
            self.label.setText('0')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())