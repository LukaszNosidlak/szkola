import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
import math

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Kalkulator')
        self.setGeometry(100, 100, 300, 400)

        self.result_line_edit = QLineEdit(self)
        self.result_line_edit.setReadOnly(True)
        self.result_line_edit.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result_line_edit.setStyleSheet('font-size: 18px;')

        layout = QVBoxLayout(self)

        buttons = [
            ('7', self.digit_pressed),
            ('8', self.digit_pressed),
            ('9', self.digit_pressed),
            ('/', self.operator_pressed),
            ('4', self.digit_pressed),
            ('5', self.digit_pressed),
            ('6', self.digit_pressed),
            ('*', self.operator_pressed),
            ('1', self.digit_pressed),
            ('2', self.digit_pressed),
            ('3', self.digit_pressed),
            ('-', self.operator_pressed),
            ('0', self.digit_pressed),
            ('.', self.decimal_pressed),
            ('=', self.calculate_result),
            ('+', self.operator_pressed),
            ('√', self.square_root_pressed),
            ('C', self.clear_result),
        ]

        for btn_text, btn_callback in buttons:
            btn = QPushButton(btn_text, self)
            btn.clicked.connect(btn_callback)
            layout.addWidget(btn)

        layout.addWidget(self.result_line_edit)

        self.show()

    def digit_pressed(self):
        button = self.sender()
        current_text = self.result_line_edit.text()

        # Sprawdź, czy poprzedni znak to operator, jeśli tak, dodaj spację przed cyfrą
        if current_text and current_text[-1] in ['+', '-', '*', '/']:
            self.result_line_edit.insert(' ' + button.text())
        # Jeśli nie, sprawdź, czy ostatnia cyfra zawiera już kropkę
        elif '.' not in current_text.split()[-1]:
            self.result_line_edit.insert(button.text())

    def operator_pressed(self):
        button = self.sender()
        current_text = self.result_line_edit.text()

        # Sprawdź, czy poprzedni znak to cyfra, jeśli tak, dodaj spację przed operatorem
        if current_text and current_text[-1].isdigit():
            self.result_line_edit.insert(' ' + button.text() + ' ')

    def decimal_pressed(self):
        current_text = self.result_line_edit.text()
        
        # Sprawdź, czy poprzednia część tekstu zawiera już kropkę
        if '.' not in current_text.split()[-1]:
            # Sprawdź, czy poprzedni znak to cyfra, jeśli tak, dodaj spację przed kropką
            if current_text and current_text[-1].isdigit():
                self.result_line_edit.insert('.')

    def calculate_result(self):
        try:
            expression = self.result_line_edit.text().replace('√', 'math.sqrt')
            result = eval(expression)
            if result.is_integer():
                result = int(result)
            self.result_line_edit.setText(str(result))
        except Exception as e:
            self.result_line_edit.setText('Error')

    def square_root_pressed(self):
        current_text = self.result_line_edit.text()
        
        # Sprawdź, czy poprzednia część tekstu nie zawiera cyfry, jeśli tak, dodaj pierwiastek kwadratowy
        if not current_text or not current_text[-1].isdigit():
            self.result_line_edit.insert('√')

    def clear_result(self):
        self.result_line_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec())


