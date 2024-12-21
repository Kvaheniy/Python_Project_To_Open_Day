import string
import random
from main import MainApp
import PyQt5.QtWidgets as Qtw

class FirstApp(MainApp):
    def __init__(self, window_title: str, size_w: int, size_h: int):
        super().__init__(window_title, size_w, size_h)

        # Стиль вікна
        self.setStyleSheet("""
            QWidget {
                background-color: #4B0082;
                border: 0px solid #800080;
                border-radius: 25px;
            }
            QLabel {
                color: white;
                font-size: 16px;
            }
            QLineEdit {
                color: yellow;
                background-color: black;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton {
                background-color: #800080;
                color: white;
                border-radius: 5px;
                padding: 5px 15px;
            }
            QPushButton:hover {
                background-color: #9932CC;
            }
            QCheckBox {
                color: white;
                font-size: 14px;
            }
        """)

        # Розташування для введення довжини пароля
        self.h_layout2 = Qtw.QHBoxLayout()
        self.v_layout.addLayout(self.h_layout2)

        # Мітка "Довжина пароля"
        label_len = Qtw.QLabel('Довжина пароля: ')
        self.h_layout2.addWidget(label_len)

        # Поле для введення довжини
        self.len_field = Qtw.QLineEdit()
        self.len_field.setText('0')  # Довжина за замовчуванням
        self.h_layout2.addWidget(self.len_field)

        # Чекбокси для параметрів пароля
        self.uppercase_checkbox = Qtw.QCheckBox('Включити великі англійські букви')
        self.uppercase_checkbox.setChecked(True)
        self.v_layout.addWidget(self.uppercase_checkbox)

        self.lowercase_checkbox = Qtw.QCheckBox('Включити малі англійські букви')
        self.lowercase_checkbox.setChecked(True)
        self.v_layout.addWidget(self.lowercase_checkbox)

        self.ukr_uppercase_checkbox = Qtw.QCheckBox('Включити великі українські букви')
        self.ukr_uppercase_checkbox.setChecked(False)
        self.v_layout.addWidget(self.ukr_uppercase_checkbox)

        self.ukr_lowercase_checkbox = Qtw.QCheckBox('Включити малі українські букви')
        self.ukr_lowercase_checkbox.setChecked(False)
        self.v_layout.addWidget(self.ukr_lowercase_checkbox)

        self.jap_letters_checkbox = Qtw.QCheckBox('Включити японські символи (хіраґана)')
        self.jap_letters_checkbox.setChecked(False)
        self.v_layout.addWidget(self.jap_letters_checkbox)

        self.digits_checkbox = Qtw.QCheckBox('Включити цифри')
        self.digits_checkbox.setChecked(True)
        self.v_layout.addWidget(self.digits_checkbox)

        self.special_checkbox = Qtw.QCheckBox('Включити спец. символи')
        self.special_checkbox.setChecked(False)
        self.v_layout.addWidget(self.special_checkbox)

        # Поле для результату
        out_label = Qtw.QLabel('Ваш пароль: ')
        self.h_layout.addWidget(out_label)

        self.password_display = Qtw.QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setText('Ваш пароль')
        self.h_layout.addWidget(self.password_display)

        # Кнопка для генерації пароля
        botton_generation = Qtw.QPushButton('Згенерувати')
        botton_generation.clicked.connect(self.generation_password)
        self.h_layout.addWidget(botton_generation)

    def generation_password(self):
        """Генерує пароль на основі обраних параметрів."""
        try:
            length = int(self.len_field.text())  # Зчитуємо довжину пароля
        except ValueError:
            self.password_display.setText('Некоректна довжина!')
            return

        # Створення шаблону для пароля
        password_template = ''
        if self.uppercase_checkbox.isChecked():
            password_template += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            password_template += string.ascii_lowercase
        if self.ukr_uppercase_checkbox.isChecked():
            password_template += 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        if self.ukr_lowercase_checkbox.isChecked():
            password_template += 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        if self.jap_letters_checkbox.isChecked():
            password_template += 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'
        if self.digits_checkbox.isChecked():
            password_template += string.digits
        if self.special_checkbox.isChecked():
            password_template += string.punctuation

        # Перевірка, чи є символи для генерації
        if not password_template:
            self.password_display.setText('Оберіть параметри!')
            return

        # Генерація пароля
        password = ''.join(random.choice(password_template) for _ in range(length))
        self.password_display.setText(password)

if __name__ == '__main__':
    app = Qtw.QApplication([])
    window_one = FirstApp('Генератор паролів', 600, 300)
    app.exec_()